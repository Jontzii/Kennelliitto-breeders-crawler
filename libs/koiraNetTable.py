import pandas as pd
from libs.koiraNetRow import KoiraNetRow
from libs.settings import Settings


class KoiraNetTable:
    dataFrame: pd.DataFrame = None

    table_headers = [
        "Kasvattaja",
        "Kasvattajasopimus",
        "Kasvattajan sivu",
        "Pentueet",
        "Pennut",
        "Ensimmäinen pentue",
        "Viimeisin pentue",
        "Emän keskimääräinen jalostusikä",
        "Pentueita keskimäärin vuodessa",
        "FI MVA",
        "Pentueet muissa roduissa",
        "Yhteensä pentueita",
    ]

    def __init__(self, table, settings: Settings):
        # Get data
        rows = table.find_all("tr")

        # Remove headers
        rows = [row for row in rows if row.find("th") is None]

        # Create rows from the table
        koiraNetRows: list[KoiraNetRow] = []

        for row in rows:
            koiraNetRow = KoiraNetRow(row)

            # Filter based on settings
            if self._check_row_against_settings(koiraNetRow, settings):
                koiraNetRows.append(koiraNetRow)

        # Create a DataFrame from the rows
        self.dataFrame = pd.DataFrame(
            [koiraNetRow.toList() for koiraNetRow in koiraNetRows],
            columns=self.table_headers,
        )

    def _check_row_against_settings(self, row: KoiraNetRow, settings: Settings) -> bool:
        if settings.require_breeder_commitment and not row.has_breeder_commitment:
            return False
        
        if settings.max_litters_per_year is not None:
            if row.average_litters_per_year > settings.max_litters_per_year:
                return False

        if settings.max_amount_of_other_breeds is not None:
            if row.amount_of_other_breeds_with_litters > settings.max_amount_of_other_breeds:
                return False

        if settings.min_litters is not None:
            if row.total_litters < settings.min_litters:
                return False

        if settings.max_litters is not None:
            if row.total_litters > settings.max_litters:
                return False

        return True

    def toCsv(self, path: str):
        self.dataFrame.to_csv(path, index=False)

    def toExcel(self, path: str):
        self.dataFrame.to_excel(path, sheet_name="Kasvattajat", index=False)
