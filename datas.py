
utilisateurs = [
    {'nom': 'Alice','code': 'AbC123','amount':100000},
    
]

# Accéder au nom du premier utilisateur


# Parcourir la liste et afficher chaque utilisateur
for utilisateur in utilisateurs:
    print(f"{utilisateur['nom']} a {utilisateur['amount']} euro dans son compte bancaire")




import statistics

class Statistiques:
    def __init__(self, donnees):
        if not donnees:
            raise ValueError("La liste de données ne peut pas être vide.")
        self.donnees = donnees

    def moyenne(self):
        return statistics.mean(self.donnees)

    def mediane(self):
        return statistics.median(self.donnees)

    def variance(self):
        return statistics.variance(self.donnees)

    def ecart_type(self):
        return statistics.stdev(self.donnees)

    def mode(self):
        try:
            return statistics.mode(self.donnees)
        except statistics.StatisticsError:
            return "Pas de mode unique"

# Exemple d'utilisation
if __name__ == "__main__":
    donnees = [4, 8, 6, 5, 3, 8, 9]
    stats = Statistiques(donnees)

    print("Données :", donnees)
    print("Moyenne :", stats.moyenne())
    print("Médiane :", stats.mediane())
    print("Variance :", stats.variance())
    print("Écart-type :", stats.ecart_type())
    print("Mode :", stats.mode())




import math

class PopulationEstimator:
    def __init__(self, initial_population, birth_rate, death_rate, net_migration_rate):
        """
        :param initial_population: int, population de départ
        :param birth_rate: float, taux de natalité annuel (ex. 0.025 pour 2.5%)
        :param death_rate: float, taux de mortalité annuel (ex. 0.01 pour 1%)
        :param net_migration_rate: float, taux de migration nette annuel (ex. 0.005 pour 0.5%)
        """
        self.initial_population = initial_population
        self.birth_rate = birth_rate
        self.death_rate = death_rate
        self.net_migration_rate = net_migration_rate

    def estimate_population(self, years):
        """
        Estime la population après un certain nombre d'années.
        """
        population = self.initial_population
        for year in range(years):
            growth_rate = self.birth_rate - self.death_rate + self.net_migration_rate
            population += population * growth_rate
        return int(population)

    def yearly_projection(self, years):
        """
        Retourne la population estimée pour chaque année jusqu'à la durée spécifiée.
        """
        population = self.initial_population
        projections = []
        for year in range(1, years + 1):
            growth_rate = self.birth_rate - self.death_rate + self.net_migration_rate
            population += population * growth_rate
            projections.append((year, int(population)))
        return projections


# Exemple d'utilisation
if __name__ == "__main__":
    # Paramètres : population initiale, taux de natalité, taux de mortalité, taux de migration
    estimator = PopulationEstimator(
        initial_population=1000000,
        birth_rate=0.025,  # 2.5%
        death_rate=0.01,   # 1%
        net_migration_rate=0.002  # 0.2%
    )

    print("Estimation de la population dans 10 ans :")
    print(estimator.estimate_population(10))

    print("\nProjection annuelle pour les 10 prochaines années :")
    for year, pop in estimator.yearly_projection(10):
        print(f"Année {year} : {pop} habitants")
