# Задача:
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input('Введите номер билета: '))

a = number // 1000
b = number % 1000
num1 = a // 100
num2 = a % 100//10
num3 = a % 10
sum1 = num1 + num2 + num3
print('Сумма первых трех чисел: ',sum1)

num4 = b // 100
num5 = b % 100//10
num6 = b % 10
sum2 = num4 + num5 + num6
print('Сумма последних трех чисел: ',sum2)

print('Результат: ')
if sum1 == sum2:
  print("ВЫИГРЫШ")
else:
  print("ПРОИГРЫШ")