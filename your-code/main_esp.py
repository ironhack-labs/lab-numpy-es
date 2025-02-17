#1. Importa el paquete NUMPY bajo el nombre np.

#[tu código aquí]
import numpy as np

#2. Imprime la versión de NUMPY y la configuración.
 
#[tu código aquí]
print("Versión de NumPy:", np.__version__) # versión de NumPy

np.show_config() # configuración de NumPy

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

#[tu código aquí]
a = np.random.rand(2, 3, 5) # manera 1: usando random.rand

a2 = np.random.random_sample((2, 3, 5)) # manera 2: usando random.random_sample

a3 = np.random.uniform(low=0, high=1, size=(2, 3, 5)) # manera 3: usando random.uniform

#4. Imprime a.

#[tu código aquí]
print(a)

print(a2)

print(a3)

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

#[tu código aquí]
b = np.ones((5, 2, 3))

#6. Imprime b.

#[tu código aquí]
print(b)

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

#[tu código aquí]
print("¿Tienen a y b el mismo tamaño?", a.size == b.size)

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no? 
# No, no es posible sumar a y b directamente porque tienen formas (shape) diferentes.

#[tu código aquí]
try:
    resultado = a + b
except ValueError as e:
    print("Error:", e)

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

#[tu código aquí]
c = b.transpose(1, 2, 0)
print(c)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?
#Porque c tiene la misma forma que a ((2,3,5)), la suma funcionará sin problemas. 

#[tu código aquí]
d = a + c
print("Suma de a + c:\n", d)

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.
# 'a' es el array original con valores aleatorios entre 0 y 1 y 'd' es el resultado de la suma a + c, la suma aumenta cada valor de a en 1 porque c era un array lleno de unos.

#[tu código aquí]
print(a)
print(d)

#12. Multiplica a y c. Asigna el resultado a 'e'.

#[tu código aquí]
e = a * c
print("Array e (a * c):\n", e)

#13. ¿Es e igual a a? ¿Por qué sí o por qué no?
# Si son exactamente iguales porque 'c' es una array de unos y multiplicar por 1 no cambia los valores.

#[tu código aquí]
print("¿Son iguales a y e?", a == e)
print("¿e = a?", np.array_equal(e, a))


#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

#[tu código aquí]
d_max = np.max(d)   # Valor máximo
d_min = np.min(d)   # Valor mínimo
d_mean = np.mean(d) # Promedio

print("Valor máximo en d:", d_max)
print("Valor mínimo en d:", d_min)
print("Promedio de d:", d_mean)

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

#[tu código aquí]
f = np.empty(d.shape)


"""
#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""

#[tu código aquí]
for i in range(d.shape[0]):  # primera dimensión
    for j in range(d.shape[1]):  # segunda dimensión
        for k in range(d.shape[2]):  # tercera dimensión
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100
            elif d_min < d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50
            elif d_mean < d[i, j, k] < d_max:
                f[i, j, k] = 75
print(f)



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

#[tu código aquí]
print(d)
print(f)

# 


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

#[tu código aquí]
g = np.empty(d.shape, dtype=object)

g[d == d_min] = "A" 
g[(d > d_min) & (d < d_mean)] = "B"
g[d == d_mean] = "C" 
g[(d > d_mean) & (d < d_max)] = "D"
g[d == d_max] = "E"  

print(g)