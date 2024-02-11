import pandas as pd

annees = [2018, 2019, 2020, 2021, 2022]

caracteristiques_lum = { 
    1: "Plein jour",
    2: "Crépuscule ou aube",
    3: "Nuit sans éclairage public",
    4: "Nuit avec éclairage public non allumé",
    5: "Nuit avec éclairage public allumé"
}

caracteristiques_agg = {
    1: "Hors agglomération",
    2: "En agglomération"
}

caracteristiques_int = {
    1: "Hors intersection",
    2: "Intersection en X",
    3: "Intersection en T",
    4: "Intersection en Y",
    5: "Intersection à plus de 4 branches",
    6: "Giratoire",
    7: "Place",
    8: "Passage à niveau",
    9: "Autre intersection"
}

caracteristiques_atm = {
    -1: "Non renseigné",
    1: "Normale",
    2: "Pluie légère",
    3: "Pluie forte",
    4: "Neige - grêle",
    5: "Brouillard - fumée",
    6: "Vent fort - tempête",
    7: "Temps éblouissant",
    8: "Temps couvert",
    9: "Autre"
}

caracteristiques_col = {
    -1: "Non renseigné",
    1: "Deux véhicules - frontale",
    2: "Deux véhicules – par l’arrière",
    3: "Deux véhicules – par le coté",
    4: "Trois véhicules et plus – en chaîne",
    5: "Trois véhicules et plus - collisions multiples",
    6: "Autre collision",
    7: "Sans collision"
}

lieux_catr = {
    1: "Autoroute",
    2: "Route nationale",
    3: "Route Départementale",
    4: "Voie Communales",
    5: "Hors réseau public",
    6: "Parc de stationnement ouvert à la circulation publique",
    7: "Routes de métropole urbaine",
    9: "autre"
}

lieux_surf = {
    -1: "Non renseigné",
    1: "Normale",
    2: "Mouillée",
    3: "Flaques",
    4: "Inondée",
    5: "Enneigée",
    6: "Boue",
    7: "Verglacée",
    8: "Corps gras - huile",
    9: "Autre"
}

lieux_situ = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Sur chaussée",
    2: "Sur bande d’arrêt d’urgence",
    3: "Sur accotement",
    4: "Sur trottoir",
    5: "Sur piste cyclable",
    6: "Sur autre voie spéciale",
    8: "Autres"
}

vehicules_catv = {
    00: "Indéterminable",
    1: "Bicyclette",
    2: "Cyclomoteur <50cm3",
    3: "Voiturette (Quadricycle à moteur carrossé)",
    4: "Référence inutilisée depuis 2006 (scooter immatriculé)",
    5: "Référence inutilisée depuis 2006 (motocyclette)",
    6: "Référence inutilisée depuis 2006 (side-car)",
    7: "VL seul",
    8: "Référence inutilisée depuis 2006 (VL + caravane)",
    9: "Référence inutilisée depuis 2006 (VL + remorque)",
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque",
    11: "Référence inutilisée depuis 2006 (VU (10) + caravane)",
    12: "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    13: "PL seul 3,5T <PTCA <= 7,5T",
    14: "PL seul > 7,5T",
    15: "PL > 3,5T + remorque",
    16: "Tracteur routier seul",
    17: "Tracteur routier + semi-remorque",
    18: "Référence inutilisée depuis 2006 (transport en commun)",
    19: "Référence inutilisée depuis 2006 (tramway)",
    20: "Engin spécial",
    21: "Tracteur agricole",
    30: "Scooter < 50 cm3",
    31: "Motocyclette > 50 cm3 et <= 125 cm3",
    32: "Scooter > 50 cm3 et <= 125 cm3",
    33: "Motocyclette > 125 cm3",
    34: "Scooter > 125 cm3",
    35: "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)",
    36: "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)",
    37: "Autobus",
    38: "Autocar",
    39: "Train",
    40: "Tramway",
    41: "3RM <= 50 cm3",
    42: "3RM > 50 cm3 <= 125 cm3",
    43: "3RM > 125 cm3",
    50: "EDP à moteur",
    60: "EDP sans moteur",
    80: "VAE",
    99: "Autre véhicule"
}

usagers_catu = {
    1: "Conducteur",
    2: "Passager",
    3: "Piéton"
}

usagers_grav = {
    1: "Indemne",
    2: "Tué",
    3: "Blessé hospitalisé",
    4: "Blessé léger"
}

usagers_sexe = {
    1: "Masculin",
    2: "Féminin"
}

df_final = pd.DataFrame()

for a in annees:
    if a == 2018:
        df_caracteristiques = pd.read_csv(f"./csv/caracteristiques-{a}.csv", low_memory=False, sep=",", encoding="latin-1")
        df_lieux = pd.read_csv(f"./csv/lieux-{a}.csv", low_memory=False, sep=",", encoding="latin-1")
        df_usagers = pd.read_csv(f"./csv/usagers-{a}.csv", low_memory=False, sep=",", encoding="latin-1")
        df_vehicules = pd.read_csv(f"./csv/vehicules-{a}.csv", low_memory=False, sep=",", encoding="latin-1")
    else:
        df_caracteristiques = pd.read_csv(f"./csv/caracteristiques-{a}.csv", low_memory=False, sep=";", encoding="latin-1")
        df_lieux = pd.read_csv(f"./csv/lieux-{a}.csv", low_memory=False, sep=";", encoding="latin-1")
        df_usagers = pd.read_csv(f"./csv/usagers-{a}.csv", low_memory=False, sep=";", encoding="latin-1")
        df_vehicules = pd.read_csv(f"./csv/vehicules-{a}.csv", low_memory=False, sep=";", encoding="latin-1")

    # merge des 4 dataframes
    df = pd.merge(df_caracteristiques, df_lieux, on="Num_Acc")
    df = pd.merge(df, df_usagers, on="Num_Acc")
    df = pd.merge(df, df_vehicules, on="Num_Acc")

    df['agg'] = df['agg'].map(caracteristiques_agg)
    df['int'] = df['int'].map(caracteristiques_int)
    df['atm'] = df['atm'].map(caracteristiques_atm)
    df['col'] = df['col'].map(caracteristiques_col)
    df['lum'] = df['lum'].map(caracteristiques_lum)
    df['catr'] = df['catr'].map(lieux_catr)
    df['surf'] = df['surf'].map(lieux_surf)
    df['situ'] = df['situ'].map(lieux_situ)
    df['catv'] = df['catv'].map(vehicules_catv)
    df['catu'] = df['catu'].map(usagers_catu)
    df['grav'] = df['grav'].map(usagers_grav)
    df['sexe'] = df['sexe'].map(usagers_sexe)


    print(df.head())

    # ajout du dataframe à df_final
    df_final = pd.concat([df_final, df])

    #sauvegarde du dataframe
    #df.to_csv(f"./csv/tri/df-{a}.csv", index=False)

#sauvegarde du dataframe final
df_final = df_final.drop(columns=["id_vehicule_y", "env1", "infra", "vma", "com", "adr", "v1", "v2", "circ", "nbv", "vosp", "prof", "pr", "pr1", "plan", "lartpc", "larrout", "situ", "id_vehicule_x", "num_veh_x", "senc", "obs", "obsm", "choc", "manv", "motor", "occutc", "place", "trajet", "secu1", "secu2", "secu3", "locp", "actp", "etatp", "num_veh_y", "id_usager"])
    
df_final = df_final.drop_duplicates(subset=df_final.columns[:-1])
df_final.to_csv("./csv/tri/df_final.csv", index=False)