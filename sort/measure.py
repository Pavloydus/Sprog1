import copy
import random
import matplotlib.pyplot as pit

from bubble1 import bubble1
from bubble2 import bubble2

def measure_sorts():
    lists_lens = [n for n in range(10, 50, 10)]

    bubble1_results = []
    bubble2_results = []