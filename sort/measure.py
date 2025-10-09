import copy
import random
import matplotlib.pyplot as plt

from bubble1 import bubble1
from bubble2 import bubble2
from bubble3 import bubble3
from bubble4 import bubble4
from insert1 import insert1
from selection1 import selection1
from shell1 import shell1


def measure_sorts():
    lists_lens = [n for n in range(10, 50, 10)]

    bubble1_results = []
    bubble2_results = []
    bubble3_results = []
    bubble4_results = []
    insert1_results = []
    selection1_results = []
    shell1_results = []

    for n in range(10, 50, 10):
        unsorted_list = [random.randint(0, n**2) for i in range(n)]

        bubble1_results.append(bubble1(copy.deepcopy(unsorted_list)))
        bubble2_results.append(bubble2(copy.deepcopy(unsorted_list)))
        bubble3_results.append(bubble3(copy.deepcopy(unsorted_list)))
        bubble4_results.append(bubble4(copy.deepcopy(unsorted_list)))
        insert1_results.append(insert1(copy.deepcopy(unsorted_list)))
        selection1_results.append(selection1(copy.deepcopy(unsorted_list)))
        shell1_results.append(shell1(copy.deepcopy(unsorted_list)))

    plt.plot(lists_lens, bubble1_results, label='bubble 1', color = 'brown')
    plt.plot(lists_lens, bubble2_results, label='bubble 2', color = 'red')
    plt.plot(lists_lens, bubble3_results, label='bubble 3', color = 'orange')
    plt.plot(lists_lens, bubble4_results, label='bubble 4', color = 'yellow')
    plt.plot(lists_lens, insert1_results, label='insert 1', color = 'blue')
    plt.plot(lists_lens, selection1_results, label='selection 1', color = 'green')
    plt.plot(lists_lens, shell1_results, label='shell 1', color = 'purple')


    plt.legend()
    plt.show()

measure_sorts()