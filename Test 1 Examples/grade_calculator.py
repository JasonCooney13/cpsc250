# Get the student type
student_type = input()
if student_type not in ("UG", "G", "DL"):
    print("Error: student status must be UG, G or DL")
else:
    # Get the student grades
    student_grades = [float(x) for x in input().split()]

    # Define the total points in each category, and the weights for each student type
    total_points = (800, 400, 150, 200)
    ug_weights = (0.20, 0.20, 0.30, 0.30)
    g_weights = (0.15, 0.05, 0.35, 0.45)
    dl_weights = (0.05, 0.05, 0.40, 0.50)

    # Calculate the percentages in each category
    student_percentages = []
    for i in range(len(student_grades)):
        student_percentages.append(min(100.0*student_grades[i]/total_points[i], 100.0))

    # Calculate the overall grade
    final_grade = 0.0
    for i in range(len(student_grades)):
        if student_type == 'UG':
            final_grade += student_percentages[i] * ug_weights[i]
        elif student_type == "G":
            final_grade += student_percentages[i] * g_weights[i]
        else:
            final_grade += student_percentages[i] * dl_weights[i]

    # Calculate the letter grade
    # Step 4: Calculate and print letter grade
    if final_grade >= 90:
        letter = 'A'
    elif final_grade >= 80:
        letter = 'B'
    elif final_grade >= 70:
        letter = 'C'
    elif final_grade >= 60:
        letter = 'D'
    else:
        letter = 'F'

    # Create the output report
    category_names = ('Homework', 'Quizzes', 'Midterm', 'Final Exam')
    for i in range(len(student_grades)):
        print(f"{category_names[i]}: {student_percentages[i]:.1f}%")
    print(f"{student_type} average: {final_grade:.1f}%")
    print(f"Course grade: {letter}")
