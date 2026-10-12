lista =["Ana", "Carlos", "Diana"]
print("Lista inicial",lista)

lista.append("Elena")
lista.insert(1, "Beatriz")
print("Lista tras inserciones", lista)

print("Primer alumno:", lista[0])
print("segundo alumno:", lista[2])
print("indice Diana", lista.index("Diana"))
print("Primeros 3:", lista[:3])
print("Subgrupo 1 al 3",lista[1:4])
print("Ultimos dos estudiantes",lista[-2:])
print("Lista totalmente invertida", lista[::-1])