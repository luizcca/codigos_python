import time
dx = 0.01
y = 0
x = 0
area = 0
total = 0
while x >= 0 and x <= 3:
    y = (x * x)
    #time.sleep(0.5)
    area = area + (y * dx)
    x = x + dx
    #time.sleep(0.5)
    print('total= %f'%total)
