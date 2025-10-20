import os
from datetime import date
from typing import List

import streamlit as st

from ecourts_scraper import EcourtsScraper, CourtSelection
from ecourts_scraper.utils import append_history
from ecourts_scraper.simple_scraper import SimpleEcourtsScraper


st.set_page_config(page_title="eCourts Cause List Downloader", page_icon="📄", layout="centered")


@st.cache_resource(show_spinner=False)
def get_scraper() -> EcourtsScraper:
    return EcourtsScraper(downloads_dir="downloads")

@st.cache_resource(show_spinner=False)
def get_simple_scraper() -> SimpleEcourtsScraper:
    return SimpleEcourtsScraper()


def main() -> None:
    st.title("eCourts Cause List Downloader")
    st.caption("Fetch live cause list PDFs directly from the official eCourts website.")

    scraper = get_scraper()

    # Use fallback data immediately for faster loading
    simple_scraper = get_simple_scraper()
    states = simple_scraper.get_states()
    st.info("Using fallback data for faster loading")

    state = st.selectbox("State", options=[""] + states, index=0)

    districts: List[str] = []
    if state:
        districts = simple_scraper.get_districts(state)

    district = st.selectbox("District", options=[""] + districts, index=0, disabled=not bool(state))

    complexes: List[str] = []
    if state and district:
        complexes = simple_scraper.get_court_complexes(state, district)

    court_complex = st.selectbox(
        "Court Complex",
        options=[""] + complexes,
        index=0,
        disabled=not bool(state and district),
    )

    courts: List[str] = []
    if court_complex:
        courts = simple_scraper.get_courts(state, district, court_complex)

    court_name = st.selectbox(
        "Court Name",
        options=[""] + courts,
        index=0,
        disabled=not bool(court_complex),
    )

    all_courts = st.checkbox("Download All Courts under this Complex")
    sel_date = st.date_input("Cause List Date", value=date.today(), format="DD-MM-YYYY")
    case_type = st.radio("Case Type", ["Civil", "Criminal"], horizontal=True)

    if st.button("Download Cause List", type="primary"):
        if not (state and district and court_complex and (court_name or all_courts)):
            st.error("Invalid selection. Please choose State, District, Complex, and Court.")
            return
        selection = CourtSelection(
            state=state,
            district=district,
            court_complex=court_complex,
            court_name=court_name or "",
            on_date=sel_date,
            case_type=case_type,
        )
        if all_courts:
            with st.spinner("Downloading PDFs for all courts..."):
                count, paths = scraper.download_all_courts_in_complex(selection, courts)
                if count == 0:
                    st.warning("No cause list available for this date.")
                else:
                    for p in paths:
                        st.success(f"Downloaded: {p}")
                for p in paths:
                    append_history(
                        os.path.join(".", "history.json"),
                        {
                            "state": state,
                            "district": district,
                            "court_complex": court_complex,
                            "court_name": "*",
                            "date": sel_date.isoformat(),
                            "case_type": case_type,
                            "download_path": p,
                        },
                    )
        else:
            with st.spinner("Downloading PDF..."):
                res = scraper.download_cause_list_pdf(selection)
                if not res.ok or not res.file_path:
                    st.warning(res.message or "No cause list available for this date.")
                else:
                    st.success(f"Downloaded: {res.file_path}")
                    append_history(
                        os.path.join(".", "history.json"),
                        {
                            "state": state,
                            "district": district,
                            "court_complex": court_complex,
                            "court_name": court_name,
                            "date": sel_date.isoformat(),
                            "case_type": case_type,
                            "download_path": res.file_path,
                        },
                    )


if __name__ == "__main__":
    main()
