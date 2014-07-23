import sys 
import numpy as np


def main():
    script = sys.argv[0]
    shuffled_results_file = sys.argv[1]
    real_results_file = sys.argv[2]

    process(shuffled_results_file, real_results_file)


def process(shuffled_results_file, real_results_file):
    shuffled_data = np.loadtxt(shuffled_results_file)
    real_data = np.loadtxt(real_results_file)

    print 'Real data:'
    print real_data
    print
    print 'Shuffled data:'
    print shuffled_data

main()

