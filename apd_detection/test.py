import sys

hertz = float(sys.argv[1])
multiplos = []
a_list = []
b_list = []
for i in range(9):
    multiplos.append(format((1/hertz)*(i+1), '.6f'))
    a_list.append(int(multiplos[i][5])) # 0.000a00
    b_list.append(int(multiplos[i][6])) # 0.0000b0

print(a_list)
print(b_list)
print(multiplos)