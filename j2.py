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
    def __init__(self, titre, auteur, nbdepage, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbdepage = nbdepage
        self.__disponible = disponible

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



