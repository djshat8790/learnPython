student_height = input().split()

height = 0
count = 0
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

for h in student_height:
    height += h
    count += 1

print(f"Total height : {height}")
print(f"Number of students : {count}")

average_height = round(height / count, 2)

print(f"average_height : {average_height}\n")
