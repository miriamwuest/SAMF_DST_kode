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

# FOLK1A
pkgBefolkning = {
    "table_id": "FOLK1A",
    "output_file": "data/befolkning_data.csv",
    "variable_values": [
        ["000"],  # hele landet
        ["TOT"],  # m og k i alt
        ["*"],  # alder
        ["TOT"],  # i alt
        [">=2008K1<=2026K2"],  # fra og med 2008K1 til og med 2026K2
    ],
}

# use the export_data function to export data from each table defined in the packages.
export_data(pkgIndk)
export_data(pkgBefolkning)
