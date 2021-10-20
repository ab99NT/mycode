#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""
def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for x in farms:    
             a=(x.get("name"))
             if a == "NE Farm":
                 for y in x.get("agriculture"):
                     print(y)

main()
