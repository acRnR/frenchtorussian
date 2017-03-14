import re


def stress_sym(word):
# todo: функция которая заменяет большую букву внутри нормального слова(но не аббревиатуры из больших букв) на маленькую со знаком ударения

def bygroups():
# todo: скорее всего придется переделать под новый файл
    with open('vocab.txt', 'r', encoding='UTF-8') as a:
        for line in a:
            if '\t' not in line:
                fname = line + '.txt'
            else:
                with open(fname, 'a', encoding='UTF-8') as b:
                    b.write('line' + '\n')


def byalphabet(fn):
# скорее всего не пригодится
    with open(fn, 'r', encoding='UTF-8') as a:
        arr = a.readlines()
    arr.sort()
    return arr


def make_html_code:
# todo: функция, которая вставит слова из файла в код html-страницы
    pass