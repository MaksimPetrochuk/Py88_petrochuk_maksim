some_polydrome = ('qwewq', 'radar', 'sfg', 'fdgw', 'sikis')


def polydrom_check(word):
    if word == word[:: -1]:
        return word


res = tuple(filter(polydrom_check, some_polydrome))
print(res)
