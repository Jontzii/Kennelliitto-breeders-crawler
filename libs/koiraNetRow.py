class KoiraNetRow:
    breeder: str | None = None
    has_breeder_commitment: bool = False
    breeder_url: str = "https://jalostus.kennelliitto.fi/"
    litters: int
    puppies: int
    first_litter_year: int
    latest_litter_year: int
    average_breeding_age: int
    average_litters_per_year: int
    fi_mva: int | None = None
    amount_of_other_breeds_with_litters: int
    total_litters: int

    def __init__(self, row):
        cells = row.find_all("td")

        self.breeder = cells[0].get_text().split("*")[0]
        self.has_breeder_commitment = "*" in cells[0].get_text()
        self.breeder_url += cells[0].find("a")["href"]
        self.litters = int(cells[1].get_text())
        self.puppies = int(cells[2].get_text())
        self.first_litter_year = int(cells[3].get_text())
        self.latest_litter_year = int(cells[4].get_text())
        self.average_breeding_age = self._average_breeding_age_to_float(
            cells[5].get_text()
        )
        self.average_litters_per_year = float(cells[6].get_text().replace(",", "."))
        self.fi_mva = self._fi_mva_value(cells[7].get_text())
        self.amount_of_other_breeds_with_litters = len(cells[8].find_all("a"))
        self.total_litters = int(cells[9].get_text())

    def _average_breeding_age_to_float(self, age: str) -> float:
        years = age.split(" v")[0]
        months = age.split(" kk")[0].split(" ")[-1]

        if years == "":
            years = 0

        if months == "":
            months = 0

        return float(years) + round(float(months) / 12, 2)

    def _fi_mva_value(self, value: str) -> int | None:
        if value != "":
            return int(value)
    
        return None

    def toList(self) -> list:
        return [
            self.breeder,
            self.has_breeder_commitment,
            self.breeder_url,
            self.litters,
            self.puppies,
            self.first_litter_year,
            self.latest_litter_year,
            self.average_breeding_age,
            self.average_litters_per_year,
            self.fi_mva,
            self.amount_of_other_breeds_with_litters,
            self.total_litters,
        ]

    def __str__(self) -> str:
        return f"{self.breeder} - {self.litters} - {self.puppies} - {self.first_litter_year} - {self.latest_litter_year} - {self.average_breeding_age} - {self.average_litters_per_year} - {self.fi_mva} - {self.amount_of_other_breeds_with_litters} - {self.total_litters}"
