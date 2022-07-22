import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars)for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


#1er fenetre
window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background='#4065A4')

# creer la frame principale
frame= Frame(window, bg='#4065A4')

#creer un sous boite
right_frame = Frame(frame, bg='#4065A4')



#creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()

#creer un champ/input

password_entry = Entry(right_frame, font=("helvetica", 20), bg='#4065A4', fg='white')
password_entry.pack()
#creer un BOUTON
generate_password_button = Button(right_frame, text="Generer", font=("helvetica", 20), bg='#4065A4', fg='white', command=generate_password)
generate_password_button.pack(fill=X)


right_frame.grid(row=0, column=1, sticky=W)
#afficher la frame

frame.pack(expand=YES)

#afficher la barre de menu
menu_bar = Menu(window)
#creer 1er menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command = generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# ajouter menu bar
window.config(menu=menu_bar)

#afficher fenetre
window.mainloop()
