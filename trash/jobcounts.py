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

# Search each job_description for the defined list of phrases
counts = {}
total = 0
roles = {}

cursor.execute("SELECT role, description FROM jobs")
for row in cursor.fetchall():
    total += 1
    found_phrases = set()  # Keep track of which phrases have already been found in the current description
    for phrase in phrases:
        if phrase.lower() == "r":
            if (not row[1][max(0, row[1].find(phrase)-1)].isalpha() if row[1].find(phrase) > 0 else True) and \
               (not row[1][row[1].find(phrase)+1:min(len(row[1]), row[1].find(phrase)+2)].isalpha() if row[1].find(phrase) < len(row[1])-1 else True):
                if phrase not in found_phrases:  # Check if the phrase has already been found in the current description
                    counts[phrase] = counts.get(phrase, 0) + 1
                    found_phrases.add(phrase)
        elif phrase.lower() in row[1].lower():
            if phrase not in found_phrases:  # Check if the phrase has already been found in the current description
                counts[phrase] = counts.get(phrase, 0) + 1
                found_phrases.add(phrase)
    roles[row[0]] = roles.get(row[0], 0) + 1

# Print the ratio of the number of times a word is seen in descriptions over the total number of descriptions
print(f"Total job descriptions counted: {total}")
for role, count in roles.items():
    print(f"Count of {role} jobs: {count}")
print()
for phrase, count in counts.items():
    ratio = count / total if total > 0 else 0
    print(f"{phrase}: {count} ({ratio:.2%})")
