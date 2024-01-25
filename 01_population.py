from data import populations, relationships

# Modifiez la liste populations pour ajouter les relations (liste relationships) de chaque user de cette population, vous pouvez par exemple ajoutez une clé "relation" ainsi qu'une liste vide dans un premier temps. Puis placez les relations de chaque user dans la liste populations en utilisant relationships.

def addRelations():
    for user in populations:
        user["relation"] = []

        for relation in relationships:
            if relation[0] == user["id"]:
                user["relation"].append(relation[1])
                
            elif relation[1] == user["id"]:
                user["relation"].append(relation[0])
    print(populations)

# Calculer la moyenne des relations.

def averageRelations():
    average = sum(list(map(lambda pop : len(pop["relation"]), populations))) / len(populations)
    print('Exercice 2 output: ', average)
 

# Créez une liste représentant les users (id) et le nombre de relation(s) qu'ils possèdent. Et retournez l'utilisateur qui possède le plus de relation(s).

def mostRelations():
    usersWithRelations = []
    highest = 0
    for user in populations:
        usersWithRelations.append({"userId": user["id"], "relationsNumber": len(user["relation"])})
        if len(user["relation"]) > highest:
            highest = len(user["relation"])
            userWithMostRelations = user["name"]
    print('Exercice 3 output: The user with the most relations is', userWithMostRelations)

# Trouvez les amis des amis de chaque utilisateur.

def friendsOfFriends():
    for user in populations:
        user["friendsOfFriends"] = []

        for relation in user["relation"]:
            for friend in populations[relation]["relation"]:
                if friend not in user["friendsOfFriends"] and friend != user["id"]:
                    user["friendsOfFriends"].append(friend)
    print('Exercice 4 output: ', populations)

addRelations()
averageRelations()
mostRelations()
friendsOfFriends()