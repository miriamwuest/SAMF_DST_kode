# lidt pænere udskrifter i terminalen
from pprint import pprint

from dstapi import DstApi

# brug denne her stump til at browse DSTs tabeller og variable, så du kan finde ud af, hvilke tabeller og variable du vil hente data fra.

ind = DstApi("FOLK1A")

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
