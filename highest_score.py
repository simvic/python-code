# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_val = 0
for max_score in student_scores:
    if max_score > max_val:
        max_val = max_score
print(f"The highest score in the class is: {max_val}")

