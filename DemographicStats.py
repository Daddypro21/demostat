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
