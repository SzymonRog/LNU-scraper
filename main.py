from Submitter.submitter import Submitter
from db_menager import DbManager
from exporter import Exporter
from scraper import Scraper

db_manager = DbManager()
scraper = Scraper()
exporter = Exporter()

# scraper.update_sort_order()
sub = Submitter(scraper.session)
sub.submit_by_path(db_manager, r'{^menu_lessons}\Język Python\Poziom Rozszerzony\Iteratory i listy składane', delay=10.0)

