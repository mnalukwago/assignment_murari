"""
def student_details():
    details = {"name": input("student's name.\n"),
               "gender": input("gender.\n"),
               "age": int(input("age: ")),
               "program": input("program.\n"),
               "Date of birth":(input("date of birth.\n")),
               "year of study": int(input("year of study.\n")),
               "faculty": input("faculty.\n"),
               "test1": int(input("test1.\n")),
               "test2": int(input("test2.\n")),
               "exam": int(input("final_mark.\n"))}
    sum = (((details["test1"]) + (details["test2"])) / 2) * 0.4
    exam = (details["exam"]) * 0.6
    final_mark = sum + exam
    print(f"the sum is  {sum}")
    print(f"the exam mark is {exam}")
    print(f"the final mark is {final_mar}k")

student_details()
"""

# method2
def student_detail(students):
    students = []
    num_students = int(input("Enter the number of students: "))
    
    for i in range(num_students):
        print(f"\n enter details for students{i + 1}:")
        name = input("enter student's name:  ")
        age = input("enter student's age:  ")
        gender = input("enter student's gender:  ")
        program = input("enter student's program:  ")
        faculty = input("enter student's faculty:  ")
        year_of_study = input("enter year of study:  ")
        date_of_birth = input("enter student's date of birth:  ")
        test1 = int(input("Enter test1 marks:"))
        test2 = int(input("Enter test2 marks"))
        exam_mark = ((test1 + test2)/2) * 0.4
        final_mark = exam_mark * 0.6 
        print(f"final_grade: {final_mark}")
        course_unit = final_mark + exam_mark
        print(f"course_grade: {course_unit}")

        student = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Pogram": program,
            "Faculty": faculty,
            "Year_of_study": year_of_study,
            "Date_of_birth": date_of_birth,
            "final_grade": final_mark,
            "course_grade": course_unit
        }
# adding student detail to list
        students.append(student) 

        # displaying all students' details

        print("\n list of students")
        for i, student in enumerate(students, start=1):
            print(f"\n student{i }:")     
            for key, value in student.items():
                print(f"{key}: {value}")
student_detail("students")


"""
test1_score = 80
test2_score = 70
finaltest_score = 75

test1_weight = 0.4
test2_weight = 0.4
finaltest_weight = 0.6
final_score = ("test1_score" * "test1_weight") + ("test2_score" * "test2_weight") + ("finaltest_score" * "finaltest_weight")
print(f"Final_score: {final_score:.2f} % ")




"""