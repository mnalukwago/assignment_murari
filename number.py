#number = int(input("the number of entries.\n"))
#dict = {input("enter key.\n"): input("enter value.\n") for _ in range(number)}
#print(dict)

number1 = (int(input("the number of entries.\n"))) # number1 is a global variable(it's outside the function)
def enter_number():
     number2 = number1
     capture =  {input("enter key.\n"): input("enter value.\n") for _ in range(number2)} # capture is a local variable (b'se it's inside a function)
     print(capture) 

enter_number()  
#print(capture)   
#print(enter_number) 

def capture_student_details(name, age, gender, program, faculty, year_of_study, dob, test1_marks, test2_marks, final_exam_marks):
    """
    Captures the details of a student and returns a dictionary.
    """
    student = {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Program": program,
        "Faculty": faculty,
        "Year of Study": year_of_study,
        "Date of Birth": dob,
        "Test 1 Marks": test1_marks,
        "Test 2 Marks": test2_marks,
        "Final Exam Marks": final_exam_marks,
    }
    return student

# Example usage
student_info = capture_student_details(
    name="John Doe",
    age=20,
    gender="Male",
    program="Computer Science",
    faculty="Engineering",
    year_of_study=2,
    dob="2004-05-15",
    test1_marks=85,
    test2_marks=90,
    final_exam_marks=88
)

print(student_info)

