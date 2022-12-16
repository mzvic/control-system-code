import matplotlib.pyplot as plt
from datetime import datetime, timedelta
#print only one row

restas = []
c = 0
with open('timestamp.csv', 'r') as f:
    data = f.read().splitlines()
    try:
        for i in range(len(data)):
            #substract the first timestamp with the next one
            resta = datetime.strptime(data[i+1].split(',')[0], '%H:%M:%S.%f') - datetime.strptime(data[i].split(',')[0], '%H:%M:%S.%f') 
            restas.append(int(str(resta)[8:15]))
            if restas[i] > 255:
                print(restas[i], " MAYOR")
                c += 1
            if restas[i] < 244:
                print(restas[i], " MENOR")
                c += 1
            
            
            

    except IndexError:
        pass
    
plt.plot(restas)
#plot straight line in y = 250
plt.axhline(y=250, color='r', linestyle='dotted')
print(c)
plt.show()
        