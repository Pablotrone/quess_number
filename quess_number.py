from random import randint
number = randint(1, 100)
print('Угадайте чисто от 1 до 100')
while True:
    quess = int(input('Введите чисто: '))
    if quess < number:
        print('Ваше чисто меньше того, что загадано.')
    if quess > number:
        print('Ваше число больше того, что загадано.')
    if quess == number:
        break
print('Отличная интуиция! Вы угадали число :)')         