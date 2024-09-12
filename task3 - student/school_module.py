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

class Student:

    def __init__(self,student_id,student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.grades = []

    def add_grades(self,student_id,grade):
        if student_id not in School.students_list:
            print(f"Student with ID {student_id} not found.")
        else:
            for grades in grade:
                self.grades.append(int(grades))
        print(self.grades)

    def average_grade(self):
        total = 0
        for ele in self.grades:
            total += int(ele)
        return total/5

    def student_details(self):
        print(f"Student_id: {self.student_id}")
        print(f"Student_name: {self.student_name}")
        print(f"Average_grade: {self.average_grade()}")

class School:
    students_list = {}

    def get_by_id(self,student_id):
        if student_id in self.students_list:
            return self.students_list[student_id]
        else:
            return None

    def add_a_student(self,student):
        self.students_list[student.student_id] = student
        print(self.students_list)


    def remove_by_student_id(self,student_id):
        pass


    def search_for_a_student(self,student_id):
        pass


    def get_all_students(self):
        for student in self.students_list.values():
            yield student

class AdvancedSchool(School):

    def remove_by_student_id(self, student_id):
        if student_id in self.students_list:
            del self.students_list[student_id]
            print(f"Successfully deleted student with ID {student_id} from school.")
        else:
            print(f"Student with ID {student_id} doesn't exist")

    def search_for_a_student(self, student_id):
        if student_id in self.students_list:
            print(f"Student with ID {student_id} found.")
        else:
            print(f"Student with ID {student_id} doesn't exist")

    def list_of_students_with_grade_above(self,grade):
        print(f"List of students with grade greater than {grade}:\n")
        for student in self.students_list.values():
            if student.average_grade() > grade:
                student.student_details()
                print()

