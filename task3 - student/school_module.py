# . Student Class:
# 	Each student has a student_id, name, and a list of grades.
# 	Implement methods to:
# 	 - Add grades for a student.
# 	 - Calculate the average grade.
# 	 - Display student details including their average grade.
#
# 2. School Class:
# 	The School holds a collection of students and allows users to add and remove students.
# 	Implement methods to:
# 	 - Add a student to the school.
# 	 - Remove a student by student_id.
# 	 - Search for a student by student_id.
# 	 - Return an iterator (or generator) that yields each student in the school.
#
# 3. AdvancedSchool Class (inherits from School):
# 	Add a method to find students with an average grade above a given threshold.
# 	Handle exceptions when trying to remove or find a student who doesn’t exist.
#
# 4. Exception Handling:
# 	Raise an exception when attempting to remove or add a student with an invalid student_id.
# 	Handle cases where grades are invalid (e.g., non-numeric or outside the range 0-100).