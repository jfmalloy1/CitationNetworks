from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os
import glob
import time

def download_csv(cpd_id):
    #Set up downloading options
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    try:
        url = "https://www.ncbi.nlm.nih.gov/pubmed?LinkName=pccompound_pubmed_mesh&from_uid=" + cpd_id
        driver = webdriver.Chrome("../chromedriver", chrome_options=options)
        driver.get(url)

        #Find the save button - click to open it (may be completely unnecessary)
        file_button = driver.find_element_by_id("save-results-panel-trigger")
        file_button.click()

        #Select the "all" option
        select_selection = Select(driver.find_element_by_id("save-action-selection"))
        select_selection.select_by_index(1)

        #Save file as csv
        select_format = Select(driver.find_element_by_id("save-action-format"))
        select_format.select_by_value("csv")

        #Actually download it
        save_button = driver.find_element_by_xpath("//form[@id='save-action-panel-form']/div[3]/button[1]")
        save_button.click()

        #Need time for ~40k citations - 20 seconds seems appropriate
        time.sleep(20)
    except:
        print(cpd_id + " Failed")

    #Quit chrome
    driver.quit()

def change_filename(cpd_id):
     latest_file = max(glob.glob(os.getcwd() + "/*"), key=os.path.getctime)
     os.rename(latest_file, os.getcwd() + "/" + cpd_id + ".csv")

def main():
    cpd_ids = []
    with open("drugs/opioid_pubchem_ids.txt", "r") as f:
        for line in f:
            if line != "":
                cpd_ids.append(line.strip())

    for id in cpd_ids:
        #Download csv, given PubChem ID
        download_csv(id)

        #Change name of most recently downloaded file to match cpd_id
        change_filename(id)

if __name__ == "__main__":
    main()
