#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np

#2. Imprime la versión de NUMPY y la configuración.

print(f"NumPy version: {np.__version__}")
np.show_config()

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

a = np.random.rand(2, 3, 5)
print(f"\nEjercicio 3.1:\n{a}")
a2 = np.random.randn(2, 3, 5)
print(f"\nEjercicio 3.2:\n{a2}")
a3 = np.random.randint(0, 10, size=(2, 3, 5))
print(f"\nEjercicio 3.3:\n{a3}")

#4. Imprime a.

print(f"\nEjercicio 4:\n{a}")

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

b = np.ones((5, 2, 3))

#6. Imprime b.

print(f"\nEjercicio 6:\n{b}")

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

a_size = a.size
b_size = b.size
print(f"\nEjercicio 7: {a_size==b_size}")

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

same_shape = a.shape == b.shape
print(f"\nEjercicio 8: {same_shape} Para poder ser sumadas, dos matrices tienen que tener la misma forma (shape), en este caso 'a' y 'b' tienen formas distintas\nForma de a:{a.shape}\nForma de b: {b.shape}")

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = b.transpose(1, 2, 0)
print(f"\nEjercicio 9: Forma de c: {c.shape}")

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

d = a + c
print(f"\nEjercicio 10: d = \n{d}\n 'a' y 'c' se pueden sumar porque tienen la misma forma (shape)")

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print(f"\nEjercicio 11:\n{a}\n\n{d}\nLos valores de 'd' son 1 más que los valores de 'a' en la misma posición, se debe a que la matriz 'd' esta formada por todo 1")


#12. Multiplica a y c. Asigna el resultado a e.

e = a*c
print(f"\nEjercicio 12: e =\n{e}")


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

print(f"\nEjercicio 13: a =\n{a}")
print(f"\nEjercicio 13: e =\n{e}")
print(f"\nEjercicio 13: a = e? \n{a==e}, 'e' se obtiene de multiplicar los valores de 'a' por 'c' (que son todo 1), por lo que salen los mismos valores")

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(f"\nEjercicio 14: d_max = {d_max}, d_min = {d_min}, d_mean = {d_mean}")

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

f = np.empty((2, 3, 5))
print(f"\nEjercicio 15: f.shape = {f.shape}")
print(f"\nEjercicio 15: f =\n{f}")

"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

for i in range(d.shape[0]):
  for j in range(d.shape[1]):
    for k in range(d.shape[2]):
        if d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = 25
        elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = 75
        elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
        elif d[i, j, k] == d_min:
                f[i, j, k] = 0
        elif d[i, j, k] == d_max:
                f[i, j, k] = 100

print(f"\nEjercicio 16: f =\n{f}")
    

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

print(f"\nEjercicio 17: d =\n{d}")
print(f"\nEjercicio 17: f =\n{f}")


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

f = np.empty((2, 3, 5), dtype=str)
print(f"\nEjercicio 18: f.dtype = {f.dtype}; '<U1' indica que el tipo de dato de 'f' es una cadena unicode de longitud 1")
print(f"\nEjercicio 18: f.shape = {f.shape}")
print(f"\nEjercicio 18: f =\n{f}")

for i in range(d.shape[0]):
  for j in range(d.shape[1]):
    for k in range(d.shape[2]):
        if d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = "B"
        elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = "D"
        elif d[i, j, k] == d_mean:
                f[i, j, k] = "C"
        elif d[i, j, k] == d_min:
                f[i, j, k] = "A"
        elif d[i, j, k] == d_max:
                f[i, j, k] = "E"

print(f"\nEjercicio 18: f =\n{f}")