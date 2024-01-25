from data import students, levels

def zipLevel():
    for student, level in zip(students, levels):
        print(f"Student : {student}, Level : {level}")

zipLevel()