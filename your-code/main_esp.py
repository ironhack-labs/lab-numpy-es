#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np


#2. Imprime la versión de NUMPY y la configuración.

import numpy as np

print(f"Versión de NumPy: {np.__version__}")
print("Configuración de NumPy: ")
np.show_config()

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

import numpy as np

a = (np.random.rand(2, 3, 5))
print (a)

#4. Imprime a.

print (a)

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

import numpy as np

b = np.ones(((5, 2, 3)))
print (b)

#6. Imprime b.

print (b)


#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

import numpy as np

a = np.random.rand(2, 3, 5)
b = np.ones((5, 2, 3))

print(a.shape == b.shape)

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

import numpy as np

a = np.random.rand(2, 3, 5)
b = np.ones((5, 2, 3))

try:
    print(a + b)
    print("Es posible sumar porque los arrays tienen la misma forma.")
except ValueError as e:
    print(f"No es posible sumar: {e}")

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

import numpy as np

b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))

print (b)
print (c)


#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c

print (a)
print (c)
print (d)

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c

print (a)
print (d)
print ("Se ha hecho la suma de un entero a los decimales de a")

#12. Multiplica a y c. Asigna el resultado a e.

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
e = a * c

print (a)
print (c)
print (e)


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

import numpy as np

a = np.random.rand(2, 3, 5)
b = np.ones((5, 2, 3))
c = b.reshape((2, 3, 5))
e = a * c

print(a)
print(c)
print(e)
print("Es igual porque multiplicar por 1 no cambia los valores.")

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c

mi = d.min()
ma = d.max()
me = d.mean()

print (mi)
print (ma)
print (me)
print ()
print (d)

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c

f = np.empty(((2, 3, 5)))


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c
f = np.empty(((2, 3, 5)))

mi = d.min()
ma = d.max()
me = d.mean()

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        if d[i, j, k] > mi and d[i, j, k] < me:
                                f[i, j, k] = 25
                        if d[i, j, k] > me and d[i, j, k] < ma:
                                f[i, j, k] = 75
                        if d[i, j, k] == me:
                                f[i, j, k] = 50
                        if d[i, j, k] == mi:
                                f[i, j, k] = 0
                        if d[i, j, k] == ma:
                                f[i, j, k] = 100
print (d)
print (f)

"""
#17. Imprime d y f. ¿Tienes el f esperado?
Por ejemplo, si tu d es:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Tu f debería ser:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

import numpy as np

a = (np.random.rand(2, 3, 5))
b = np.ones(((5, 2, 3)))
c = b.reshape(((2, 3, 5)))
d = a + c
f = np.empty(((2, 3, 5)))

mi = d.min()
ma = d.max()
me = d.mean()

for i in range(d.shape[0]):
        for j in range(d.shape[1]):
                for k in range(d.shape[2]):
                        if d[i, j, k] > mi and d[i, j, k] < me:
                                f[i, j, k] = 25
                        if d[i, j, k] > me and d[i, j, k] < ma:
                                f[i, j, k] = 75
                        if d[i, j, k] == me:
                                f[i, j, k] = 50
                        if d[i, j, k] == mi:
                                f[i, j, k] = 0
                        if d[i, j, k] == ma:
                                f[i, j, k] = 100
print (d)
print (f)

"""
#18. Pregunta de bonificación: en lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""
