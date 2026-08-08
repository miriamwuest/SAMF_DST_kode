# dette program er et end to end eksempel på, hvordan man kan hente data fra Danmarks Statistik via deres API.
# det henter data fra Danmarks Statistik via deres API.
# senere deler vi det op: vi bruger browse_tables.py til at browse tabeller og variable, og export_dst.py til at hente data fra tabellerne.

# vi bruger Alessandro Martinellos dstapi modul, som er en wrapper til DSTs API.
# før det her kan virke, skal der via terminalen installeres en pakke:
# pip install git+https://github.com/alemartinello/dstapi
# ved at installere pakken installeres også numpy og pandas, som dstapi afhænger af.

# lidt pænere udskrifter i terminalen
from pprint import pprint

from dstapi import DstApi

# nu kan vi bruge DSTs API til at hente data.
# her vælger vi en tabel om personindkomster og kalder den ind.

ind = DstApi("INDKP107")

# tablesummary er en operation, der henter metadata om tabellen.
# vi gemmer indhold i s og viser det i terminalen.

s = ind.tablesummary(language="da")
print("============ Table summary ============")
print(s)

# her kan vi se, hvilke variable der findes i tabellen og deres mulige værdier.
print("============ Variable levels ============")
for variable in s["variable name"]:
    print(variable + ":")
    print(ind.variable_levels(variable, language="da"))

# her definerer vi, hvilke parametre der skal bruges til at hente data fra tabellen.
# define_base_params er en operation fra dstapi modulet, der henter metadata om tabellen og returnerer en dictionary med de parametre, der skal bruges til at hente data.
params = ind._define_base_params(language="da")

print("============ Parameters ============")
pprint(params)

# nu vælger vi
# Adjust the parameters of variables according to my needs
params["variables"][0]["values"] = ["000"]  # hele landet
params["variables"][1]["values"] = ["116"]  # gsn for alle personer
params["variables"][2]["values"] = ["MOK"]  # m og k i alt
params["variables"][3]["values"] = ["*"]  # alle uddannelsesniveauer
params["variables"][4]["values"] = ["115"]  # løn
params["variables"][5]["values"] = [">=2018<=2024"]  # fra og med 2018 til og med 2024

print("============ Adjusted Parameters ============")
pprint(params)

# få data
data = ind.get_data(params=params)
print("============ Data ============")
print(data)

# gem data som .csv fil
data.to_csv("data/indkomst_data.csv")
