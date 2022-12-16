from datetime import datetime, timedelta
import sys

now = datetime.today()
result_2 = now + timedelta(seconds=int(sys.argv[1]))

while True:
    print(datetime.now(), result_2)
    if datetime.now() >= result_2:
        print('STOP')
        break