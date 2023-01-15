import random

my_list = []

for i in range(0, 5000):
    my_list.append(random.uniform(0.1, 100.0))
print(sorted(my_list))
