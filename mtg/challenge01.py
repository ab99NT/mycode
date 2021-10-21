#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests


# Define our "base" API
API = "https://api.nasa.gov/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    startdate = input("What is the startdate?")  # collect user input for MTG card set to lookup
    
    enddate = input("What is the endate)?")


    # create resp, which is our request object
    resp = requests.get(f"{API}neo/rest/v1/feed/?start_date={startdate}&end_date={enddate}&api_key=XWFii684Yigi9fhGjdFp53vuUr94g6LbafYdUzFV")   # this "f" string reads: API + "cards/" + setcode
    #resp = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={startdate}&end_date={enddate}&api_key=XWFii684Yigi9fhGjdFp53vuUr94g6LbafYdUzFV")
    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()

    with open("resp_text.txt", "w") as file:
        file.write(resp.text)

    #print(cards)



if __name__ == "__main__":
    main()

