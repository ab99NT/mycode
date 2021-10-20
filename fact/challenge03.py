#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""
def main():

    input_farm = input("Please Input  a farm (NE Farm, W Farm, or SE Farm)\n>")

    if input_farm in ("NE Farm","SE Farm","W Farm"):
        
        farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
                {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
                {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

        animals = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
                {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
                {"name": "SE Farm", "agriculture": ["chickens"]}]



        for x in farms:
             a=(x.get("name"))
             if a == input_farm:
                 for y in animals:
                     b=(y.get("name"))
                     if b == input_farm:
                         for c in b.get("agriculture"):
                             print(c)
    else:
        print("Invalid Farm")
main()
