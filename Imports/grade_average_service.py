def calculate_homework(homework_assignments):
    sum_of_grades = 0
    for homework in homework_assignments.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades / len(homework_assignments), 2)
    print(final_grade)