import sqlite3

#TODO: Question 1
# Connexion à la base de données
conn = sqlite3.connect("hopital.db")
cursor = conn.cursor()

#TODO: Question 2
# Création de la table Patient
cursor.execute("""CREATE TABLE IF NOT EXISTS Patient (
                    IdPatient INTEGER PRIMARY KEY,
                    Nom TEXT NOT NULL,
                    Prenom TEXT NOT NULL,
                    Age INTEGER,
                    Date_Entree TEXT,
                    Date_Sortie TEXT,
                    CHECK (Age >= 0),
                    CHECK (Date_Sortie IS NULL OR Date_Sortie != '')
                )""")

# Création de la table Plat
cursor.execute("""CREATE TABLE IF NOT EXISTS Plat (
                    IdPlat INTEGER PRIMARY KEY,
                    Nom TEXT NOT NULL,
                    Calories INTEGER NOT NULL CHECK (Calories > 0)
                )""")

#TODO: Question 3
# Informations du patient à ajouter
patient_info = (1256, 'BEN FOULEN', 'Mohamed', 61, '01/05/2023', None)

# Requête pour insérer le patient dans la table
# cursor.execute("""INSERT INTO Patient (IdPatient, Nom, Prenom, Age, Date_Entree, Date_Sortie)
#                 VALUES (?, ?, ?, ?, ?, ?)""", patient_info)

#TODO: Question 4
# Informations du plat à ajouter
plat_info = (26, 'Riz', 350)

# Requête pour insérer le plat dans la table
# cursor.execute("""INSERT INTO Plat (IdPlat, Nom, Calories)
#                 VALUES (?, ?, ?)""", plat_info)

#TODO: Question 5
# Nouveau nombre de calories
nouveau_nombre_calories = 1200

# Requête pour mettre à jour le plat avec l'identifiant 26
# cursor.execute("""UPDATE Plat SET Calories = ? WHERE IdPlat = ?""",
#                (nouveau_nombre_calories, 26))

#TODO: Question 6

# Requête pour supprimer les plat avec un nombre de calories inférieur à 400
cursor.execute("""DELETE FROM Plat WHERE Calories < 400""",)

#TODO: Question 6
# Requête pour récupérer tous les patients
# cursor.execute("SELECT * FROM Patient")
# patients = cursor.fetchall()

# # Affichage des patients
# for patient in patients:
#     print(patient)

#TODO: Question 7
# Requête pour récupérer les patients âgés entre 25 et 50 ans
cursor.execute("""SELECT IdPatient, Nom, Prenom, Date_Entree
                  FROM Patient
                  WHERE Age BETWEEN 25 AND 50""")
patients = cursor.fetchall()

# Affichage des informations des patients
for patient in patients:
    print("IdPatient:", patient[0])
    print("Nom:", patient[1])
    print("Prénom:", patient[2])
    print("Date d'entrée:", patient[3])
    print()

# Enregistrement des modifications et fermeture de la connexion
conn.commit()
conn.close()


