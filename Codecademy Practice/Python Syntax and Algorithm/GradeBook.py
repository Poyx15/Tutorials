last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ['physics', 'calculus', 'poetry', 'history']

grades = [98, 97, 85, 88]

subjects.append('Computer Science')
grades.append(100)

gradebook = list(zip(subjects, grades))

print(gradebook)

full_gradebook = last_semester_gradebook + gradebook

print(list(full_gradebook))