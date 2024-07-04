import pandas as pd


class Loader:
    def __init__(self, commune):
        self.commune = commune
    
    def filter_commune(self):
        data = pd.read_csv("data/consommation_savoie_2018_all.csv", sep=";")
        return data[data["Nom COMMUNE"]==self.commune]
    