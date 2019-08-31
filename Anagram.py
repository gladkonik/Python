class Counter(dict):
    def __missing__(self, key):
        return 0

def anagram(str1='', str2=''):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    if len(str1) != len(str2):
        return False

    counter = Counter()
    for el in str1:
        counter[el] += 1
    for el in str2:
        counter[el] -= 1
    for el in counter.values():
        if el != 0:
            return False

    return True

print(' ab c'.replace(" ", '').center(5,('_')))
print(anagram('lIsten', 'silent'))