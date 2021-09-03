import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    b = bin(n)[2:]
    b = b.split('0')
    print(len(max(b)))