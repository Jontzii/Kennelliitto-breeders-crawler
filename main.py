import urllib.request
from bs4 import BeautifulSoup
from libs.koiraNetTable import KoiraNetTable
from libs.settings import Settings

def main():
    settings = Settings(
        breed = 189, # Suomenlapinkoira
        max_years_from_last_litter = 2, # max 2 vuotta viimeisestä pentueesta
        max_litters_per_year = 2, # Montako pentuetta maksimissaan keskimäärin vuodessa
        require_breeder_commitment = True, # Kasvattajasitoumus oltava voimassa
        max_amount_of_other_breeds = 1, # Monessako muussa rodussa kennelillä voi olla pentuja
        min_litters = 1, # Montako pentuetta vähintään yhteensä
        max_litters = 25 # Montako pentuetta maksimissaan yhteensä
    )

    with urllib.request.urlopen(settings.get_url()) as response:
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find(id="Table")

    koiraNetTable = KoiraNetTable(table, settings)
    koiraNetTable.toCsv(f"{settings.get_file_name()}.csv")
    koiraNetTable.toExcel(f"{settings.get_file_name()}.xlsx")

if __name__ == "__main__":
    main()
