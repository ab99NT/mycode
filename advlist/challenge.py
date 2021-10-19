#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - making selections from complex lists"""

def main():

    # create a list called list
    icecream= ["flavors", "salty"]

    northerntrust= ["Alex","Andrew","Dave","Julia","Kurt","Marlon","Roger","Seth","Tim","Viq"]

    no=99

    icecream.append(no)

    user_input= int(input("Please enter a number between 0 - 9: "))
    
    # display list1
    print(f"{icecream[2]} {icecream[0]} and {northerntrust[user_input]} chooses to be {icecream[1]}")
    #print(icecream[-1]+ "," + "and " + northerntrust[user_input])
    
main()
