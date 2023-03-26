const careerDropdown = document.getElementById("career-dropdown");
const courseDropdown = document.getElementById("course-dropdown");
const courseSection = document.getElementById("course-section");
const courseStatsSection = document.getElementById("course-stats-section");
const courseStats = document.getElementById("course-stats");

careerDropdown.addEventListener("change", function() {
	// Clear the course dropdown and course stats
	courseDropdown.innerHTML = '<option value="">Select Course</option>';
	courseStats.innerHTML = '';
	
	// Add courses based on the selected career
	switch (this.value) {
		case "data-analyst":
			addCourse("Data-Driven Decision Making and Design");
			addCourse("Data Analytics Tools and Techniques");
			addCourse("Data Analytics Visualization and Communication");
			addCourse(" Data Analytics Applications");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum II");
			break;
		case "data-scientist":
			addCourse("Linear Algebra");
			addCourse("Foundations of Analysis");
			addCourse("Complex Variables");
			addCourse("Differential Equations I");
			addCourse("Numerical Analysis");
			addCourse("Real Analysis I");
			addCourse("Data Science and AI for All");
			addCourse("Statistical Analysis for Data Science");
			addCourse("Introduction to Data Science");
			addCourse(" Programming for Data Science");
			addCourse("Data Organization and Visualization");
			addCourse("Data Mining and Machine Learning");
			break;
		case "data-engineer":
			addCourse("Data-Driven Decision Making and Design");
			addCourse("Data Analytics Tools and Techniques");
			addCourse("Data Analytics Visualization and Communication");
			addCourse(" Data Analytics Applications");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum I");
			addCourse("Data Analytics Practicum II");
			break;
		case "ml-engineer":
			addCourse("Machine Learning and Data Analytics");
			addCourse("Applied Big Data with Machine Learning");
			addCourse("Machine Learning");
			addCourse("Introduction to Machine Learning");
			addCourse("Data Mining and Machine Learning");
			break;
	}
	
	// Show the course section and hide the course stats section
	courseSection.style.display = "block";
	courseStatsSection.style.display = "none";
});

courseDropdown.addEventListener("change", function() {
	// Show the course stats section and output the stats for the selected course
	
	
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
});


function addCourse(courseName) {
	const option = document.createElement("option");
	option.value = courseName;
	option.text = courseName;
	courseDropdown.add(option);
}

