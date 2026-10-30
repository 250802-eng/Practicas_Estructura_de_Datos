import numpy as np
print("**********Matriz Numpy***********")
A = np.array([[10,15],[20,5]])
B = np.array([[5,12],[15,8]])

suma = A + B
print("Total de productos vendidos (Sabado + Domingo):")
print(suma)

print("Ingreso total en pesos (a 50 pesos por producto):")
precio = 50 * suma
print(precio)


print("********Matriz Nativa**************")
MatrizA = ([[10,15],[20,5]])
MatrizB = ([[5,12],[15,8]])

sumar = [[MatrizA[i][j]+MatrizB[i][j]for j in range(len(MatrizA[0]))] for i in range(len(MatrizA))]
print("Total de productos vendidos (Sabado + Domingo):")
print(sumar)

ingreso = [[MatrizA[i][j]* 50 +MatrizB[i][j] * 50 for j in range(len(MatrizA[0]))] for i in range(len(MatrizA))]
print("Ingreso total en pesos (a 50 pesos por producto):")
print(ingreso)
