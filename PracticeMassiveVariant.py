# В Python v.3 для строк используется кодировка Unicode.
# Следует помнить, в Python, в отличие от многих других языков программирования, нет такого типа данных как одиночный символ. В Python любой символ - это строка, длина которой равна единице.
phrase = str(input('Введите сообщение которое нужно зашифровать(на русском) = '))
key = int(input('Введите число-ключ = '))
kluch = []  # преобразуем число в список,где элементы списка есть цифры числа
phrase = list(
    phrase)  # переводим строки в списки,таким образом мы сможем полноценно работать с каждым элементом кодового слова или сообщения
space = 0;
flag = 0;
while (key > 0):  # Превращаем в список ключ
    kluch.insert(0, key % 10)
    key = key // 10
A = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
     'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
B = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
     'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
for i in range(0, len(phrase)):
    if ord(phrase[i]) == 32:
        space = space + 1  # Считаем кол-во пробелов сначала
for i in range(0, space):  # удаляем пробелы
    phrase.remove(' ')
gruppa = int(input('Введите длину для равных групп,на которые хотите разбить число = '))
while (flag == 0):
    # print(phrase)
    # n2=len(phrase)
    if (len(phrase) % gruppa == 0):
        flag = 1;
        break;
    gruppa = (int(input('Невозможно разбить на равные группы,введите ещё раз  = ')))
    # print(razdel,n2%i==0)
n1 = 0  # Счётчик,показывает куда надо вставлять пробелы
space = 0
# print(razdel)
for i in range(0, len(phrase) + len(
        phrase) // gruppa - 1):  # сначала разобъём сообщение на слова,каждое длиной в кодовое слово
    if n1 >= gruppa:
        phrase.insert(i, " ")
        space = space + 1
        n1 = 0
        continue
    n1 = n1 + 1
n1 = 0
print(phrase)
for i in range(0, len(phrase)):
    if n1 >= len(kluch):
        n1 = 0
    if ord(phrase[i]) == 32:  # кодировка пробела в таблице Unicode
        continue
    # print(n1,"Сдвиг = ",kluch[n1])
    if ('а' <= phrase[i] <= 'я' or phrase[i] == 'ё'):
        for j in range(0, len(A)):
            if ord(phrase[i]) == ord(A[j]):
                phrase[i] = A[j + kluch[
                    n1] - 33]  # одной из особенностью питона можно назвать то,что списки(массивы)могут иметь отрицательный индекс
                break;
            # print(ord(phrase[i]),ord(A[j]),ord(phrase[i])==ord(A[j]))
    if ('А' <= phrase[i] <= 'Я' or phrase[i] == 'Ё'):
        for j in range(0, len(B)):
            if ord(phrase[i]) == ord(B[j]):
                phrase[i] = B[j + kluch[
                    n1] - 33]  # одной из особенностью питона можно назвать то,что списки(массивы)могут иметь отрицательный индекс
                break;
            # print(ord(phrase[i]),ord(B[j]),ord(phrase[i])==ord(B[j]))
    n1 = n1 + 1
print(''.join(phrase))
