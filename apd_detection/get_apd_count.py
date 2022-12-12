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
                
                if (a == 0 and b == 0) or (a == 2 and b == 5) or (a == 5 and b == 0) or (a == 7 and b == 5): # Multiplos de 0.000<25>0
                    f.write(str(ts_b) + ',' + str(read_hex) + '\n')
                    print(str(ts_b) + ',' + str(read_hex) + '\n')
                    
            except IndexError:
                f2.write(str(ts_b) + '\n')
                    