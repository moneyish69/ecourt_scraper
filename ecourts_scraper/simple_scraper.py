"""Simple requests-based scraper for eCourts"""

import requests
from bs4 import BeautifulSoup
from typing import List
from .fallback_data import FALLBACK_STATES, FALLBACK_DISTRICTS, FALLBACK_COMPLEXES, FALLBACK_COURTS

class SimpleEcourtsScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.base_url = "https://services.ecourts.gov.in/ecourtindia_v6/"
        
    def get_states(self) -> List[str]:
        """Get states using requests"""
        try:
            url = f"{self.base_url}?p=cause_list/"
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                state_select = soup.find('select', {'id': 'sess_state_code'})
                if state_select:
                    options = [opt.text.strip() for opt in state_select.find_all('option') 
                             if opt.text.strip() and opt.text.strip() != "Select State"]
                    if options:
                        return options
            raise Exception("No states found")
        except Exception:
            print("Using fallback states")
            return FALLBACK_STATES
            
    def get_districts(self, state_name: str) -> List[str]:
        """Get districts using fallback data"""
        return FALLBACK_DISTRICTS.get(state_name, ["District 1", "District 2", "District 3"])
        
    def get_court_complexes(self, state_name: str, district_name: str) -> List[str]:
        """Get court complexes using fallback data"""
        return FALLBACK_COMPLEXES.get(district_name, ["Court Complex 1", "Court Complex 2"])
        
    def get_courts(self, state_name: str, district_name: str, complex_name: str) -> List[str]:
        """Get courts using fallback data"""
        return FALLBACK_COURTS.get(complex_name, ["Court No. 1", "Court No. 2", "Court No. 3"])