# pip install pandas faker

import random

import pandas as pd
from faker import Faker

fake = Faker("pl_PL")

ILE_LOSOWYCH = 10_000
csv_file_pandas = "dane_losowe_csv.csv"
xlsx_file_pandas = "dane_losowe_excel.xlsx"

enc = "utf-8"

fake_records = [
    {
        "id": fake.uuid4(),
        "imie": fake.first_name(),
        "nazwisko": fake.last_name(),
        "nazwa_firmy": fake.company(),
        "email": fake.email(),
        "telefon": fake.phone_number(),
        "miasto": fake.city(),
        "wiek": random.randint(18, 70),
    }
    for _ in range(ILE_LOSOWYCH)
]

# zapis z wykorzystaniem Pandas
tabela = pd.DataFrame(fake_records)
tabela.to_csv(csv_file_pandas, index=False, sep=";")
tabela.to_excel(xlsx_file_pandas, index=False)
