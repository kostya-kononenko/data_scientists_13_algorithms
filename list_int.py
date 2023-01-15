import random
import time


def bubble_sort(old_list):
    is_sorted = False
    temp = 0
    iteration = 0
    while not is_sorted:
        is_sorted = True
        for idx, number in enumerate(old_list):
            if len(old_list) - 1 - iteration == idx:
                continue
            if old_list[idx] > old_list[idx + 1]:
                is_sorted = False
                old_list[idx], old_list[idx + 1] = old_list[idx + 1], old_list[idx]
    return old_list


bubble_sort([random.randint(0, 1000) for i in range(0, 5000)])


def time_calculator(func, tries_count):
    result = 0
    for i in range(0, tries_count):
        start = time.time()
        i = func
        end = time.time()
        result += (end-start)
    return result / tries_count


f = time_calculator(bubble_sort, 10)

print(f'Середній час виконання сортування бульбашками складає:  {f}')
