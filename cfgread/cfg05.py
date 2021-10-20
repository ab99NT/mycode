#!/usr/bin/env python3
## create file object in "r"ead mode
user_input = input("please enter name of file to load:\n>")

with open(user_input, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    num_lines = sum(1 for line in configfile)
    print('Total lines:', num_lines)
#    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
#print(configlist)

