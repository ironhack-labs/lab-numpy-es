import numpy as np

# 2. Imprime la versión de NUMPY y la configuración.
print(np.__version__)
print(np.show_config())

# 3. Genera un array tridimensional de 2x3x5 con valores aleatorios.
a = np.random.random((2,3,5))

# 4. Imprime a.
print(a)

# 5. Crea un array tridimensional de 5x2x3 con todos los valores igual a 1.
b = np.ones((5,2,3))

# 6. Imprime b.
print(b)

# 7. ¿Tienen a y b el mismo tamaño?
print(a.size == b.size)

# 8. ¿Es posible sumar a y b?
# No, porque tienen diferentes formas (shapes).

# 9. Transpone b para que tenga la misma estructura que a.
c = b.transpose(1, 2, 0)

# 10. Suma a y c.
d = a + c

# 11. Imprime a y d.
print(a)
print(d)

# 12. Multiplica a y c.
e = a * c

# 13. ¿Es e igual a a?
print(np.array_equal(e, a))  # Sí, porque multiplicar por 1 no cambia los valores.

# 14. Identifica los valores máximos, mínimos y medios en d.
d_max = d.max()
d_min = d.min()
d_mean = d.mean()

# 15. Crea un array vacío con la misma forma que d.
f = np.empty(d.shape)

# 16. Rellena los valores en f según las condiciones dadas.
f[(d > d_min) & (d < d_mean)] = 25
f[(d > d_mean) & (d < d_max)] = 75
f[d == d_mean] = 50
f[d == d_min] = 0
f[d == d_max] = 100

# 17. Imprime d y f.
print(d)
print(f)

# 18. Usa valores de cadena en lugar de números.
f_str = np.empty(d.shape, dtype=str)
f_str[(d > d_min) & (d < d_mean)] = 'B'
f_str[(d > d_mean) & (d < d_max)] = 'D'
f_str[d == d_mean] = 'C'
f_str[d == d_min] = 'A'
f_str[d == d_max] = 'E'

# Imprime f_str
print(f_str)
