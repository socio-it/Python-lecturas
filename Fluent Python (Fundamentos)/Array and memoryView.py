"""memoryview sirve para crear una vista directa de los datos sin copiar los datos
tipo apuntador es util para procesar grandes volumens de datos binarios"""
import array
x = array.array('i',range(500))
menv = memoryview(x)
print(len(menv))
print(menv[4])

"""Numpy hace algo igual pero con mas poder matematico"""
import numpy as np
a = np.arange(12)
print(type(a))
a.shape = 3, 4
print(a)