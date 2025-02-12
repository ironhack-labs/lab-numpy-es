#1. Importa el paquete NUMPY bajo el nombre np.

import numpy as np

# 2. Imprime la versión de NUMPY y la configuración.
numpy_version = np.__version__
numpy_config = np.show_config()

# 3. Genera un array tridimensional de 2x3x5 con valores aleatorios. Asigna el array a la variable "a".
a = np.random.rand(2, 3, 5)

# 4. Imprime a.
print("Array a:\n", a)

# 5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1. Asigna el array a la variable "b".
b = np.ones((5, 2, 3))

# 6. Imprime b.
print("Array b:\n", b)

# 7. ¿Tienen a y b el mismo tamaño? ¿Cómo lo demuestras en código Python?
same_size = a.size == b.size
print("¿a y b tienen el mismo tamaño?", same_size)

# 8. ¿Es posible sumar a y b? ¿Por qué sí o por qué no?
can_add = a.shape == b.shape
print("¿Se pueden sumar a y b?", can_add, "- No se pueden sumar porque sus formas son diferentes:", a.shape, b.shape)

# 9. Transpone b para que tenga la misma estructura que a (es decir, se convierta en un array de 2x3x5). 
# Asigna el array transpuesto a la variable "c".
c = b.transpose(1, 2, 0)

# 10. Intenta sumar a y c. Ahora debería funcionar. Asigna la suma a la variable "d".
d = a + c
print("Array d (suma de a y c):\n", d)

# 11. Imprime a y d.
print("Array a:\n", a)
print("Array d:\n", d)

# 12. Multiplica a y c. Asigna el resultado a e.
e = a * c

# 13. ¿Es e igual a a? ¿Por qué sí o por qué no?
e_equals_a = np.array_equal(e, a)
print("¿Es e igual a a?", e_equals_a, "- Sí, porque c contiene solo unos, por lo que la multiplicación no altera los valores.")

# 14. Identifica los valores máximos, mínimos y medios en d. Asigna esos valores a las variables "d_max", "d_min" y "d_mean".
d_max = np.max(d)
d_min = np.min(d)
d_mean = np.mean(d)
print(f"Máximo: {d_max}, Mínimo: {d_min}, Media: {d_mean}")

# 15. Crea un array vacío "f" con la misma forma que d usando `np.empty`.
f = np.empty(d.shape)

# 16. Rellena los valores en f con base en las condiciones establecidas.
for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f[i, j, k] = 0
            elif d[i, j, k] == d_max:
                f[i, j, k] = 100
            elif d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f[i, j, k] = 25
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f[i, j, k] = 75
            elif d[i, j, k] == d_mean:
                f[i, j, k] = 50

# 17. Imprime d y f.
print("Array d:\n", d)
print("Array f:\n", f)

# 18. Usar valores de cadena ("A", "B", "C", "D" y "E") en lugar de números.
f_labels = np.empty(d.shape, dtype=str)

for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        for k in range(d.shape[2]):
            if d[i, j, k] == d_min:
                f_labels[i, j, k] = "A"
            elif d[i, j, k] == d_max:
                f_labels[i, j, k] = "E"
            elif d[i, j, k] > d_min and d[i, j, k] < d_mean:
                f_labels[i, j, k] = "B"
            elif d[i, j, k] > d_mean and d[i, j, k] < d_max:
                f_labels[i, j, k] = "D"
            elif d[i, j, k] == d_mean:
                f_labels[i, j, k] = "C"

# Imprimir resultado con etiquetas de texto
print("Array f con etiquetas:\n", f_labels)