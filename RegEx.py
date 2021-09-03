import math
import os
import random
import re
import sys



if __name__ == '__main__':
    name_list=[]
    N = int(input().strip())

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if emailID[-10:]=='@gmail.com':
            name_list.append(firstName)
    for e in sorted(name_list):
        print(e) 