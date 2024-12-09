a = [s.upper() for s in "Hello World"]
# print(a)


b = [w.strip(',') for w in ['there,,', 'hi', 'apple,', 'have', 'has,', 'comas,', 'buy']]
# print(b)

sentence = "Beautiful better than ugly"
c = ["".join(sorted(word , key=lambda x: x.lower())) for word in sentence.split()]
# print(c)











