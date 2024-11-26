student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

maxScore = 0
minScore = 99999
for score in student_scores:
    if score > maxScore:
        maxScore = score

for score in student_scores:
    if score < minScore:
        minScore = score

print(f"The max value is {maxScore}\nMinimum value is {minScore}" )
