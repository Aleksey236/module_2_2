print('Введите три целых числа:')
first = int(input(' '))
second = int(input(' '))
third = int(input(' '))
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
else:
    print(0)