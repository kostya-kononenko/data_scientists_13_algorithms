from random_words import RandomWords

my_list = []
w = RandomWords()

for i in range(0, 5000):
    my_list.append(w.random_word())
print(my_list)
