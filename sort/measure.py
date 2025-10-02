import copy
import random
import matplotlib.pyplot as plt

from bubble1 import bubble1
from bubble2 import bubble2
from insert1 import insert1
from selection1 import selection1


def measure_sorts():
    lists_lens = [n for n in range(10, 50, 10)]

    bubble1_results = []
    bubble2_results = []
    insert1_results = []
    selection1_results = []

    for n in range(10, 50, 10):
        unsorted_list = [random.randint(0, n**2) for i in range(n)]

        bubble1_results.append(bubble1(copy.deepcopy(unsorted_list)))
        bubble2_results.append(bubble2(copy.deepcopy(unsorted_list)))
        insert1_results.append(insert1(copy.deepcopy(unsorted_list)))
        selection1_results.append(selection1(copy.deepcopy(unsorted_list)))

    plt.plot(lists_lens, bubble1_results, label='bubble 1', color = 'blue')
    plt.plot(lists_lens, bubble2_results, label='bubble 2', color = 'red')
    plt.plot(lists_lens, insert1_results, label='insert 1', color = 'green')
    plt.plot(lists_lens, selection1_results, label='selection 1', color = 'brown')


    plt.legend()
    plt.show()

measure_sorts()