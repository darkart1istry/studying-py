from random import *
#списки со всеми возможными символами
dgts = '0123456789'
lwrcase = 'abcdefghijklmnopqrstuvwxyz'
uprcase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
pnctn = '!#$%&*+-=?@^_'
symb = 'il1Lo0O'
chars = ''

#ввод пользовательских данных, проверка на необходимость включения определенных символов
colv = int(input('Сколько паролей вам нужно сгенерировать? '))
length = int(input('Какой длины должен быть пароль? '))
dgt = input('Включать ли в пароль цифры от 0 до 9? (+/-): ')
if dgt == '+':
    chars += dgts
upr = input('Включать ли в пароль прописные буквы? (+/-): ')
if upr == '+':
    chars += uprcase
lwr = input('Включать ли в пароль строчные буквы? (+/-): ')
if lwr == '+':
    chars += lwrcase
passpnctn = input('Включать ли в пароль символы "!#$%&*+-=?@^_"? (+/-): ')
if passpnctn == '+':
    chars += pnctn
passsymb = input('Исключать ли неоднозначные символы "il1Lo0O"? (+/-): ')
if passsymb == '-':
    chars += symb
elif passsymb == '+':
    chars = chars.replace('i', '')
    chars = chars.replace('l', '')
    chars = chars.replace('1', '')
    chars = chars.replace('L', '')
    chars = chars.replace('o', '')
    chars = chars.replace('0', '')
    chars = chars.replace('O', '')

#функция генерации пароля
def generate_password(c, l):
    for i in range(c):
        password = ''.join(choice(chars) for _ in range(l))
        print(f'Пароль {i+1}: {password}')

generate_password(colv, length)
