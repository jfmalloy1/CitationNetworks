from selenium import webdriver
from selenium.webdriver.support.ui import Select
import os
import re
from webdriver_manager.chrome import ChromeDriverManager
import json

""" Get list of filenames associated with PubMed opioid references """
""" Input: filepath to list of opioid csv files """
""" Output: list of opioid metadata filenames """
def get_opioid_filenames(fp):
    files = os.listdir(fp)
    filenames = []
    for f in files:
        if (re.match("^[0-9]", f)):
            filenames.append(f)

    return filenames

""" Test crossref API scraping on a random DOI """
def test_crossref(doi):
    url = "https://api.crossref.org/works/" + doi
    print(url)

    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)
        #print(doi, "succeeded")
        source = driver.page_source
        source = re.sub("<html><head></head><body><pre style=\"word-wrap: break-word; white-space: pre-wrap;\">", "", source)
        source = re.sub("</pre></body></html>", "", source)
        metadata = json.loads(source)
        print(metadata)
        #TODO: "is-referenced-by-count" is citation count (within Crossref)
    except:
        print(doi, "failed")

    driver.quit()

""" Goal - download relevant metadate from crossref, given DOI """
def main():
    #Get all csv files associated with opioid drugs
    opioid_files = get_opioid_filenames("drugs/")
    print(opioid_files)

    #TEST CROSSREF SCRAPE
    test_crossref("10.1016/j.forsciint.2019.110137")


if __name__ == "__main__":
    main()
