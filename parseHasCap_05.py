# Créez une classe Parse, soit la chaîne de caractères suivantes, utilisez les fonctions strip() et split() pour retournez une structure comportant uniquement des numériques, vous testerez votre méthode sur la chaîne suivante :

class Parser:
    def __init__(self, delimiter, input_string):
        self.delimiter = delimiter
        self.input_string = input_string

    def parse_numbers(self):
        result = [int(token.strip()) for token in self.input_string.split(self.delimiter) if token.strip().isnumeric()]
        return result

    def __str__(self):
        return ' '.join(map(str, self.parse_numbers()))

phrase = '8790: bonjour le monde:8987:7777:Hello World:    9007'
p = Parser(':', phrase)
print(p)

# Ecrire une classe HasCap qui lorsqu'on renvoie tous les mots/particules d'un texte t commençant par une majuscule dans un dictionnaire en comptant le nombre d'occurence de ces mots/particules.

class HasCap():
  def __init__(self, phrase):
    self.phrase = phrase
    self.cap_words_count = {}

  def parse(self):
    words = self.phrase.split()
    for word in words:
      if word[0].isupper():
        clean_word = word.strip('.,!?"\'')

        if clean_word in self.cap_words_count:
          self.cap_words_count[clean_word] += 1
        else:
          self.cap_words_count[clean_word] = 1

    return self.cap_words_count

phrase = "Le langage Python est placé sous une licence libre proche de la licence BSD6 et fonctionne sur la plupart des plates-formes informatiques, des smartphones aux ordinateurs centraux7, de Windows à Unix avec notamment GNU/Linux en passant par macOS, ou encore Android, iOS, et peut aussi être traduit en Java ou .NET. Il est conçu pour optimiser la productivité des programmeurs en offrant des outils de haut niveau et une syntaxe simple à utiliser."
hasCap = HasCap(phrase)
h = hasCap.parse()
print(h)