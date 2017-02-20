
def bygroups():
    with open('vocab.txt', 'r', encoding='UTF-8') as a:
        for line in a:
            if '\t' not in line:
                fname = line + '.txt'
            else:
                with open(fname, 'a', encoding='UTF-8') as b:
                    b.write('line' + '\n')


def byalphabet(fn):
    with open(fn, 'r', encoding='UTF-8') as a:
        arr = a.readlines()
    arr.sort()
    return arr


def make_html_code:
    pass