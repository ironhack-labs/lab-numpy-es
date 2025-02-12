#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np

#2. Imprime la versión de NUMPY y la configuración.

print("Ejercicio 2")
print(np.__version__)
print(np.show_config())

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

a = np.random.randint(100, size=(2, 3, 5))

#alternativas
a2 = np.random.random((2, 3, 5))
a3 = np.array([np.random.randint(100, size=(3, 5)), np.random.randint(100, size=(3, 5))])

#4. Imprime a.

print("Ejercicio 4")
print(a)

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

b = np.ones((5, 2, 3), dtype="int")

#6. Imprime b.

print("Ejercicio 6")
print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

print("Ejercicio 8")
print(a.size == b.size)

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

# No es posible sumarlas porque no tienen las mismas dimensiones, aunque tengan el mismo tamaño. Una es 2x3x5 y la otra es 5x3x2.

try:
        print(a + b) #ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)
except:
        pass
print("Ejercicio 8")
print("ValueError: operands could not be broadcast together with shapes (2,3,5) (5,2,3)")

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = np.transpose(b, axes=(1,2,0))
print("Ejercicio 9")
print(c)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

d = a + c
print("Ejercicio 10")
print(d)

# Funciona porque las matrices son ahora de mismas dimensiones. Ha habido que elegir el orden de transposición para hacerlas coincidir, no obstante.

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print("Ejercicio 11")
print(a)
print(d)

# En primer lugar, las dos matrices tienen las mismas dimensiones. En segundo lugar, "d" es resultado de sumar 1 a cada uno de los valores de "a".

#12. Multiplica a y c. Asigna el resultado a e.

e = a * c

#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

print("Ejercicio 13")
print(a)
print(e)

# "e" equivale a "a" porque es resultado de multiplicar cada valor de "a" por 1.

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print("Ejercicio 14")
print(d_max)
print(d_min)
print(d_mean)

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

f = np.empty((2, 3, 5))

"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100

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

print("Ejercicio 17")
print(d)
print(f)

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

g = np.empty((2, 3, 5), dtype="str")

g[(d > d_min) & (d < d_mean)] = "B"
g[(d > d_mean) & (d < d_max)] = "D"
g[d == d_mean] = "C"
g[d == d_min] = "A"
g[d == d_max] = "E"

print("Ejercicio 18")
print(d)
print(g)