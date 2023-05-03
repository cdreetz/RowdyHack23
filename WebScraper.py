import json
from Bot import Bot
from selenium.webdriver.common.by import By
from time import sleep
import itertools
import urllib
from selenium.common.exceptions import NoSuchElementException
from random import shuffle
import mysql.connector
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi



class StackScraper(Bot):
    def __init__(self, headless=False, verbose=False):
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
            "amazon"
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
        sleep(0.5)
        for idx, listing in enumerate(listings):
            self.scroll_into_view(listing)
            # print(id)
            listing.click()
            # print("click listing")
            sleep(0.5)
            try:
                job = self._get_job()
            except:
                continue
            self.save_job(job, role_name, company)

    def scroll_into_view(self, element):
        try:
            self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
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
            By.XPATH, './/div[@class="nJlQNd sMzDkb"]').text
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
        return description
    

    def save_job(self, job, role_name, company):
        print(job.keys()) # check the keys in job dictionary
        if self.verbose:
            print(f'Saving {role_name} job at {company}')
        try:
            # Set up MongoDB connection
            uri = "mongodb+srv://cdreetz:Xue5CboEBAW1UIim@cluster0.hxuskkk.mongodb.net/?retryWrites=true&w=majority"
            # Create a new client and connect to the server
            client = MongoClient(uri, tlsCAFile=certifi.where())
           
            db = client['Cluster0']
            jobs_collection = db['jobs']
            print(f"Connected to MongoDB server")

            # Check if job already exists in collection
            if self.verbose:
                print(f"Checking if job ID {job['id']} already exists...")
            count = jobs_collection.count_documents({'id': job['id']})
            if count > 0:
                if self.verbose:
                    print(f"Job ID {job['id']} already exists")
                return

            # Insert job into collection
            if self.verbose:
                print(f"Inserting job ID {job['id']} into collection {jobs_collection}...")
            jobs_collection.insert_one({'id': job['id'], 'role': role_name, 'company': company, 'description': job['description']})
            if self.verbose:
                print(f"Job ID {job['id']} inserted into collection {jobs_collection}.")
        except Exception as e:
            print(f"Error saving job ID {job['id']}: {str(e)}")
        finally:
            client.close()






if __name__ == '__main__':
    StackScraper()