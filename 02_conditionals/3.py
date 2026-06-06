score = 130

if score>=100:
    print("Recheck your score")
    exit()
if score>=90:
    grade ="A"
elif score>=80:
    grade="B"
else:
    grade="F"

print("Your Grade is", grade)