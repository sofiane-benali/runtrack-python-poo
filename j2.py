# JOB 1
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longeur = longueur
        self.__largeur = largeur

    def getlongeur(self):
        return self.__longeur

    def getlongueur(self, i):
        self.__longeur = i
        return self.__longeur

    def getlargeur(self):
        return self.__largeur

    def setlargeur(self, i):
        self.__largeur = i
        return self.__largeur


boite = Rectangle(20, 30)

print(boite.getlongeur())

boite.setlargeur(300)
print(boite.getlargeur())


# JOB 2
class Livre:
    def __init__(self, titre, auteur, nbdepage,level , disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbdepage = nbdepage
        self.__disponible = disponible
        self.__level = level

    def gettitre(self):
        return self.__titre

    def settitre(self, i):
        self.__titre = i
        return self.__titre

    def getauteur(self):
        return self.__auteur

    def setauteur(self, i):
        self.__auteur = i
        return self.__auteur

    def getnbdepage(self):
        return self.getnbdepage()

    def setnbdepage(self, i):
        self.__nbdepage = i
        if self.__nbdepage <= 0:
            pass
        else:
            return self.__titre

# JOB 3

    def verification(self):
        return self.__disponible

    def emprunter(self):
        if self.verification() == True:
            return self.__disponible == False
        else:
            return "Livre non disponible à l'emprunt"

    def rendre(self):
        if self.verification == False:
            return self.__disponible == True
        else:
            return "Le livre n'a pas été emprunté"



# JOB 4
class Student:
    def __init__(self, nom, prenom, numeroetudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numeroetudiant = numeroetudiant
        self.__nombredecredit = 0
        self.__level = self.__studenteval()

    def add_credits(self,i):
        if i >= 0:
            self.__nombredecredit = i
        else:
            pass
        return self.__nombredecredit

    def showcredits(self):
        return self.__nombredecredit

    def __studenteval(self):
        if self.__nombredecredit >= 90:
            return "Excellent"
        elif self.__nombredecredit >= 80:
            return "Très bien"
        elif self.__nombredecredit >= 70:
            return "Bien"
        elif self.__nombredecredit >= 60:
            return "Passable"
        elif self.__nombredecredit < 60:
            return "Insuffisant"

    def getstudentinfo(self):
        return [f"Nom = {self.__prenom}",f"Pénom = {self.__nom}",f"ID = {self.__numeroetudiant}",f"Niveau = {self.__level}"]


John = Student("John","Doe",145)
John.add_credits(30)
print(f"Le nombre de crédits de John Doe est de {John.showcredits()} points")
print(John.getstudentinfo())


# JOB 5
class Voiture():
    def __init__(self, marque, modele, annee,km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50

    def demarrer(self):
        if self.__en_marche == False and self.__verifier_plein() >= 5:
            return self.__en_marche == True

    def arreter(self):
        if self.__en_marche:
            return self.__en_marche == False

    def __verifier_plein(self):
        return self.__reservoir

voiture = Voiture("peugeot", "208", 2020, 20)
# JOB 6
class Commande:
    def __init__(self, numerodecommande):
        self.__numerodecommande = numerodecommande
        self.__listedeplatscommande = {}
        self.__statutdecommande = "en cours"

    def addplat(self,nom,prix):
        self.__listedeplatscommande[f"{nom}"]=prix
        return self.__listedeplatscommande

    def supprcommande(self):
        return self.__listedeplatscommande.clear()

    def calculertotal(self):
        pass

    def totalpanier(self):
        return self.__listedeplatscommande



commandedusoir = Commande(133)
commandedusoir.addplat("pizza",11)
print(commandedusoir.totalpanier())
