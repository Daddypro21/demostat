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

    #estimation de la population dans un futur proche(2ans ou plus) d'apres les données exacte
    #données : nbre de decès ,de naissance et l'immigration
    def estimate_population(self, years):
        population = self.initial_population
        for year in range(years):
            growth_rate = self.birth_rate - self.death_rate + self.net_migration_rate
            population += population * growth_rate
        return int(population)

    #estimation de la population en listant toutes les années dans un futur proche(2ans ou plus) d'apres les données exacte
    #données : nbre de decès ,de naissance et l'immigration
    def yearly_projection(self, years):
        population = self.initial_population
        projections = []
        for year in range(1, years + 1):
            growth_rate = self.birth_rate - self.death_rate + self.net_migration_rate
            population += population * growth_rate
            projections.append((year, int(population)))
        return projections

    def calculate_annual_percentages(self, population):
        """
        Calcule les pourcentages de naissances et de décès pour une population donnée.
        """
        births = population * self.birth_rate
        deaths = population * self.death_rate
        print(f"\nPour une population de {population} :")
        print(f"- Naissances : {births:.0f} ({self.birth_rate * 100:.2f}%)")
        print(f"- Décès     : {deaths:.0f} ({self.death_rate * 100:.2f}%)")

    def compare_years(self, previous_population, current_population):
        """
        Compare la population d'une année à l'autre.
        """
        variation = current_population - previous_population
        percentage = (variation / previous_population) * 100
        trend = "croissance" if percentage > 0 else "décroissance" if percentage < 0 else "stabilité"
        print(f"\nComparaison de la population :")
        print(f"- Année précédente : {previous_population}")
        print(f"- Année actuelle   : {current_population}")
        print(f"→ Variation : {variation} habitants ({percentage:.2f}% → {trend})")

    def compare_birth_death_percentages(self, previous_birth_rate, previous_death_rate):
        """
        Compare les taux de naissance et de décès avec ceux de l'année précédente.
        """
        delta_birth = (self.birth_rate - previous_birth_rate) * 100
        delta_death = (self.death_rate - previous_death_rate) * 100

        print(f"\nComparaison des taux :")
        print(f"- Taux de natalité : {previous_birth_rate * 100:.2f}% → {self.birth_rate * 100:.2f}% ({delta_birth:+.2f}%)")
        print(f"- Taux de mortalité : {previous_death_rate * 100:.2f}% → {self.death_rate * 100:.2f}% ({delta_death:+.2f}%)")


# Exemple d'utilisation
if __name__ == "__main__":
    estimator = PopulationEstimator(
        initial_population=5000000,
        birth_rate=0.025,  # 2.5%
        death_rate=0.01,   # 1%
        net_migration_rate=0.002  # 0.2%
    )

    print("Estimation de la population dans 10 ans :")
    final_population = estimator.estimate_population(10)
    print(final_population)

    print("\nProjection annuelle pour les 10 prochaines années :")
    projections = estimator.yearly_projection(10)
    for year, pop in projections:
        print(f"Année {year} : {pop} habitants")

    # Calcul des pourcentages pour l'année 0 et l'année 10
    estimator.calculate_annual_percentages(estimator.initial_population)
    estimator.calculate_annual_percentages(final_population)

    # Comparaison des populations entre l'année 0 et 10
    estimator.compare_years(estimator.initial_population, final_population)

    # Comparaison des taux si l'année précédente avait d'autres taux
    estimator.compare_birth_death_percentages(previous_birth_rate=0.026, previous_death_rate=0.011)
