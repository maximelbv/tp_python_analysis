# Pour vos résultats de la partie 1 et 2.
# Creez un model ( une classe ) pour enregistrer les données nettoyées, que vous allez enregistrer dans une table ou un ficher.
# Visualisez les données en console, par exemple, pour vérifier qu'elles sont correctectement importées

import populations_01
import levels_02

population = populations_01.friendsOfFriends()
zipList = levels_02.zipLevel()

class User :
  def __init__(self,name, id=None, relation=[], friendsOfFriend=set(), level=None):
    self.id = id
    self.name = name
    self.relation = relation
    self.friendsOfFriend = friendsOfFriend
    self.level = level

  def __iter__(self):
    return self
  def __next__(self):
    return self

users = list(map(lambda user: User(**user).__dict__ ,population))

for student in zipList:
  index = next((i for (i, u) in enumerate(users) if u["name"] == student[0]), None)
  if index is not None:
    users[index]["level"] = student[1]
  else:
    users.append(User(name=student[0], level=student[1]).__dict__)

for u in users:
  print(u)