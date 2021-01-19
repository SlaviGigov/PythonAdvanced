students = {}

for n in range(int(input())):
    name, grade = input().split()
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for k, v in students.items():
    grades = " ".join(map(lambda x: f"{x:.2f}", v))
    print(f"{k} -> {grades} (avg: {sum(v)/(len(v)):.2f})")

# 100/100