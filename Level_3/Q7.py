# Using a for loop
def create_dict_with_for_loop(students, subjects):
    student_subject_dict = {}
    for i in range(len(students)):
        student_subject_dict[students[i]] = subjects[i]
    return student_subject_dict

if __name__ == "__main__":
    # Input lists
    students = ["Sam", "Alice", "Mona"]
    subjects = ["Commerce", "Science", "Computer"]
    dict_with_for_loop = create_dict_with_for_loop(students, subjects)
    print("Dictionary using for loop:")
    print(dict_with_for_loop)


