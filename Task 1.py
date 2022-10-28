# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = (input('Введите текст: '))
if len(text) == 0:
    text = 'конь лошадь пони жук дом вода свеча бревно бар'
text = text.split(' ')
text = list(filter(lambda x: 'а' not in x, text))
text = list(filter(lambda x: 'б' not in x, text))
text = list(filter(lambda x: 'в' not in x, text))
print(text)
