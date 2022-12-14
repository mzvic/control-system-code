from datetime import datetime, timedelta
import serial
import sys

fpga_uart = serial.Serial(port='/dev/ttyUSB1', baudrate=4_000_000)

try:
    interval = timedelta(seconds=int(sys.argv[2]))

except IndexError:
    print("No time given as argument.(python get_apd_count.py <frequency> <time in seconds>)")
    exit()

try:
    frequency = float(sys.argv[1])
    seconds = 1 / frequency

except IndexError:
    print("No frequency given as argument.(python get_apd_count.py <frequency> <time in seconds>)")
    exit()

multiplos = []
a_list = []
b_list = []
for i in range(9):
    multiplos.append(format((seconds)*(i+1), '.6f'))
    a_list.append(int(multiplos[i][5])) # 0.000a00
    b_list.append(int(multiplos[i][6])) # 0.0000b0

with open('timestamp.csv', 'w') as f:
    with open('error.csv', 'w') as f2:
        first_ts = datetime.now()
        while True:
            try:
                ts_b = datetime.now().time().strftime('%H:%M:%S.%f') # 00:00:00.000000
                x = str(ts_b)

                a = int(x[12]) # 0.000a00
                b = int(x[13]) # 0.0000b0
                read_hex = ord(fpga_uart.read())               

                if (a == a_list[0] and b == b_list[0]) or (a == a_list[1] and b == b_list[1]) or (a == a_list[2] and b == b_list[2]) or (a == a_list[3] and b == b_list[3]) or (a == a_list[4] and b == b_list[4]) or (a == a_list[5] and b == b_list[5]) or (a == a_list[6] and b == b_list[6]) or (a == a_list[7] and b == b_list[7]) or (a == a_list[8] and b == b_list[8]): # Multiples of seconds
                    f.write(str(ts_b) + ',' + str(read_hex) + '\n')
                    print(str(ts_b) + ',' + str(read_hex) + '\n')
                    


                if datetime.now() >= first_ts + interval:
                    exit()
                    
                    
            except IndexError:
                f2.write(str(ts_b) + '\n')

                    