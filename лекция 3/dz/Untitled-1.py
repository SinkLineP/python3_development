from collections import Counter

def write(word):
    small = 
    clear = word.replace(' ','')
    c = dict(Counter(clear))
    for x,y in c.items():
        print(f"{x} - {y}")

write(input("Enter your text: "))