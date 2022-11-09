import random
import numpy as np
from numpy import linalg


y = int(input("Напиши да какие нибудь цифры от 1 до 40 по братский : "))
while (y < 1) or (y > 40):
    y = int(input("Я же тебя предупредил\n Заново брат от 1 до 40:"))

m = np.random.randint(7, size=(y,y))
print("magic:\n", m)

s = np.linalg.matrix_rank(m)
print("\n Ранг:", s)

accuracy = int(input(' Минимальное количество знаков после запятой :'))  
accuracy1 = 0.1 ** accuracy

n = 1
factorial = 1
summa = 0
fg = 0
fraction = 1 
while abs(fraction) > accuracy1:
    fg += summa
    summa += (-(np.linalg.det(linalg.matrix_power(m , 2 * n - 1)))) / factorial
    n += 1
    factorial = factorial * (2*n - 1) * (2*n - 2)
    fraction = abs(fg-summa)  
    fg = 0
    print(n - 1, ':', summa, '   ', fraction)
print('\nСумма знакопеременного ряда:', summa)
print ('Все брат мучать больше не буду.\n Всего хо-ро-ше-го')
