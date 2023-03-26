import mysql.connector

phrases = ["Excel", "SQL", "R", "python", "java", "SAS", "TensorFlow", "algorithms", "data mining", "deep learning", "time series", "survival analysis", "business"]

# Set up MySQL server connection
host = '34.174.152.9'
database = 'main'
user = 'admin'
password = '`cxH2lf;bxDPF3|s'
cnxn = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cursor = cnxn.cursor()

# Get the total number of courses
cursor.execute("SELECT COUNT(*) FROM courses")
num_courses = cursor.fetchone()[0]

# Search the first course description for the defined list of phrases
results = {}

cursor.execute("SELECT course_desc FROM courses LIMIT 1")
row = cursor.fetchone()
desc = row[0]
phrase_bools = [phrase.lower() in desc.lower() for phrase in phrases]
results[desc] = phrase_bools

# Print the number of courses and the results for the first row
print(f"Total number of courses: {num_courses}")
print(f"Results for course description: {desc}")
print(phrase_bools)
