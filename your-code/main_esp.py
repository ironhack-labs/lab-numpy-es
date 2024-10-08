#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np


#2. Imprime la versión de NUMPY y la configuración.

np.version


#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

a = np.random.randint(0,100,(2,3,5))

#4. Imprime a.

print(a)

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

b = np.ones((5,2,3))

#6. Imprime b.

print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

print(f"Es la forma de a igual a la de b?\n{a.shape == b.shape}")
print(f"Tienen las mismas dimensiones a y b?\n{a.ndim == b.ndim}")
print(f"Tienen el mismo tamaño a y b?\n{a.size == b.size}")

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

print("print(a + b)")
print("---------ValueError-------------- ")
print("Sólo podemos sumar arrays que tengan la misma forma.")

#9. Transpon b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

c = b.reshape(2,3,5)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?
d = a + c
print(d)
print("Tienen la misma forma")

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

print(a)
print(d)
print('Todos los elementos de "d" son uno más que los de "a" porque hemos sumado "c" que es un array de unos')

#12. Multiplica a y c. Asigna el resultado a e.

e = a * c


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

print(e)
print('Es exactamente igual a "a" pq hemos multiplicados todos sus elementos por 1')

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)

print(f"'d': {d}")
print(f"d_max: {d_max}")
print(f"d_min: {d_min}")
print(f"d_mean: {d_mean}")

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

for i in range(len(f)):
    for j in range(len(f[i])):
        for k in range(len(f[i][j])):
            element = f[i][j][k]            
            if element > d_min and element < d_mean:
                f[i][j][k] = 25
            elif element > d_mean and element < d_max:
                f[i][j][k] = 75
            elif element == d_mean:
                f[i][j][k] = 50
            elif element == d_min:
                f[i][j][k] = 0
            elif element == d_max:
                f[i][j][k] = 100
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

f_dict = {"A":0, "B":25, "C":50, "D":75, "E":100}

def get_label(value, f_dict):
    if value == f_dict["A"]:
        return "A"
    elif value == f_dict["B"]:
        return "B"
    elif value == f_dict["C"]:
        return "C"
    elif value == f_dict["D"]:
        return "D"
    elif value == f_dict["E"]:
        return "E"
    
f_labeled = [[[get_label(value, f_dict) for value in row] for row in matrix] for matrix in f]
f_labeled
