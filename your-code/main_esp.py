#1. Importa el paquete NUMPY bajo el nombre np.

#[tu código aquí]

import numpy as np

#2. Imprime la versión de NUMPY y la configuración.

#[tu código aquí]

print("Versión de Numpy:", np.__version__)
np.show_config()

#3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a"
# Desafío: hay al menos tres maneras fáciles que usan numpy para generar arrays aleatorios. ¿Cuántas formas puedes encontrar?

#[tu código aquí]

a = np.random.random((2, 3, 5))


#4. Imprime a.

#[tu código aquí]

print("\nArray a:")
print(a)

'''
Array a:
[[[0.01122607 0.14374416 0.05549063 0.49972925 0.35791686]
  [0.80071337 0.66093297 0.91895483 0.34838548 0.11400443]
  [0.57675869 0.17377863 0.5007251  0.5434889  0.49692678]]

 [[0.63683943 0.46096616 0.91426954 0.51508917 0.52842475]
  [0.30646784 0.31527515 0.03435644 0.94103355 0.85235986]
  [0.18481951 0.28038175 0.55566151 0.16455659 0.1892707 ]]]
'''

#5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
#Asigna el array a la variable "b"

#[tu código aquí]

b = np.ones((5, 2, 3))

#6. Imprime b.

#[tu código aquí]

print("\nArray b:")
print(b)

'''

Array b:
[[[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]

 [[1. 1. 1.]
  [1. 1. 1.]]]


'''


#7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?

#[tu código aquí]

print("\n¿Tienen a y b el mismo tamaño?")
print("Tamaño de a:", a.size)
print("Tamaño de b:", b.size)
print("¿Son iguales?", a.size == b.size)

'''
¿Tienen a y b el mismo tamaño?
Tamaño de a: 30
Tamaño de b: 30
¿Son iguales? True

'''

#8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?

#[tu código aquí]

print("\nForma de a:", a.shape)
print("Forma de b:", b.shape)
print("¿Se pueden sumar?", a.shape == b.shape)

'''
Forma de a: (2, 3, 5)
Forma de b: (5, 2, 3)
¿Se pueden sumar? False

'''

#9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). Asigna el array transpuesto a la variable "c".

#[tu código aquí]

c = b.transpose(1, 2, 0)
print("\nArray c (b transpuesto):")
print(c)
print("Forma de c:", c.shape)

'''
Array c (b transpuesto):
[[[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]

 [[1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]
  [1. 1. 1. 1. 1.]]]
Forma de c: (2, 3, 5)

'''


#10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d". Pero, ¿por qué funciona ahora?

#[tu código aquí]

d = a + c
print("\nArray d (a + c):")
print(d)


'''
Array d (a + c):
[[[1.01122607 1.14374416 1.05549063 1.49972925 1.35791686]
  [1.80071337 1.66093297 1.91895483 1.34838548 1.11400443]
  [1.57675869 1.17377863 1.5007251  1.5434889  1.49692678]]

 [[1.63683943 1.46096616 1.91426954 1.51508917 1.52842475]
  [1.30646784 1.31527515 1.03435644 1.94103355 1.85235986]
  [1.18481951 1.28038175 1.55566151 1.16455659 1.1892707 ]]]

'''
# Funciona porque ahora tienen la misma forma (2, 3, 5).

#11. Imprime a y d. ¿Notas la diferencia y la relación entre los dos arrays en términos de los valores? Explica.

#[tu código aquí]

print("\nArray a:")
print(a)
print("\nArray d:")
print(d)

'''
Array a:
[[[0.01122607 0.14374416 0.05549063 0.49972925 0.35791686]
  [0.80071337 0.66093297 0.91895483 0.34838548 0.11400443]
  [0.57675869 0.17377863 0.5007251  0.5434889  0.49692678]]

 [[0.63683943 0.46096616 0.91426954 0.51508917 0.52842475]
  [0.30646784 0.31527515 0.03435644 0.94103355 0.85235986]
  [0.18481951 0.28038175 0.55566151 0.16455659 0.1892707 ]]]

Array d:
[[[1.01122607 1.14374416 1.05549063 1.49972925 1.35791686]
  [1.80071337 1.66093297 1.91895483 1.34838548 1.11400443]
  [1.57675869 1.17377863 1.5007251  1.5434889  1.49692678]]

 [[1.63683943 1.46096616 1.91426954 1.51508917 1.52842475]
  [1.30646784 1.31527515 1.03435644 1.94103355 1.85235986]
  [1.18481951 1.28038175 1.55566151 1.16455659 1.1892707 ]]]

'''
# La diferencia es que d es igual a a + 1, ya que c es un array de unos con la misma forma.


#12. Multiplica a y c. Asigna el resultado a e.

#[tu código aquí]

e = a * c
print("\nArray e (a * c):")
print(e)


