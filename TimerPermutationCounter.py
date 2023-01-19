#about this program
#Counts the time taken to calculate how many permutations there are for the input number

import itertools
import time
from datetime import timedelta
from time import process_time
from itertools import permutations

def main():
    while True:
        try:
            #Ask user how many elements are in the list
            arraylength = int(input("Provide the size of the array: "))
            l = []
            for i in range(arraylength):
                l.append(i+1)
            print("Array : ", l)

            # making the list
            X = permutations(l)

            #Start timer
            t1_start = process_time()

            #find number of permutations
            length = sum(1 for ignore in X)
            print(length)

            #Show time it takes for program to run, stop timer
            t1_stop = process_time()
            elapsed = t1_stop-t1_start

            #Print difference between start and stop timer
            print("Elapsed time during whole program: ", (timedelta(seconds=elapsed)), " HH:MM:SS:MMMM")
            break
        except:
            print("Only enter a number\nPlease Retry:")

if __name__ == "__main__":
    main()
