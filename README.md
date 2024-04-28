# Kennelliitto Breeder Crawler

Get only the breeders that match your requirements, nicely given as Excel and CSV files.

## Settings

Before running set the settings to your liking in the `main.py`. Only required value is `Breed`.

|Setting|Description|Default|
|--|--|--|
|breed|Breed of the dog in number, get it from the website||
|max_years_from_last_litter|Max years from the last litter|`None`|
|max_litters_per_year|What is the max amount of litters per year|`None`|
|require_breeder_commitment|Require breeder commitment "Kasvattajasitoumus"|`False`|
|max_amount_of_other_breeds|What is the max amount of other dog breeds the breeder has litters in|`None`|
|min_litters|Minimum amount of litters|`None`|
|max_litters|Maximum amount of litters|`None`|

## Running

Example commands for running.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

The program will generate .csv and .xlsx files containing the same information.
