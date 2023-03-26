# RowdyHack23
Hackathon


# File Descriptions

### Webscraper.py
The web scraper utilized to collect data from the job postings of interest.  Built primarily off of Selenium tools from the driver to scrollIntoView method.  Directed by XPATH's for clicking, scrolling, and recording data.

### Bot.py
This script sets up the settings of the webdriver in which Webscraper.py works within.  Defines some of the methods used in Jobscraper as well.

## Courses.py
Uses BeautifulSoup to parse the html code of the course catalog and create a table of the course names and descriptions

## Flaskapp.py
This is the main file for the flask application so users can interact with the tool, input their selections, and recieve the outputting information

## templates
This folder holds all of the html templates used in Flaskapp.py
