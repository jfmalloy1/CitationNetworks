import pandas as pd
import math

""" Make a txt file of 1) all DOIs separated by "OR" 2) number of DOIs found """
""" Input: dataframe of PubChem metadata for a specific drug, index of  """
""" Output: a txt file """
def create_search(df, label, i):
    df = df.dropna(subset=["DOI"])

    search_term = ""
    for index, row in df.iterrows():
        if index != len(df):
            search_term += str(row["DOI"]) + " OR "
        else:
            search_term += str(row["DOI"])

    print(search_term, file=open("Searches/" + label + "_search_" + str(i) + ".txt", "w"))

def main():
    #TEST: read in single opioid citation file
    label = "3345"
    df = pd.read_csv("drugs/" + label + ".csv")
    size = len(df)
    print(size)

    #Get the number of different search terms need to be created - 6000 terms is the max WoS can handle
    searches = math.ceil(size/6000)

    for i in range(1, searches+1):
        #Output a text file with all DOIs separated by "OR": do this in groups of 6000 or less
        if size < len(df):
            create_search(df, label, i)
        else:
            print(i)
            create_search(df[1*i:6000*i], label, i)


if __name__ == "__main__":
    main()
