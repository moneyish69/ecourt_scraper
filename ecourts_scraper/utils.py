import json
import os
import re
from dataclasses import asdict
from datetime import datetime
from typing import Any, Dict, Optional


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def sanitize_filename(name: str) -> str:
    sanitized = re.sub(r"[^A-Za-z0-9_.-]+", "_", name).strip("._")
    return sanitized or "file"


def build_output_filename(state: str, district: str, complex_: str, court: str, date_str: str) -> str:
    parts = [state, district, complex_, court, date_str]
    joined = "_".join(sanitize_filename(p) for p in parts if p)
    return f"{joined}.pdf"


def append_history(log_path: str, record: Dict[str, Any]) -> None:
    ensure_directory(os.path.dirname(log_path) or ".")
    existing: Optional[list] = None
    if os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = None
    if existing is None:
        existing = []
    record_with_timestamp = {**record, "timestamp": datetime.utcnow().isoformat() + "Z"}
    existing.append(record_with_timestamp)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
