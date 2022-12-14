import sys
hertz = float(sys.argv[1])
sec = 1/hertz

                                            # TO DO: Probar diferentes frecuencias 
multiplos = []
for i in range(1, 10):
   multiplos.append(format(sec*i, '.6f'))

print(multiplos)
a_list = []
b_list = []

for i in range(len(multiplos)):
    a_list.append(int(multiplos[i][5]))
    b_list.append(int(multiplos[i][6]))

print(a_list)
print(b_list)

from datetime import datetime
import serial
fpga_uart = serial.Serial(port='/dev/ttyUSB1', baudrate=4_000_000)

with open('timestamp.csv', 'w') as f:
    with open('error.csv', 'w') as f2:
        while True:
            try:
                ts_b = datetime.now().time().strftime('%H:%M:%S.%f') # 00:00:00.000000
                x = str(ts_b)

                a = int(x[12]) # 0.000a00
                b = int(x[13]) # 0.0000b0
                read_hex = ord(fpga_uart.read())
                
                if (a == a_list[0] and b == b_list[0]) or (a == a_list[1] and b == b_list[1]) or (a == a_list[2] and b == b_list[2]) or (a == a_list[3] and b == b_list[3]) or (a == a_list[4] and b == b_list[4]) or (a == a_list[5] and b == b_list[5]) or (a == a_list[6] and b == b_list[6]) or (a == a_list[7] and b == b_list[7]) or (a == a_list[8] and b == b_list[8]): # Multiplos de 0.000<25>0
                    f.write(str(ts_b) + ',' + str(read_hex) + '\n')
                    print(str(ts_b) + ',' + str(read_hex) + '\n')
                    
            except IndexError:
                f2.write(str(ts_b) + '\n')