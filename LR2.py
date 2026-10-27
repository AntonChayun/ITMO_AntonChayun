from csv import reader
from datetime import datetime
import os



#Количество книг с >30 символов в названии
def count_sym():
    with open('books.csv', 'r') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        table = table[1:]
        count = 0
        for row in table:
            name_lenght = len(row[1])
            if name_lenght > 30:
                count += 1
        print(f'Количество записей, у которых в поле "Название" строка длиннее 30 символов: {count}')
        return table
count_sym()


#Поиск по автору (книги от 200р)
def find_string(searchline, string):
    string = string.lower()
    index = string.find(searchline.lower())
    return index

def search(table):
    searchline = input('Введите Автора: ')
    if searchline in ['']:#проверка на пустой ввод
        return 0
    elif searchline.isalpha() == False:#проверка на буквенный ввод
        return 0
    flag =0
    for row in table:
        if find_string(searchline, row[4]) != -1 and float(row[7]) >= 200 :
            print(row[4])
            print(f'Произведение "{row[1]}"\n')
            flag +=1

    if flag == 0:
        print('Ничего не найдено!')
    else:
        print(f'Найдено произведений: {flag}')

with open('books.csv', 'r') as csvfile:
    table = list(reader(csvfile, delimiter=';'))
    table = table[1:]
    search(table)


#Новый файл
chosen_str = list(table[1:21])
def create_file():
    txtfile = open('20_strings.txt', 'w', encoding='utf-8')
    str_count = 0
    for stripe in chosen_str:
        author = stripe[4]
        title = stripe[1]
        year = stripe[6]
        str_count +=1

        line = f"{str_count}. {author}. {title} - {year}\n" 
        txtfile.write(line)
    print("Создан файл '20_strings.txt'")
    txtfile.close()
create_file()


#xml
import xml.dom.minidom as minidom


xml_file = open('currency.xml', 'r', encoding='Windows-1251')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
NumCodes = []
CharCodes = []

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:# проверка на элементный узел (<>)
            if child.tagName == 'NumCode':
                if child.firstChild.nodeType == 3:#проверка на текстовый узел
                    NumCode = child.firstChild.data
            if child.tagName == 'CharCode':
                if child.firstChild.nodeType == 3:
                    CharCode = child.firstChild.data
    NumCodes.append(NumCode)
    CharCodes.append(CharCode)


print(f'NumCodes: {NumCodes}')
print(f'CharCodes: {CharCodes}')


xml_file.close()

#доп

# Теги
Tags=[]
with open('books.csv', 'r') as csvfile:
    table = list(reader(csvfile, delimiter=';'))
    table = table[1:]
    for new_row in table:
        parts = new_row[12].split("#")
        for i in parts:
            i = i.lstrip()#удаление пробела в начале строки
            if i!= '' and not i in Tags:
                Tags.append(i)

print(Tags)

#Популярные

with open('books.csv', 'r') as csvfile:
    table = list(reader(csvfile, delimiter=';'))
    table = table[1:]
    max_dow = []
    for strip in table:
        num_pop_book = int(strip[8])
        name_pop_book = strip[1]
        max_dow.append((num_pop_book,name_pop_book))
    max_dow_sorted = sorted(max_dow, reverse=True)[:20]
    print('20 самых популярнх книг:')
    iter =0
    for (pop, name) in max_dow_sorted:
        iter += 1
        print(f'{iter}. {name} - кол-во копий: {pop}')