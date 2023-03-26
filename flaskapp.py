from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the selected career and course from the form data
        selected_career = request.form.get('career')
        selected_course = request.form.get('course')

        # Query the database to get the roles for the selected career
        query = f"SELECT role FROM jobs WHERE role = '{selected_career}'"
        cursor.execute(query)
        roles = [row[0] for row in cursor.fetchall()]

        # Query the database to get the course description for the selected course
        query = f"SELECT course_desc FROM courses WHERE course_name = '{selected_course}'"
        cursor.execute(query)
        course_desc = cursor.fetchone()[0]

        # Define a list of phrases to search for
        phrases = ["Excel", "SQL", "R", "Python", "Java", "SAS", "TensorFlow", "Algorithms", "Data Mining", "Deep Learning", "Time Series", "Survival Analysis"]

        # Count the number of job descriptions that contain each phrase
        query = "SELECT role, description FROM jobs"
        cursor.execute(query)
        total = 0
        counts = {}
        roles_counts = {}
        for row in cursor.fetchall():
            if row[0] in roles:
                total += 1
                for phrase in phrases:
                    if phrase.lower() == "r":
                        if (not row[1][max(0, row[1].find(phrase)-1)].isalpha() if row[1].find(phrase) > 0 else True) and \
                           (not row[1][row[1].find(phrase)+1:min(len(row[1]), row[1].find(phrase)+2)].isalpha() if row[1].find(phrase) < len(row[1])-1 else True):
                            counts[phrase] = counts.get(phrase, 0) + 1
                    elif phrase.lower() in row[1].lower():
                        counts[phrase] = counts.get(phrase, 0) + 1
                roles_counts[row[0]] = roles_counts.get(row[0], 0) + 1

        # Calculate the ratio of the number of times each phrase is seen over the total number of job descriptions
        phrase_ratios = {phrase: count / total if total > 0 else 0 for phrase, count in counts.items()}

        # Render the template with the selected course, phrase ratios, and roles counts
        return render_template('output.html', selected_course=selected_course, course_desc=course_desc, phrase_ratios=phrase_ratios, roles_counts=roles_counts)
    else:
        # Get the list of available course names from the database
        cursor.execute("SELECT course_name FROM courses")
        course_names = [row[0] for row in cursor.fetchall()]

        # Render the template with the list of available course names and job careers
        return render_template('input.html', course_names=course_names)

if __name__ == '__main__':
    app.run(debug=True)