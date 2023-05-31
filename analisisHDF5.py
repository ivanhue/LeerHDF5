import h5py
from archivos import *
from itertools import chain
# from torch.utils.data import Dataloader
import logging as log
log.basicConfig(
    level=log.WARN,
    format='%(asctime)s %(message)s',
    datefmt='%H:%M:%S'
    )
# Archivos

def explorar_archivos(files):

    for j,f in enumerate(files):
        print("**************************************","ARCHIVO: ",j,"**************************************")
        # Recorre todos los archivos disponibles en la carpeta experimentos.
        for i in range(len(f)): 
            # Elegir posición 
            index = i

            # print(type(f1))
            print(list(f.keys()))
            try:
                value = list(f.keys())[index]
            except IndexError as e:
                log.info("Longitud excedida")
                value = list(f.keys())[0]
            espacios = ("\t"*index**2)+value+"--->"
            # print(espacios,"Hola")
            log.info(str(value))
            print(espacios+str(list(f[value])))
            # print(list(f1[value]['Raw']))
            print("\n\n")



def analisis(archivo):
    
    dset = archivo['3BData']['Raw']
    # dset.shape
    # print(dset.dtype)
    print(len(dset.shape))
    # print(dset[0][-8:-1])
    for i,fila in enumerate(dset):
        if 0 in fila:
            print("hay un valor cero en: ",i)
    print(len(dset))
    # dset.resize()
    # 219_406_336






def obtener_arbol(name):
    print((name))



def main():
    path = f["control"]
    file = h5py.File(path, 'r')
        # self.file = path
    dset = file['3BData']['Raw']
    # s = h5py.File('version03_0.brw', 'r')
    # explorar_archivos((s,))
    # obtener_arbol()
    
    # print(f1.keys())

    analisis(file)









if __name__ == "__main__":
    main()