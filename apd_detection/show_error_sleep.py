import time
import sys
import matplotlib.pyplot as plt

resultados = []

while len(resultados) <= int(sys.argv[2]):
    
    start = time.time() # Tiempo inicial
    time.sleep(float(sys.argv[1])) # Tiempo de espera
    resultados.append(time.time() - start) # Tiempo inicial - Tiempo final

plt.plot(resultados, label = "(Tiempo Inicial - Tiempo Final) REAL")
plt.xlabel('Muestras')
plt.ylabel('Tiempo')
plt.title('Error de tiempo de espera ({})'.format(sys.argv[1]))
plt.axhline(y=float(sys.argv[1]), color = 'red', label = "(Tiempo Inicial - Tiempo Final) ESPERADO")
plt.legend()
plt.show()
