class Ville:
    def __init__(self,nom,nbhabitant):
        self.__nom = nom
        self.__nbhabitant = nbhabitant

    def getname(self):
        return self.__nom

    def getnbhabitant(self):
        return self.__nbhabitant

    def getinfos(self):
        print(f"{self.__nom},{self.__nbhabitant}")
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.ville = ville

    def ajouterpopulation(self):
        self.ville.__nbhabitant += 1


villenulle = Ville("Paris",1_000_000)
villenulle.getinfos()
meilleureville = Ville("Marseille",861635)
meilleureville.getinfos()

j = Personne("John",45,villenulle)
m = Personne("Myrtille",4,villenulle)
c = Personne("Chloé",18,meilleureville)

j.ajouterpopulation()
m.ajouterpopulation()
c.ajouterpopulation()

meilleureville.getinfos()
villenulle.getinfos()

class CompteBancaire:
    def __init__(self, numero_de_compte, nom, prenom, solde):
        self.__numero_de_compte = numero_de_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde

    def afficher(self):
        return f"Nom :{self.__nom}, Prénom : {self.__prenom}, Numéro de compte : {self.__numero_de_compte}"

    def affichersolde(self):
        return self.__solde

    def versement(self,montant):
        montant += self.__solde

    def retrait(self, montant):
        if montant <= self.__solde:
            montant -= self.__solde



        



