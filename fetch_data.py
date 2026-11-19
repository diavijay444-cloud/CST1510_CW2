from pathlib import Path
import requests
import pandas as pd

URL = "https://disease.sh/v3/covid-19/countries"
RECORDS_KEY = None
KEEP = ["country", "continent", "cases", "deaths", "population"]

response = requests.get(URL, timeout=30)
print("Status:", response.status_code)
response.raise_for_status()

data = response.json()
records = data if RECORDS_KEY is None else data[RECORDS_KEY]

table = pd.DataFrame(records)
tidy_data = table[KEEP].copy()
tidy_data.columns = [c.strip().lower().replace(" ", "_") for c in tidy_data.columns]

print(tidy_data.head())

out_path = Path(__file__).resolve().parent / "DATA" / "raw.csv"
tidy_data.to_csv(out_path, index=False)
print(f"Saved {len(tidy_data)} rows to {out_path}")