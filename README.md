You need to check to see if students are registered for classes. To make this easier, you need a program that, given a last name, will read in the information from a file. Each record in the file will contain seven pieces of information, separated by spaces, in the following order: the student’s first name, last name, gpa, credit hours, meal plan level, advisor, and whether they have submitted the forms for enrollment (“True” or “False”). Download the following file and add them to your Project 5 program folder: studentInfo.txt Download studentInfo.txt

Your Task:
Your instructor is very particular regarding how this assignment will be completed so you must follow the guidelines listed below exactly.

You will need to define eight functions with the following criteria:
•    A function named fileReader() which has 2 parameters: lastName, which is the last name of the student, and fileInput, which is the file variable created in the main part of the program. The function should return the student information or “Student not found"
•    A function named firstName() that has one parameter, studentInfo, and returns the first name of the student.
•    A function named lastName() that has one parameter, studentInfo, and returns the last name of the student.
•    A function named gpa() that has one parameter, studentInfo, and returns the gpa of the student.
•    A function named creditHours() that has one parameter, studentInfo, and returns the number of credit hours of the student.
•    A function named mealPlan() that has one parameter, studentInfo, and returns the meal plan level of the student.
•    A function named advisor() that has one parameter, studentInfo, and returns the advisor assigned to the student.
•    A function named enrollmentSubmit() that has one parameter, studentInfo. This function should read “True” or “False” from the enrollment (last) column of the student’s record. If the line reads True, the function returns “[lastName] has enrolled”. If the line reads False, the function returns “[lastName] has not enrolled”..

 Program Documentation:

Use the project header as specified in the Style Guidelines on Northwest Online.
Use good programming style.
For example, use blank lines to separate major sections of code.
Use comments to indicate the major steps in your program algorithm.
Use back slash ( \ ) character if the statement continues onto the next line and is lengthy
Do not add any features to the program that you turn in. Do not include Python statements that we have not studied at this point in the course.
