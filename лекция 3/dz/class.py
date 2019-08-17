from collections import Counter

class Text:
        def write(self,word):
                clear = word.replace(' ','')
                hash = dict(Counter(clear))
                for k,v in hash.items():
                        print(f"{k}-{v}")



a = Text()
a.write(input())