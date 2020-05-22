##NOTES
#Collects 20 pubmed citations, given a pubchem id

import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.ncbi.nlm.nih.gov/pubmed?linkname=pccompound_pubmed_mesh&from_uid=971"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #find all div classes of "rprtnum nohighlight"
    id_wrapper = soup.find_all(class_="rprtnum nohighlight")
    #find all PubMed ids of papers associated with a specific compound

    pubmed_ids = []
    for id in id_wrapper:
        pubmed_ids.append(id.input["value"])

    print(pubmed_ids)

if __name__ == "__main__":
    main()
