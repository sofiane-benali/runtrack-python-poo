# job1
class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    # job2
    def get_number(self):
        return f"Le nombre 1 est: {self.nombre1}, le nombre 2 est: {self.nombre2}"

    # job3
    def addition(self):
        return self.nombre1 + self.nombre2


# job2 = Operation(12, 3)
# print(job2.get_number())

# job3 = Operation(15, 32)
# print(job3.addition())


# job 5
class Personne:
    def __init__(self, nom=None, prenom=None):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Mon nom est: {self.nom} \nMon prénom est: {self.prenom}"


# sofiane = Personne("Ben Ali", "Sofiane")
# print(sofiane.SePresenter())


# job 6
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def afficherpoints(self):
        return self.x, self.y

    def changervaleurpoints(self):
        self.x = input("Insérez la valeur de x")
        self.y = input("Insérez la valeur")
        return self.x, self.y


# affine = Point(1, 3)
# print(affine.afficherpoints())
# affine.changervaleurpoints()


# job 7

class Animal:
    def __init__(self, age=0, nom=None):
        self.age = age
        self.nom = nom

    def viellir(self):
        self.age += 1
        return self.age

    def nommer(self):
        self.nom = input("Quel nom voulez vous donner à votre animal ?")
        return f"L'animal se nomme : {self.nom}"


# job8

class Personnage():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def haut(self):
        self.y += 1
        return self.y

    def bas(self):
        self.y -= 1
        return self.y

    def gauche(self):
        self.x += 1
        return self.x

    def droite(self):
        self.x -= 1
        return self.x

    def position(self):
        return (self.x, self.y)


# guts = Personnage()
# guts.haut()
# guts.gauche()
# print(guts.position())

# job 9

class Cercle:
    def __init__(self, rayon=None):
        self.rayon = rayon

    def changerRayon(self):
        self.rayon = input("Insérez la nouvelle la taille du rayon souhaité :")
        return self.rayon

    def afficherinfos(self):
        return f"Voici les informations de votre cercle: {self.rayon}"

    def circonference(self):
        pass

    def aire(self):
        pass

    def diametre(self):
        pass


# job10

class Produit:
    def __init__(self, nom=None, prixht=0, tva=0.20):
        self.nom = nom
        self.prixht = prixht
        self.tva = tva
    def CalculerPrixTTC(self):
        return self.prixht + self.prixht * self.tva

    def afficher(self):
        return f"Votre produit :{self.nom} Coùte :{self.CalculerPrixTTC()}"

baguette = Produit("Baguette",1)
print(baguette.afficher())

