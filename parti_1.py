# Creation d'une classe
class Voiture:
    marque = "Lamborghini"
    couleur = "rouge"
    
print(Voiture.marque)
print(Voiture.couleur)


#Creation des instances d'une classe
voiture_01 = Voiture()
voiture_02 = Voiture()
print("instance 1 :", voiture_01.marque)
print("instance 2 :", voiture_02.marque)


#Creation d'attributs de classe et d'instance
Voiture.marque = "Porche"

print("instance 1 :", voiture_01.marque)
print("instance 2 :", voiture_02.marque)

voiture_01.marque = "Volvo"
voiture_02.marque = "Reault"

print(Voiture.marque)
print("instance 1 :", voiture_01.marque)
print("instance 2 :", voiture_02.marque)


# Initialisation d'une instance
class Fruit:
    fruits_achetés = 0
    def __init__(self, nom):
        Fruit.fruits_achetés += 1
        self.nom = nom
        
fruit_01 = Fruit("Pomme")
fruit_02 = Fruit("Orange")
print("nbre de fruit achetés :", Fruit.fruits_achetés)
print("fruit : ", fruit_01.nom )
print("fruit : ", fruit_02.nom )


# La signification de self
class Fruit:
    fruits_achetés = 0
    def __init__(self, nom):
        Fruit.fruits_achetés += 1
        self.nom = nom
        
    def afficher_fruits(self):
        print(f"Les fruits sont : {self.nom}")
    
    
        
fruit_01 = Fruit("Pomme")
fruit_02 = Fruit("Orange")
print("nbre de fruit achetés :", Fruit.fruits_achetés)
print("fruit : ", fruit_01.nom )
print("fruit : ", fruit_02.nom )
fruit_02.afficher_fruits()
