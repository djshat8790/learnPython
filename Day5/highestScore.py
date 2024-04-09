student_score = input().split()
max_score = 0
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
    if student_score[n] > max_score:
        max_score = student_score[n]
print(f"The highest score is : {max_score}\n")
