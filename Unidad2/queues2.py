from collections import deque
import time
cola_reproduccion=deque()
#El usuario agrega canciones 
cola_reproduccion.append("1.antologia")
cola_reproduccion.append("2.historia de amor")
cola_reproduccion.append("3.historia entre tus dedos")
#Mostrar las canciones en espera
print("Canciones en espera:")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("Iniciando reproduccion")
    #El reproductor procesa la cola cancion por cancion (desencolar)
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora{cancion_actual}")
    time.sleep(1) #simula la duraccion del tema
    print(f"finalizo:{cancion_actual}")
    #Muestra cuantas canciones quedan en la cola
    print(f"Quedan{len(cola_reproduccion)}) canciones en la cola)")
    print("La cola de reproduccion ha terminado.")
