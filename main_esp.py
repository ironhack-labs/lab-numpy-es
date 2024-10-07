#1. Importa el paquete NUMPY bajo el nombre np.
import numpy as np

#2. Imprime la versión de NUMPY y la configuración.
print(np.version.version)
print()

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?
a = np.random.randint(0,10,size=(2,3,5))
a = np.random.random((2,3,5))

#4. Imprime a.
print(a)
print()

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"
b = np.random.randint(1,2,size=(5,3,2))
b = np.ones((5,3,2))

#6. Imprime b.
print(b)
print()

#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?
print("a y b son del mismo tamaño" if a.shape==b.shape else "a y b son de tamaño diferente")
print()

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?
'''No porque son de distinta forma'''

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".
c = np.transpose(b)

#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?
'''Funciona porque son de la misma forma'''
d = a + c

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.
print(a)
print(d)
'''Se han sumado término a término a y c, y d tiene una unidad más en cada uno'''

#12. Multiplica a y c. Asigna el resultado a e.
e = a * c

#13. ¿Es e igual a a? ¿Por qué sí o por qué no?
e,a
'''Se han multiplicado los términos por 1 y se quedan igual'''

#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print()
print(f"Max: {d_max}, Min: {d_min}, Med: {d_mean}")
print()

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.
f = np.empty([2,3,5])

#16. Rellena los valores en f. Para cada valor en d, si es mayor que d_min pero menor que d_mean, asigna 25 al valor correspondiente en f.
"""
Si un valor en d es mayor que d_mean pero menor que d_max, asigna 75 al valor correspondiente en f.
Si un valor es igual a d_mean, asigna 50 al valor correspondiente en f.
Asigna 0 al valor correspondiente(s) en f para d_min en d.
Asigna 100 al valor correspondiente(s) en f para d_max en d.
Al final, f debería tener solo los siguientes valores: 0, 25, 50, 75 y 100.
Nota: no necesitas usar Numpy en esta pregunta.
"""
f = np.reshape(f,-1)
i = 0
for dato in np.reshape(d,-1):
    if dato > d_min and dato < d_mean:
        f[i] = 25
    elif dato > d_mean and dato < d_max:
        f[i] = 75
    elif dato == d_mean: 
        f[i] = 50
    elif dato == d_min: 
        f[i] = 0  
    elif dato == d_max: 
        f[i] = 100        
    i += 1

f = np.reshape(f,d.shape)

#17. Imprime d y f. ¿Tienes el f esperado?
"""
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
print()
print(f)

#18. Pregunta de bonificación: 
"""
En lugar de usar números (es decir, 0, 25, 50, 75 y 100), ¿cómo usar valores de cadena 
("A", "B", "C", "D" y "E") para etiquetar los elementos del array? Esperas el resultado sea:
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
De nuevo, no necesitas Numpy en esta pregunta.
"""
g = np.empty([2,3,5], dtype="str")

g = np.reshape(g,-1)
i = 0
for dato in np.reshape(d,-1):
    if dato > d_min and dato < d_mean:
        g[i] = 'A'
    elif dato > d_mean and dato < d_max:
        g[i] = 'B'
    elif dato == d_mean: 
        g[i] = 'C'
    elif dato == d_min: 
        g[i] = 'D'  
    elif dato == d_max: 
        g[i] = 'E'        
    i += 1
    
g = np.reshape(g,d.shape)
print(d)
print()
print(g)

pass