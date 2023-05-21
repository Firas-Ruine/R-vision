import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
def valider():
    messagebox.showinfo("Bienvenue", "Bienvenue !")

def reinitialiser():
    entry_nom.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_ville.delete(0, tk.END)

def quitter():
    fenetre.quit()

fenetre = tk.Tk()
fenetre.title("Interface")


# Création des widgets
label_nom = tk.Label(fenetre, text="Votre Nom:")
entry_nom = tk.Entry(fenetre)

label_prenom = tk.Label(fenetre, text="Votre Prénom:")
entry_prenom = tk.Entry(fenetre)

label_ville = tk.Label(fenetre, text="Votre Ville:")
entry_ville = tk.Entry(fenetre)

bouton_valider = tk.Button(fenetre, text="Valider", command=valider)
bouton_reinitialiser = tk.Button(fenetre, text="Réinitialiser", command=reinitialiser)
bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter)

# Placement des widgets dans la fenêtre
label_nom.grid(row=0, column=0, padx=10, pady=10)
entry_nom.grid(row=0, column=1, padx=10, pady=10)

label_prenom.grid(row=1, column=0, padx=10, pady=10)
entry_prenom.grid(row=1, column=1, padx=10, pady=10)

label_ville.grid(row=2, column=0, padx=10, pady=10)
entry_ville.grid(row=2, column=1, padx=10, pady=10)

bouton_valider.grid(row=3, column=0, padx=10, pady=10)
bouton_reinitialiser.grid(row=3, column=1, padx=10, pady=10)
bouton_quitter.grid(row=3, column=2, padx=10, pady=10)

# Chargement de l'image
image_path = "./medyassine.jpg"  # Remplacez "medyassine.jpg" par le chemin vers votre image
image = Image.open(image_path)
image = image.resize((100, 100))  # Réduire la taille de l'image si nécessaire
photo = ImageTk.PhotoImage(image)

# Création du widget pour afficher l'image
label_image = tk.Label(fenetre, image=photo)
label_image.grid(row=0, column=2, rowspan=2, padx=10, pady=10)


# Obtenir les dimensions de l'écran
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()

# Calculer la position du centre de l'écran
window_width = 400  # Largeur de la fenêtre
window_height = 250  # Hauteur de la fenêtre
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Positionner la fenêtre au centre de l'écran
fenetre.geometry(f"{window_width}x{window_height}+{x}+{y}")
fenetre.mainloop()
