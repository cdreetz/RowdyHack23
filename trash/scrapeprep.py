import json
from Bot import Bot
from selenium.webdriver.common.by import By
from time import sleep
import itertools
import urllib
from selenium.common.exceptions import NoSuchElementException
import os
from random import shuffle


class StackScraper(Bot):
    def __init__(self):
        super().__init__(verbose=True)

        role_names = [
            "data scientist",
            "data analyst",
            "data engineer",
            "machine learning engineer"
        ]
        companies = [
            "apple",
            "google",
            "microsoft",
            "facebook",
            "tesla",
            "amazon",
            "UT Health Science Center at San Antonio",
            #"HEB"
        ]
        shuffle(role_names)
        self.driver.get("https://www.google.com")
        for role_name, company in itertools.product(role_names, companies):
            self.get_all_jobs(role_name, company)

    def get_all_jobs(self, role_name, company):
        query = f"https://www.google.com/search?q={role_name} {company}&ibp=htl;jobs#htivrt=jobs".replace(
            ' ', '+')
        print(query)
        self.driver.get(query)
        listings = self.driver.find_elements(
            By.XPATH, "//div[@class='PwjeAc']")
        print(f"Number of listings found: {len(listings)}")
        sleep(1)
        for idx, listing in enumerate(listings):
            self.scroll_into_view(listing)
            # id = listing.find_element(By.XPATH, '..').get_attribute("data-ved")
            # print(id)
            listing.click()
            # print("Click listing")
            sleep(0.5)
            try:
                job = self._get_job()
            except:
                continue
            self.save_job(job, role_name, company)

    def scroll_into_view(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except Exception as e:
            print(f"Error while scrolling to element: {e}")
                
        
    def _get_job(self):
        return {
            "id": self._get_job_id(),
            "company": self._get_company(),
            "description": self._get_job_description()
        }
    
    def _get_job_id(self):
        parsed_url = urllib.parse.urlparse(self.driver.current_url)
        id = urllib.parse.parse_qs(parsed_url.fragment)['htidocid'][0]
        return id
    
    def _get_company(self):
        job_container = self.driver.find_element(
            By.XPATH, '//div[@class="whazf bD1FPe"]') 
        company = job_container.find_element(
            By.XPATH, './/div[@class="nJlQNd sMzDkb"]'
            ).text
        return company
    
    def _get_job_description(self):
        job_container = self.driver.find_element(
            By.XPATH, '//div[@class="whazf bD1FPe"]')
        try:
            expand_description_button = job_container.find_element(
                By.XPATH, 'div/div/div/div/div/div/div[@class="CdXzFe j4kHIf"]')
            self.scroll_into_view(expand_description_button)
            expand_description_button.click()
        except NoSuchElementException:
            pass
        description = job_container.find_element(
            By.XPATH, ".//span[@class='HBvzbc']").text
        # By.XPATH "div/div/div/div/div/span[@class=']".text
        return description
    
    def save_job(self, job, role_name, company):
        print(job.keys()) # check the keys in job dictionary
        if self.verbose:
            print(f'Saving {role_name} job at {company}')
        folder_path = os.path.join("raw_data", role_name.replace(
            " ", "-"), company.replace(" ", "-"))
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, job["id"])
        if os.path.exists(file_path):
            if self.verbose:
                print(f"Job ID {job['id']} already exists")
            return
        with open(file_path, 'w') as f:
            json.dump(job, f, indent=4)


if __name__ == '__main__':
    StackScraper()
        

        
    

        