from data import students, levels

# Soit les deux listes suivantes : students et levels ces deux listes sont de même longueur et correspondent respectivement aux noms des étudiants et à leur niveau d'étude, à l'aide de la fonction zip et d'une itération affichez le nom et le niveau de chaque étudiant.

def zipLevel():
    for student, level in zip(students, levels):
        print(f"Student : {student}, Level : {level}")

zipLevel()