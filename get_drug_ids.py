import pandas as pd
import pubchempy as pcp
import os
import re
import pandas as pd

#Return the cas number and the name of opioids
def get_info(path):
    df = pd.read_csv(path)
    return list(df["cas_number"]), list(df["name"])

#Returns the pubchem ID of a compound (based on name only)
#Only returns the first cpd_id taken from Pubchem search
def get_pubchem_id(name):
    print(name)
    try:
        cpd_id = pcp.get_cids(name, "name")
        return name, cpd_id[0]
    except:
        return name, ""

#One-time use: remove all non-opioid results
def remove_non_opioids():
    #read in list of pubchem ids
    df = pd.read_csv("drugs/opioid_pubchem_ids.csv", dtype={"Name": "str", "ID":"str"})
    print(len(df))

    drug_files = os.listdir("drugs")

    #find all ids of compounds in Veronica's list
    old_ids = []
    for f in drug_files:
        old_ids.append(str(re.sub(".csv", "", f)))

    # #How many of these compounds are present in the opioid list, but not Veronica's?
    # count = 0
    # found_names = []
    # for item, row in df.iterrows():
    #     if row["ID"] in old_ids:
    #         found_names.append(row["Name"])
    #
    # print(count)
    # print(found_names)
    # print(len(found_names))
    # print("Difference between OG and found list:", list(set(df["Name"]) - set(found_names)))
    # #ANSWER: 4 of them (opium doesn't have a CID, everything else does and has been manually added)

    #Now remove all non-opioids from file
    count = 0
    for oid in old_ids:
        if oid not in df["ID"].values:
            try:
                os.remove("drugs/" + oid+ ".csv")
            except:
                continue

def main():
    # #Opioid names - from Drugbank
    # opioids = ["Tramadol", "Morphine", "Hydromorphone", "Methadone", "Meperidine", "Oxycodone", "Butorphanol"]
    # opioids += ["Dextropropoxyphene", "Pentazocine", "Fentanyl", "Nalbuphine", "Buprenorphine", "Dezocine"]
    # opioids += ["Dextromoramide", "Dihydrocodeine", "Ketobemidone", "Piritramide", "Meptazinol", "Phenazocine"]
    # opioids += ["Tilidine", "Codeine", "Sufentanil", "Alfentanil", "Levorphanol", "Remifentanil", "Hydrocodone"]
    # opioids += ["Diphenoxylate", "Oxymorphone", "Levacetylmethadol", "Methadyl acetate", "Dihydroetorphine", "Diamorphine"]
    # opioids += ["Ethylmorphine", "Etorphine", "Carfentanil", "Alphacetylmethadol", "Dihydromorphine", "DPDPE"]
    # opioids += ["Lofentanil", "Opium", "Normethadone", "Alphaprodine", "Phenoperidine", "Bezitramide", "Tapentadol"]
    # opioids += ["Nicomorphine", "Naltrexone", "Eluxadoline", "Carfentanil, C-11", "Desomorphine", "Benzhydrocodone"]
    # #Read in drugbank csv, return cas_ids
    # cas_ids, names = get_info("drugs/opioids_filtered.csv")
    #
    # #any opioids not in Veronica's list?
    # missing_opioids = list(set(opioids) - set(names))
    # #No - all opioids are present in Veronica's list. Just use the list above.
    #
    # #Find all pubchem ids of opioids
    # opiods_pubchem_ids = []
    # for name in opioids:
    #     opiods_pubchem_ids.append(get_pubchem_id(name))
    #
    # #Print all ids to a file
    # print("Name,ID", file=open("drugs/opioid_pubchem_ids.csv", "w"))
    # for id in opiods_pubchem_ids:
    #     print(str(id[0]) + "," + str(id[1]), file=open("drugs/opioid_pubchem_ids.csv", "a"))

    #ONE TIME USE - remove all non-opioids from directory
    remove_non_opioids()

if __name__ == "__main__":
    main()
