#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np


#2. Imprime la versión de NUMPY y la configuración.

print(np.version.version)

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

#Forma 1 randint
a = np.random.randint(0, 10, (2, 3, 5))

#Forma 2 random
#a = np.random.rand(2, 3, 5)

#Forma 3 random_sample
#a = np.random.random_sample((2, 3, 5))

#4. Imprime a.
print(a)


#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"
b = np.ones((5, 2, 3))

#6. Imprime b.

print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

if a.shape == b.shape:
    print('la forma es igual')
else:
    print('la forma no es igual')

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

#No se podrán sumar porque no tienen la misma forma
try:
    z = a + b
    print("Suma exitosa. Resultado:\n", z)
except ValueError as e:
    print("Error en la suma:", e)

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = b.transpose(1, 2, 0)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

try:
    d = a + c
    print("Suma exitosa. Resultado:\n", d)
except ValueError as e:
    print("Error en la suma:", e)

#Ahora funciona porque tiene la misma forma

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print(a)
print(d)
# d es 'a' a la que se le suma 1 en cada elemento de la matriz 

#12. Multiplica a y c. Asigna el resultado a e.

e = a * c 


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

if a.all()== e.all():
    print('Es igual e y a porque multiplicar una matriz de unos a otra matriz es como no hacer nada')

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

f = np.empty((2,3,5))


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

for i in range(d.shape[0]): #profundidad
    for j in range(d.shape[1]): #filas
        for k in range(d.shape[2]): #columnas
            # Obtener el valor correspondiente de d
            valor = d[i, j, k]

            # Asignar valores a f
            if valor == d_min:
                f[i, j, k] = 0
            elif valor == d_max:
                f[i, j, k] = 100
            elif valor == d_mean:
                f[i, j, k] = 50
            elif d_min < valor < d_mean:
                f[i, j, k] = 25
            elif d_mean < valor < d_max:
                f[i, j, k] = 75




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

print(f'esta es la matriz d {d}')

print(f'Esta es la matriz f {f}')



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
f = np.empty((2,3,5), dtype=str)
for i in range(d.shape[0]): #profundidad
    for j in range(d.shape[1]): #filas
        for k in range(d.shape[2]): #columnas
            # Obtener el valor correspondiente de d
            valor = d[i, j, k]

            # Asignar valores a f
            if valor == d_min:
                f[i, j, k] = 'A'
            elif valor == d_max:
                f[i, j, k] = 'B'
            elif valor == d_mean:
                f[i, j, k] = 'C'
            elif d_min < valor < d_mean:
                f[i, j, k] = 'D'
            elif d_mean < valor < d_max:
                f[i, j, k] = 'E'

print(f)