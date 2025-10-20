"""ecourts_scraper package.

Provides utilities to scrape eCourts cause lists, lookup cases, and download PDFs.
"""

from .scraper import EcourtsScraper, CourtSelection, DownloadResult
from .case_lookup import EcourtsCaseLookup, CaseDetails, CaseListing, SearchResult

__all__ = [
    "EcourtsScraper",
    "CourtSelection", 
    "DownloadResult",
    "EcourtsCaseLookup",
    "CaseDetails",
    "CaseListing",
    "SearchResult",
]
