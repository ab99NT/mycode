#!/usr/bin/env python3

def main():

    # Program to return a capital for the given country input

    usr_country = input("Please enter a country to find it's capital:\n>")

    count = 0

    while count < 3:
       if usr_country == "":
           usr_country = input("Please enter a country to find it's capital:")

           count = count + 1
       else:

           count = 4


    # Generate a dictionary from country list file.
           countries = {}

           try:
               country_data = open('countries.txt', 'r')

#        print("made it here")
           except IOError:
               print("Country list file could not be opened.")
               quit(
                       )
           try:
               for each_line in country_data:
                   (country_name, capital_city) = each_line.split(':', 1)
                   country_name = country_name.strip()
                   capital_city = capital_city.strip()
                   countries[country_name] = capital_city  # "Japan": "Tokyo"
               country_data.close()
#        print( countries.values() )

           except ValueError:
               pass

#        print( countries.keys() )
           print(f"The capital City of {usr_country} is {countries.get(usr_country)}" )

main()
