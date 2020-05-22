import pandas as pd
import pubchempy as pcp

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
        return cpd_id[0]
    except:
        return ""

def main():
    #Read in drugbank csv, return cas_ids
    cas_ids, names = get_info("drugs/opioids_filtered.csv")

    #Find all pubchem ids of opioids
    opiods_pubchem_ids = []
    for name in names:
        opiods_pubchem_ids.append(get_pubchem_id(name))

    #Print all ids to a file
    for id in opiods_pubchem_ids:
        print(id, file=open("drugs/opioid_pubchem_ids.txt", "a"))

if __name__ == "__main__":
    main()
