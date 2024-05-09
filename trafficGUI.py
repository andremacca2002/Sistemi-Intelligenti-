import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")
from GeneratePath import PathGenerator

def main():
    # Creazione dell'interfaccia grafica
    window = tk.Tk()
    window.title("Tutti all'UNIBS")
    window.geometry("400x300")

    #stringa vuota per separare la grafica dal bordo superiore
    stringa_spazio = tk.Label(window, text="")
    stringa_spazio.pack(pady=30)

    # Etichetta per l'orario
    orario_label = tk.Label(window, text="Orario (HH:mm):")
    orario_label.pack()

    # Casella di testo per l'orario
    orario_input = tk.Entry(window)
    orario_input.pack()

    #stringa vuota per separare input orario da pulsante
    stringa_spazio2 = tk.Label(window, text="")
    stringa_spazio2.pack(pady=5)


    # Pulsante per generare il percorso
    generate_button = tk.Button(window, text="Genera Percorso", command=lambda: PathGenerator(orario_input.get()).generate_path())
    generate_button.pack(ipadx=5, ipady=3)

    # Funzione per abilitare il pulsante di generazione quando viene inserito l'orario
    def enable_generate_button(event):

        if orario_input.get().__len__() == 5 :
            generate_button.config(state="normal")
        else:
            generate_button.config(state="disabled")

    # Associa la funzione all'evento di inserimento di testo nell'entry di orario
    orario_input.bind("<KeyRelease>", enable_generate_button)

    # Pulsante per chiudere la finestra
    close_button = tk.Button(window, text="Chiudi", command=window.quit)
    close_button.pack(pady=8)

    window.mainloop()

if __name__ == '__main__':
    main()