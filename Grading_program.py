student_scores = {
    "Harsh": 89,
    "Krish":75,
    "Pankaj":93,
    "Sumit":70,
    "Umesh":65
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score >90:
        student_grades[student] = "Outstanding"
    elif score >80:
        student_grades[student] = "Excellent"
    elif score >70:
        student_grades[student] = "Critical"
    else:
        student_grades[student] = "Fail"
print(student_grades)