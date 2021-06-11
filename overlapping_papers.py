import pandas as pd
import os
import tqdm as tqdm

""" Checks all downloaded papers (besides self) for overlaps
    Input: dataframe of a specific drug, filename (to prevent overlapping)
    Output: overlapping papers
"""
def check_all_papers(df0, f0, id_link_df):
    pmids = df0["PMID"].tolist() #pubmed ids of the drug to be checked

    overlapping_papers_dict = {} #dictionary to see overlap
    for f in os.listdir("drugs/"):
        if f[0].isdigit() and f != f0:
            #Name of the drug currently being checked against
            drug_name = id_link_df[id_link_df["ID"] == int(f[:-4])]["Name"].item()
            df = pd.read_csv("drugs/" + f)
            if "PMID" in df.columns: #make sure the drug has papers associated with it
                for id in pmids: #for each paper id in the drug to be checked...
                    if id in df["PMID"]: #If it is found in the drug to be checked against add to a dictionary!
                        if drug_name not in overlapping_papers_dict.keys():
                            #start a new index if needed
                            overlapping_papers_dict[drug_name] = 1
                        else:
                            #Otherwise add one to an existing index
                            overlapping_papers_dict[drug_name] += 1


    print(id_link_df[id_link_df["ID"] == int(f0[:-4])]["Name"].item())
    print(len(df0))
    print(overlapping_papers_dict)
    print()

def main():
    id_link_df = pd.read_csv("drugs/opioid_pubchem_ids.csv")
    id_link_df = id_link_df.dropna()

    # test_df = pd.read_csv("drugs/41049.csv")
    # check_all_papers(test_df, "41049.csv")

    for f in os.listdir("drugs/"):
        if f[0].isdigit():
            df = pd.read_csv("drugs/" + f)
            check_all_papers(df, f, id_link_df)


if __name__ == "__main__":
    main()
