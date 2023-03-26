from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import mysql.connector

@csrf_exempt
def get_course_data(request):
    if request.method == 'POST':
        # Get the selected career and course from the POST data
        career = request.POST.getlist('career')
        course = request.POST.get('course')
        
        # Connect to the MySQL database
        cnx = mysql.connector.connect(user='admin', 
                              password='`cxH2lf;bxDPF3|s',
                              host='34.174.152.9',
                              database='main')

        # Prepare the SQL query to retrieve the course data
        cursor = cnx.cursor()
        query = "SELECT * FROM courses WHERE career IN {} AND course_name = %s".format(tuple(career))
        cursor.execute(query, (course,))
        rows = cursor.fetchall()
        
        # Convert the query results to a JSON object
        course_data = []
        for row in rows:
            course_data.append({
                'id': row[0],
                'course_name': row[1],
                'career': row[2],
                'description': row[3]
            })
        
        # Close the database connection
        cursor.close()
        cnx.close()
        
        # Return the course data as a JSON response
        return JsonResponse(course_data, safe=False)
