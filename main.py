class DemographicStats:
    def __init__(self, population, births, deaths):
        """
        :param population: int - population moyenne de l'année
        :param births: int - nombre de naissances vivantes durant l'année
        :param deaths: int - nombre de décès durant l'année
        """
        self.population = population
        self.births = births
        self.deaths = deaths

    def birth_rate(self):
        """Calcule le taux de natalité pour 1000 habitants"""
        return (self.births / self.population) * 1000

    def death_rate(self):
        """Calcule le taux de mortalité pour 1000 habitants"""
        return (self.deaths / self.population) * 1000

    def estimate_births_from_rate(self, rate_per_thousand):
        """Estime le nombre de naissances à partir d'un taux de natalité donné (‰)"""
        return int((rate_per_thousand / 1000) * self.population)

    def estimate_deaths_from_rate(self, rate_per_thousand):
        """Estime le nombre de décès à partir d'un taux de mortalité donné (‰)"""
        return int((rate_per_thousand / 1000) * self.population)

    def estimate_future_population(self, years):
        """
        Estime la population après un certain nombre d'années
        en utilisant les taux de natalité et mortalité.
        :param years: int - nombre d'années pour la projection
        :return: float - population estimée
        """
        pop = self.population
        birth_rate_percent = self.birth_rate() / 1000  # taux en décimal
        death_rate_percent = self.death_rate() / 1000  # taux en décimal
        net_growth_rate = birth_rate_percent - death_rate_percent

        for year in range(years):
            pop += pop * net_growth_rate

        return int(pop)

    def summary(self):
        """Affiche un résumé des statistiques démographiques"""
        br = self.birth_rate()
        dr = self.death_rate()
        print(f"Taux de natalité : {br:.2f} pour 1000 habitants")
        print(f"Taux de mortalité : {dr:.2f} pour 1000 habitants")
        print(f"Naissances estimées (selon taux) : {self.estimate_births_from_rate(br)}")
        print(f"Décès estimés (selon taux) : {self.estimate_deaths_from_rate(dr)}")


# --- Exemple d'utilisation ---
if __name__ == "__main__":
    # Données exemple : population, naissances, décès
    stats = DemographicStats(
        population=5000000,
        births=120000,
        deaths=5000
    )

    stats.summary()

    years = 10
    future_population = stats.estimate_future_population(years)
    print(f"\nPopulation estimée dans {years} ans : {future_population} habitants")











#...............CLASS BankAccount ........................

from datas import datas

class BankAccount:
    
    def __init__(self):
        
        self.__name = 'John' 
        self.__amount = 75000
        self.__code = "AbC123"
        self.__data = False
        
    
    #getters method
    def get_name(self):
        return self.__name
    
    def get_code(self):
        return self.__code
    
    def get_amount(self):
        return self.__amount
    
    def get_data(self):
        return self.__data
    
    #setters method
    
    def set_name(self,name):# setters set_name to modify a name
        self.__name = name
    
    def set_amount(self,amount): # setters set_amount to modify a amount
        if type(amount) == int: # we check if amount is int type
            self.__amount = amount
            
    def set_code(self,code):# setters set_code to modify a code
        self.__code = code
        
    def __set_data(self,data): # this setters is private , no access out of class
        if type(data) == bool: # we check if data is bool type
            self.__data = data 
            
    # this method checks if datas matched ,it's private       
    def __check_data(self,name,code):
        
        if self.__name == name and self.__code == code :
            return True
        return False
 
    #  this method is for entreing data : name and code 
    def enter_data(self):
        name = input("Entrez votre Nom : ")
        code = input("Entrez votre code: ")
        return self.__check_data(name,code)
        

    
    #This method display datas after all verification
    def display_data(self,data):
        if data:
            return f" Name : {self.__name} , Balance : {self.__amount}"
        return "ACCES DENIED"
    
    #Add amount    
    def add_amount(self):
        try:
            
            if self.enter_data():
                amount = int(input("Entrez votre montant à déposer: "))
                self.__amount += amount
                
                response = input("Voulez vous consulter votre nouveau solde ? OUI ou NON : ")
                r = response.lower()
                if r == "oui" :
                   return f" Name : {self.__name} , Balance : {self.__amount}"
               
                return f"Merci d'avoir utilisé nos services,vous avez ajouté {amount} euro dans votre compte"
              
                
            else:
                print("ACCES DENIED")
        except Exception as e:
            return "Le montant doit etre un nombre"
            
    # Retire amount      
    def retire_amount(self):
        try:
            
            if self.enter_data():
                amount = int(input("Entrez votre montant à retirer: "))
                self.__amount -= amount
                
                response = input("Voulez vous consulter votre nouveau solde ? OUI ou NON : ")
                r = response.lower()
                if r == "oui" :
                
                    return f" Name : {self.__name} , Balance : {self.__amount}"
                
                return f"Merci d'avoir utilisé nos services,vous avez retiré {amount} euro dans votre compte"
            else:
                print("ACCES DENIED")
        except Exception as e:
            return "Le montant doit etre un nombre"
            
            






#...............CLASS GUICHET ........................
 
 
 
 
 
 
 
          
class Guichet(BankAccount):
    
    def __init__(self):
        super().__init__()
    
    def your_name_and_code(self):
        
       print(" ENTREZ VOS IDENTIFIANTS SVP POUR CONSULTER VOTRE COMPTE, C'EST POUR LA SECURITE CAR C'EST UNE BANQUE ")
       return super().enter_data()
    
    #Faire un depot  
    def deposit(self):
        print("ENTREZ VOS IDENTIFIANTS POUR AJOUTER DE L'ARGENT DANS VOTRE COMPTE")
        return super().add_amount()
        
    #retirer de l'argent
    def withdrawl(self):
        print("ENTREZ VOS IDENTIFIANTS POUR RETIRER DE L'ARGENT DANS VOTRE COMPTE")
        return super().retire_amount()
        



#....................................OBJECTS.......................................

guichet = Guichet()

# data = guichet.your_name_and_code() #le guichet nous demande de faire entrer un identifiant pour la verification

# #Une fois la verification passé , data est passé dans display_data pour afficher le resultat
# print(guichet.display_data(data))

print(guichet.deposit())
#print(guichet.__amount)
# print(guichet.__check_data('John','AbC123'))
# print(guichet.__name)
#print(guichet.get_name())