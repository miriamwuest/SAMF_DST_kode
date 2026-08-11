import pandas as pd

from dstapi import DstApi

# for all yearly tables, we set the yearUntil variable to make updates easy.
yearUntil = 2024


# define a function to export data from a DST table based on a package of parameters
def export_data(package):
    table = DstApi(package["table_id"])
    params = table._define_base_params(language="da")
    for i, variable in enumerate(params["variables"]):
        variable["values"] = package["variable_values"][i]
    data = table.get_data(params=params)
    data.to_csv(package["output_file"])


# add a package for each table you want to export data from, with the table ID, output file name, and variable values to filter the data by.
# HISB3: Befolkning

pkgHISB3 = {
    "table_id": "HISB3",
    "output_file": "data/HISB3_data.csv",
    "variable_values": [
        ["M+K", "LFT", "DT", "IND", "UDV"],  #  befolk hele landet osv
        [f">=2001<={yearUntil}"],  # fra og med 2001 til og med {yearUntil}
    ],
}

# INDPK107
pkgIndk = {
    "table_id": "INDKP107",
    "output_file": "data/indkomst_data.csv",
    "variable_values": [
        ["000"],  # hele landet
        ["116"],  # gsn for alle personer
        ["MOK"],  # m og k i alt
        ["*"],  # alle uddannelsesniveauer
        ["115"],  # løn
        [f">=2018<={yearUntil}"],  # fra og med 2018 til og med {yearUntil}
    ],
}


# use the export_data function to export data from each table defined in the packages.
export_data(pkgHISB3)
export_data(pkgIndk)


# pivot tables may be neccessary to make the data easier to work with. The following code pivots the HISB3 data and saves it to a new CSV file.

# hisb
HISB3_data = pd.read_csv("data/HISB3_data.csv", sep=",", encoding="utf-8")
# print(HISB3_data)

pivoted = HISB3_data.pivot(index="BEVÆGELSE", columns="TID", values="INDHOLD")
pivoted.to_csv("data/HISB3_data_pivoted.csv", sep=",", encoding="utf-8")
# print(pivoted)
