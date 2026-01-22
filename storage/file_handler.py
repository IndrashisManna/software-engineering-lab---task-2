def save_result(student, percentage, grade):
    with open("results.csv", "a") as file:
        file.write(f"{student.roll_no},{student.name},{percentage},{grade}\n")
