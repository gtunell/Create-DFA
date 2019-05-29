#!/usr/bin/env python3
# Author: Gregory Tunell
# UID: 115065703

import sys

def find_sequences(b, m):

    # initialize variables
    lst = []
    i = 0
    repeating_element = -1

    # continue until we find a repeat element
    while repeating_element < 0:
        x = b ** i
        x = x % m

        # stop if we find a duplicate element and keep track of it
        if x in lst:
            repeating_element = x
        else:
            lst.append(x)
            i += 1
    
    # split the list and return the tuple
    index = lst.index(repeating_element)
    unique = lst[0:index]
    repeating = lst[index:]

    return (unique, repeating)

def compute_table(weights, length_unique, b, m):

    # initialize variables
    w = len(weights)
    d = {}
    repeating_index = 0

    # loop through every weight (0 ≤ j < w)
    for j in range(0, w):

        # keep track once we pass the unique weights
        new_state = -1
        if j + 1 < w: # still doing uniques
            new_state = j + 1
        else: # now we loop over the repeating weights
            new_state = length_unique + repeating_index
            repeating_index += 1

        # for every weight loop through the classifier values (0 ≤ k < m)
        for k in range(0, m):
             
            d[(j, k)] = []
            d_entry = d[(j, k)]
            # enter possible digit entries and its transition (0 ≤ α < b)
            for a in range(0, b):
            
                classifier = (k + (weights[j] * a)) % m
                d_entry.append((new_state, classifier))
                d[(j, k)] = d_entry

    return d      

def print_table(table):
    for key in table.keys():
        print(key, end = " ") 
        print(table[key])

def states_encountered(d, x):

    current_state = (0, 0)
    encountered_states = [current_state]

    for i in x:
        current_state = d[current_state][i]
        encountered_states.append(current_state)

    return encountered_states

def accept_or_reject(sequence, i):

    length = len(sequence)
    _, k = sequence[length - 1]

    return "accept" if k == i else "reject"

def main(argv):

    b = int(argv[0])
    m = int(argv[1])
    i = int(argv[2])
    x = map(int, argv[3:])

    # get answers
    (unique, repeating) = find_sequences(b, m)
    weights = unique + repeating
    length_unique = len(unique)
    table = compute_table(weights, length_unique, b, m)
    encountered_states = states_encountered(table, x)
    result = accept_or_reject(encountered_states, i)

    # print answers
    print(unique)
    print(repeating)
    print_table(table)
    print(len(weights) * m)
    print(encountered_states)
    print(result)


if __name__ == "__main__":
    main(sys.argv[1:])
