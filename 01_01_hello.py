# program hello_username
"""
Напишите программу, которая приветствует пользователя, выводя слово Hello,
введенное имя и знаки препинания по образцу (см. пример входных и выходных
данных). Программа должна считывать в строковую переменную значение и писать
соответствующее приветствие. Обратите внимание, что после запятой должен
обязательно стоять пробел, а перед восклицательным знаком пробела нет.
Операцией конкатенации строк (+) пользоваться нельзя.

Hello, [username]!
"""

username = input()
print('Hello, ', username, '!', sep='')
