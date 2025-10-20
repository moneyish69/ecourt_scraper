"""Fallback data for eCourts when site is slow/down"""

FALLBACK_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
    "Delhi", "Jammu and Kashmir", "Ladakh", "Puducherry"
]

FALLBACK_DISTRICTS = {
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Thane", "Nashik", "Aurangabad", "Solapur", "Kolhapur"],
    "Delhi": ["Central Delhi", "East Delhi", "New Delhi", "North Delhi", "South Delhi", "West Delhi"],
    "Karnataka": ["Bangalore", "Mysore", "Hubli", "Mangalore", "Belgaum", "Gulbarga"],
    "Tamil Nadu": ["Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem", "Tirunelveli"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Ghaziabad", "Agra", "Varanasi", "Meerut", "Allahabad"],
    "West Bengal": ["Kolkata", "Howrah", "Durgapur", "Asansol", "Siliguri", "Malda"],
    "Gujarat": ["Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar", "Jamnagar"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Bikaner", "Udaipur", "Ajmer"],
    "Punjab": ["Ludhiana", "Amritsar", "Jalandhar", "Patiala", "Bathinda", "Mohali"],
    "Haryana": ["Gurgaon", "Faridabad", "Panipat", "Ambala", "Yamunanagar", "Rohtak"]
}

FALLBACK_COMPLEXES = {
    "Mumbai": ["Bandra Family Court", "Borivali Family Court", "Andheri Family Court", "Fort Court Complex"],
    "Delhi": ["Tis Hazari Courts", "Karkardooma Courts", "Rohini Courts", "Dwarka Courts"],
    "Bangalore": ["City Civil Court", "City Sessions Court", "High Court Complex"],
    "Chennai": ["City Civil Court", "Metropolitan Magistrate Court", "High Court Complex"],
    "Pune": ["Pune District Court", "Pune Sessions Court", "Pune Family Court"],
    "Kolkata": ["Calcutta High Court", "Alipore Court", "Bankshall Court"]
}

FALLBACK_COURTS = {
    "Bandra Family Court": ["Court No. 1", "Court No. 2", "Court No. 3"],
    "Borivali Family Court": ["Court No. 1", "Court No. 2"],
    "Andheri Family Court": ["Court No. 1", "Court No. 2", "Court No. 3"],
    "Fort Court Complex": ["Court No. 1", "Court No. 2", "Court No. 3", "Court No. 4"],
    "Tis Hazari Courts": ["Court No. 1", "Court No. 2", "Court No. 3", "Court No. 4", "Court No. 5"],
    "City Civil Court": ["Court No. 1", "Court No. 2", "Court No. 3"],
    "Pune District Court": ["Court No. 1", "Court No. 2", "Court No. 3", "Court No. 4"]
}