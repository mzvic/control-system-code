
def delete(line, line2, file):
    # get rid of the comma
    line_not_comma = line.split(',')[0] # 00:00:00.000000
    line2_not_comma = line2.split(',')[0] # 00:00:00.000000
    # assign a variable to the last 3 miliseconds of line
    line_1 = "0." + line_not_comma[-4:] # 0.000000
    # assign a variable to the last 3 miliseconds of line2
    line_2 = "0." + line2_not_comma[-4:] # 0.000000
    # if the difference between the two lines is less than 0.0010, delete the line2
    if float(line_2) - float(line_1) < 0.0010: 
        #delete line2
        print(str(float(line_2) - float(line_1)))
        file.seek(0)
        lines = file.readlines()
        file.seek(0)
        for i in lines:
            if i != line2:
                file.write(i)
        file.truncate()


    
with open('timestamp.csv', 'r+') as f:
    linesa = f.readlines()
    for i in range(len(linesa)-1):
        try:
            delete(linesa[i], linesa[i+1], f)
        except IndexError:
            pass