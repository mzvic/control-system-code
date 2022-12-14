# Sistema de Control de Cosmic Dust Experiment

## Carpetas

### "apd_detection"
En esta carpeta hay diversos scripts de Python.
- "get_apd_count.py", permite leer la salida de la FPGA cada frecuencia y por el tiempo deseado, arroja dos archivos "timestamp.csv" y "error.csv", **necesita de dos argumentos, la frecuencia y el tiempo** (ESTADO: Finalizado).
- "graph.py", permite graficar el archivo "timestamp.csv" (ESTADO: No Finalizado, queda por hacer una lectura más legible).

- "hertz_to_sec.py", permite leer la salida de la FPGA con Hz a elección del usuario, arroja dos archivos "timestamp.csv" y "error.csv" (ESTADO: No Finalizado, queda por probar diversos kHz y hacer un test con la FPGA).

El archivo "timestamp.csv" contiene el tiempo de lectura (cada 4kHz en este caso) seguido de la lectura de la FPGA (0-127).
El archivo "error.csv" contiene el tiempo en el que pudo haber ocurrido un error.

### "ice-rigol"

### "interfaz gráfica"

## Archivos

El archivo "fpga_compiled.bit" corresponde al código con el que la FPGA se programa, a través del puerto IO33 se lee desde 0 a 3.3V y arroja un valor con una resolución de 0 hasta 127 (dependiendo del voltaje ???).

## **NOTA: El archivo get_apd_count.py puede fallar debido al puerto asignado en la lectura serial, se recomienda cambiarlo dependiendo del puerto que ocupes en el computador (COMx a /dev/ttyUSBx)**
