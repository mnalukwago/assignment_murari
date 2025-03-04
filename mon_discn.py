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
    print(f"the final mark is {final_mark}")

student_details()
    