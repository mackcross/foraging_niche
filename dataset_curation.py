from species_class import Species #Class Set Up
import pandas as pd 

df = pd.read_csv("data/Galán_Acedo/TrophicGuild.csv", encoding="latin-1")

for species_name in df['Species (ITIS)']:
    Species(species_name)

for sp in Species.all_instances():
    print(sp.name)

