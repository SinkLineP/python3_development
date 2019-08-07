while True:

	b = input('Введите текст: ')
	z = b.lower()
	w = z.replace(" ", "")
	l = "".join(w for w in w if w not in ('!','.',':',',','?',';','-','_','|'))
	w = l
	s = w
	list(s)
	a = "".join(s[::-1])

	p = ('stop')
	if b == p:
		exit()

	if s == a:
	  print("Ваш текст является полиндромом!")
	else:
	  print("Ваш текст не является полиндромом!")