'''
Array e (a * c):
[[[0.01122607 0.14374416 0.05549063 0.49972925 0.35791686]
  [0.80071337 0.66093297 0.91895483 0.34838548 0.11400443]
  [0.57675869 0.17377863 0.5007251  0.5434889  0.49692678]]

 [[0.63683943 0.46096616 0.91426954 0.51508917 0.52842475]
  [0.30646784 0.31527515 0.03435644 0.94103355 0.85235986]
  [0.18481951 0.28038175 0.55566151 0.16455659 0.1892707 ]]]

'''


#13. ¿Es e igual a a? ¿Por qué sí o por qué no?

#[tu código aquí]

print("\n¿Es e igual a a?", np.array_equal(e, a))
# Sí, porque multiplicar por 1 no cambia los valores.

'''
¿Es e igual a a? True
'''



#14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean"

#[tu código aquí]

d_max = d.max()
d_min = d.min()
d_mean = d.mean()
print("\nd_max:", d_max)
print("d_min:", d_min)
print("d_mean:", d_mean)

'''
d_max: 1.9410335523641349
d_min: 1.0112260745589934
d_mean: 1.4360849374247247

'''

#15. Ahora queremos etiquetar los valores en d. Primero crea un array vacío "f" con la misma forma (es decir, 2x3x5) que d usando `np.empty`.

#[tu código aquí]

f = np.empty(d.shape)
print("\nArray f vacío con la misma forma que d:")
print(f)

'''

Array f vacío con la misma forma que d:
[[[0.01122607 0.14374416 0.05549063 0.49972925 0.35791686]
  [0.80071337 0.66093297 0.91895483 0.34838548 0.11400443]
  [0.57675869 0.17377863 0.5007251  0.5434889  0.49692678]]

 [[0.63683943 0.46096616 0.91426954 0.51508917 0.52842475]
  [0.30646784 0.31527515 0.03435644 0.94103355 0.85235986]
  [0.18481951 0.28038175 0.55566151 0.16455659 0.1892707 ]]]
'''

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

f = np.empty(d.shape)

# Recorre todos los índices de d para asignar valores en f
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            valor = d[i, j, k]
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

print("\nArray f con etiquetas:")
print(f)

'''
Array f con etiquetas:
[[[  0.  25.  25.  75.  25.]
  [ 75.  75.  75.  25.  25.]
  [ 75.  25.  75.  75.  75.]]

 [[ 75.  75.  75.  75.  75.]
  [ 25.  25.  25. 100.  75.]
  [ 25.  25.  75.  25.  25.]]]
'''


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

print("\nArray d:")
print(d)

print("\nArray f con etiquetas:")
print(f)


'''
Array d:
[[[1.01122607 1.14374416 1.05549063 1.49972925 1.35791686]
  [1.80071337 1.66093297 1.91895483 1.34838548 1.11400443]
  [1.57675869 1.17377863 1.5007251  1.5434889  1.49692678]]

 [[1.63683943 1.46096616 1.91426954 1.51508917 1.52842475]
  [1.30646784 1.31527515 1.03435644 1.94103355 1.85235986]
  [1.18481951 1.28038175 1.55566151 1.16455659 1.1892707 ]]]

Array f con etiquetas:
[[[  0.  25.  25.  75.  25.]
  [ 75.  75.  75.  25.  25.]
  [ 75.  25.  75.  75.  75.]]

 [[ 75.  75.  75.  75.  75.]
  [ 25.  25.  25. 100.  75.]
  [ 25.  25.  75.  25.  25.]]]

'''

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

f = np.empty(d.shape, dtype=object)

# Recorre todos los índices de d para asignar valores en f con etiquetas de cadena
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            valor = d[i, j, k]
            if valor == d_min:
                f[i, j, k] = 'A'
            elif valor == d_max:
                f[i, j, k] = 'E'
            elif valor == d_mean:
                f[i, j, k] = 'C'
            elif d_min < valor < d_mean:
                f[i, j, k] = 'B'
            elif d_mean < valor < d_max:
                f[i, j, k] = 'D'

print("\nArray d:")
print(d)

print("\nArray f con etiquetas de cadena:")
print(f)


'''
Array d:
[[[1.01122607 1.14374416 1.05549063 1.49972925 1.35791686]
  [1.80071337 1.66093297 1.91895483 1.34838548 1.11400443]
  [1.57675869 1.17377863 1.5007251  1.5434889  1.49692678]]

 [[1.63683943 1.46096616 1.91426954 1.51508917 1.52842475]
  [1.30646784 1.31527515 1.03435644 1.94103355 1.85235986]
  [1.18481951 1.28038175 1.55566151 1.16455659 1.1892707 ]]]

Array f con etiquetas de cadena:
[[['A' 'B' 'B' 'D' 'B']
  ['D' 'D' 'D' 'B' 'B']
  ['D' 'B' 'D' 'D' 'D']]

 [['D' 'D' 'D' 'D' 'D']
  ['B' 'B' 'B' 'E' 'D']
  ['B' 'B' 'D' 'B' 'B']]]
  
'''
