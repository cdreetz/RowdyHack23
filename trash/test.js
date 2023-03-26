// Send a GET request to the Django API endpoint to retrieve the course stats
fetch('/api/course-stats/' + courseDropdown.value)
.then(response => response.json())
.then(data => {
    // Display the course stats data in the 'course-stats' paragraph element
    courseStats.innerHTML = "Score for " + courseDropdown.value + ": "
})
.catch(error => {
    // Handle any errors that occur while fetching the data
    console.error(error);
    courseStats.innerHTML = "Error fetching data.";
})