class Settings:
    base_url = "https://jalostus.kennelliitto.fi/frmKasvattajat.aspx"

    # Rodun numero
    breed: int

    # Montako vuotta enintään viimeisestä pentueesta
    max_years_from_last_litter: int | None = None

    # Montako pentuetta maksimissaan keskimäärin vuodessa
    max_litters_per_year: int | None = None

    # Onko kasvattajasitoumus oltava voimassa
    require_breeder_commitment: bool | None = None

    # Monessako muussa rodussa kennelillä voi olla pentuja
    max_amount_of_other_breeds: int | None = None  

    # Montako pentuetta vähintään yhteensä
    min_litters: int | None = None

    # Montako pentuetta maksimissaan yhteensä
    max_litters: int | None = None

    def __init__(
        self,
        breed: int,
        max_years_from_last_litter: int | None = None,
        max_litters_per_year: int | None = None,
        require_breeder_commitment: bool | None = None,
        max_amount_of_other_breeds: int | None = None,
        min_litters: int | None = None,
        max_litters: int | None = None,
    ) -> None:
        self.breed = breed
        self.max_years_from_last_litter = max_years_from_last_litter
        self.max_litters_per_year = max_litters_per_year
        self.require_breeder_commitment = require_breeder_commitment
        self.max_amount_of_other_breeds = max_amount_of_other_breeds
        self.min_litters = min_litters
        self.max_litters = max_litters

    def get_url(self) -> str:
        return f"{self.base_url}?{self._get_url_options()}"

    def get_file_name(self) -> str:
        return f"output_breed_{self.breed}"

    def _get_url_options(self) -> str:
        url_options = [
            f"R={str(self.breed)}",
            f"V={str(self.max_years_from_last_litter)}",
        ]
        return "&".join(url_options)
