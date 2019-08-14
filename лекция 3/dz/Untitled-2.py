from collections import Counter

def write(word):
    clear = word.replace(' ','')
    hash = dict(Counter(clear))
    for k,v in hash.items():
        print(f"{k}-{v}")

write(input())