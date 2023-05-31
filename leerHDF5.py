import h5py
import numpy as np
import matplotlib.pyplot as plt
from archivos import *
import logging as log
log.basicConfig(
    level=log.NOTSET,
    format='%(asctime)s %(message)s',
    datefmt='%H:%M:%S'
    )



class Archivo:
    def __init__(self, path, mode='r', size=4096) -> None:
        self.size = size
        self.file = h5py.File(path, mode)
        # self.file = path
        self.dset = self.file['3BData']['Raw']
    


    def get_matriz(self, index: int):
        if not len(self.dset.shape) == 1:
            log.info("Ya es una matriz")
            return self.dset[()]
        
        if index > self.dset.size/4096:
            raise IndexError("Indice invalido")
        vector = self.dset[()]
        
        num_filas = 4096
        num_columnas = int(round(self.dset.size/4096))
        log.info("Creando matriz:")
        matriz = np.reshape(vector, (num_filas, num_columnas), order='F')
        log.info("Matriz creada")
        return matriz





def encontrar_errores(matriz):
    cantidad_ceros_por_fila = []
    log.info("Buscando errores")
    for fila in matriz:
        cantidad_no_ceros = np.count_nonzero(fila)
        cantidad_total = fila.size
        cantidad_ceros = cantidad_total - cantidad_no_ceros
        cantidad_ceros_por_fila.append(cantidad_ceros)
    
    if cantidad_ceros_por_fila[0] != cantidad_total:
        print("Hay valores no cero en tierra")
    if (np.count_nonzero(cantidad_ceros_por_fila[1:])) != 0:
        print("Hay valores cero en la matriz")
    log.info("Busqueda terminada")

    return cantidad_ceros_por_fila




# print(f["control"])





file = Archivo(f["control"])

matriz = file.get_matriz(2)
# data = np.array(matriz)

plt.imshow(matriz[1:])
# plt.plot(np.arange(1,11), data.transpose())
plt.show()

print(matriz.shape)








# arr = encontrar_errores(matriz)

# print(np.count_nonzero(arr[1:]))


