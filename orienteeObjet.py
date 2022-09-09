# orienté objet: 
# les classe,definit a quoi notre objet doit ressembler,on va attribuer a chaque classe des attributs
# on peut faire des fonction qui vont permettre d'agir sur les instances
# POO permet d'ameliorer et organiser le code et eviter les repetitions

# EXEMPLE:
class Voiture:
     marque = "Lamborghini"
     couleur = "rouge"

print(Voiture.marque)
print(Voiture.couleur)

# CREER DES INSTANCES DES CLASSES, on part a partir des classes
class Voiture:
     marque = "Lamborghini"

voiture_01 = Voiture()
voiture_02 = Voiture()
print(voiture_01.marque)

# INSTANCE QUI PARTE DE LA MEME MARQUE MAIS QU4ON PEUT MODIFIER APRES
# ATTRIBUT DE CLASSE ET D'INSTANCE

Voiture.marque = "Porsche" # modifie toutes les instances

print(voiture_01.marque)
print(voiture_02.marque)

#modifier chaque instance differement
voiture_01.marque = "Peugeot"
voiture_02.marque = "Volkswagen"

print(voiture_01.marque)
print(voiture_02.marque)

voiture_01.marque = "Peugeot"

# INITIALISER UNE INSTANCE
# METHODE INIT
class Voiture:
     marque = "Lamborghini"
     def __init__(self, marque): #self correspond a notre instance
          self.marque = marque # definir une marque qui va etre different de chaque voiture

voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porsche" )
print(voiture_01.marque)
print(voiture_02.marque)

# EXEMPLE 2
class Voiture:
     voitures_creer = 0
     def __init__(self, marque): #self correspond a notre instance
          Voiture.voitures_creer += 1
          self.marque = marque # definir une marque qui va etre different de chaque voiture

voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porsche" )
print(voiture_01.marque)
print(voiture_02.marque)

# LA SIGNIFICATION DE SELF
class Voiture:
     def __init__(self, marque): 
          self.marque = marque

     def afficher_marque(self):
          print(f"la voiture est une {self.marque}")

voiture_01 = Voiture("Lamborghini")
voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_01)

# classe  
class Voiture: 
     #attribut de classe
     pneus = 4 # qui appartient a la classe Voiture
     #methode
     def __init__(self,marque): # comme une fonction
          #attributs d'instance
          self.marque = marque # self fait reference a notre instance
          #instance
lamborghini = Voiture("Lamborghini") # definit a partir de la classe Voiture






