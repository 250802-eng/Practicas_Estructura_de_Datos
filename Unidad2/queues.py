from collections import deque
cola=deque()
#AGREGAR ELEMNTOS A LA COLA (ENCOLAR)
cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")
#SACAR EL PRIMER ELEMENTO QUE LLEGO (DESENCOLAR)
atendido=cola.popleft()
#MOSTRAR RESULTADOS
print("Atendido",atendido)
print("cola restante:", cola)