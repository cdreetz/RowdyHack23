import requests
from bs4 import BeautifulSoup
import spacy
# python3 -m spacy download en_core_web_sm

url = "https://catalog.utsa.edu/undergraduate/business/managementsciencestatistics/#courseinventory"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
nonBreakSpace = u'\xa0'
nlp = spacy.load("en_core_web_sm")

# create empty list to store the course names and descriptions
course_list = []

# find all course blocks on the page
for course in soup.find_all('div', {'class': 'courseblock'}):

    # extract the coure name and description and remove whitespace
    course_name = course.find('p', {'class': 'courseblocktitle'}).get_text().strip()
    course_desc = course.find('p', {'class': 'courseblockdesc'}).get_text().strip()

    # process the course name and description
    course_names = nlp(course_name)
    course_descs = nlp(course_desc)

    # add the course name and description to the list as a tuple of spacy doc objects
    course_list.append((course_names, course_descs))


import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(user='admin', 
                              password='`cxH2lf;bxDPF3|s',
                              host='db.cnet.dev',
                              database='main')

# Prepare a SQL INSERT statement to save the course names and descriptions
stmt = "INSERT INTO courses (course_name, course_desc) VALUES (%s, %s)"

# Loop through the list and execute the INSERT statement for each course
for course in course_list:
    values = (course['course_name'], course['course_desc'])
    cursor = cnx.cursor()
    cursor.execute(stmt, values)
    cnx.commit()
    cursor.close()

# Close the database connection
cnx.close()


