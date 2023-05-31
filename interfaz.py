import customtkinter
import threading
import time
import numpy as np



from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import logging as log
log.basicConfig(
    level=log.INFO,
    format='%(asctime)s %(message)s',
    datefmt='%H:%M:%S'
    )


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("800x600")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=20, fill="both", expand=True)


class ComputeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        button.configure(state="disabled")
        log.info(" ********** Calculando resultados ********** ")
        print("Hola")
        time.sleep(2.1)
        print("Adios")
        log.info(" ********** Termino de calcular ********** ")
        button.configure(state="normal")


def obtener_resultados():
    t = ComputeThread()
    t.start()

def empezar_resultados():
    # button.configure(state="disabled")
    # threading.Thread(target=obtener_resultados).start()
    obtener_resultados()
    # button.configure(state="normal")


label = customtkinter.CTkLabel(master=frame, text="Spike sorting", font=("Roboto", 32))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Calcular trayectorias", command=empezar_resultados)
button.pack(pady=12, padx=10)


    
    

if __name__ == "__main__":
    root.mainloop()