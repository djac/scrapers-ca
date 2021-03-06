from utils import CSVScraper

from datetime import date


class UxbridgePersonScraper(CSVScraper):
    csv_url = 'https://docs.google.com/spreadsheets/d/1NIW_hM8gm0AlbTvWGBXaBU9DTeom74z5ZhrA10Z94G4/pub?gid=171849574&single=true&output=csv'
    updated_at = date(2018, 4, 16)
    contact_person = 'joe.murray@jmaconsulting.biz'
    many_posts_per_area = True
    unique_roles = ('Mayor', 'Regional Councillor')
