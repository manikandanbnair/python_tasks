
import school_module as sm
unique_id =1
school = sm.School()
def main():
    global unique_id
    while True:
        print("Menu:")
        print(
            "1.Add a student.\n2.Remove a student.\n3.Add grades for a student\n4.Display student details\n5.Display all students.\n6.Display students with grade above a criteria\n7.Exit")

        try:
            choice = int(input("Enter your choice\n"))
            match choice:
                case 1:

                    student_name = input("Enter the student name:\n")
                    student_id = unique_id
                    student = sm.Student(student_id,student_name)
                    sm.AdvancedSchool().add_a_student(student)
                    unique_id = unique_id + 1
                case 2:
                    try:
                        student_id = int(input("Enter the ID of the student to delete:\n"))
                        sm.AdvancedSchool().remove_by_student_id(student_id)
                    except ValueError:
                        print("ID should be of type Integer")

                case 3:
                    try:
                        mark_list = []
                        student_id = int(input("Enter the ID of the student:\n"))
                        student = school.get_by_id(student_id)
                        if student is  None:
                            print(f"Student with ID {student_id} doesn't exist")
                        else:
                            print("Enter grades for the student\n")
                            try:
                                for i in range(0, 5):
                                    mark = int(input())
                                    mark_list.append(mark)
                                student.add_grades(student_id, mark_list)
                            except ValueError:
                                print("Grades should be of type integer")
                    except ValueError:
                        print("ID should be of type Integer")

                case 4:
                    try:
                        student_id = int(input("Enter the ID of the student:\n"))
                        student = school.get_by_id(student_id)
                        if student is None:
                            print(f"Student with ID {student_id} doesn't exist")
                        else:
                            student.student_details()
                    except ValueError:
                        print("ID should be of type Integer\n")
                case 5:
                    student = sm.School().get_all_students()
                    current_student = None
                    while True:
                        choice = int(input("Enter 1 to show next student:\n"))
                        if choice == 1:
                            try:
                                if current_student is None:
                                    current_student = next(student)
                                else:
                                    try:
                                        current_student = next(student)
                                    except StopIteration:
                                        print("No more students to be shown\n")
                                        current_student = None
                                        break
                            except StopIteration:
                                print("No more students to be shown")
                                current_student = None
                        elif choice == 2:
                            break
                        else:
                            print("Invalid option")
                        if current_student is not None:
                            current_student.student_details()
                case 6:
                    grade = int(input("Enter the grade:\n"))
                    sm.AdvancedSchool().list_of_students_with_grade_above(grade)
                case 7:
                    exit(0)
                case _ :
                    print("Invalid option\n")

        except Exception as e:
            print(f"{e}")


if __name__ =="__main__":
    main()