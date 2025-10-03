students = ["Abraham", "Alejandra", "Santiago", "Diego", "Maite", "Bruno"]
averages = [85, 40, 72, 90, 55, 100]
overall_average = sum(averages) / len(averages)
print(f"Overall class average: {overall_average:.2f}")
passing_grade = 60
passed_students = [grade for grade in averages if grade >= passing_grade]
percentage_passed = (len(passed_students) / len(averages)) * 100
print(f"Percentage of students who passed: {percentage_passed:.2f}%")
failed_students = [name for name, grade in zip(students, averages) if grade < passing_grade]
print("Students who failed:", failed_students)
