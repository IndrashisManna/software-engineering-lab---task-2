def validate_marks(marks):
    return 0 <= marks <= 100


def input_marks(subject_count):
    marks_list = []
    for i in range(subject_count):
        while True:
            marks = int(input(f"Enter marks for subject {i+1}: "))
            if validate_marks(marks):
                marks_list.append(marks)
                break
            else:
                print("Invalid marks! Enter between 0 and 100.")
    return marks_list
