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

def main():
    """Run time code"""



    # create resp, which is our request object
    resp = requests.get(f"http://api.open-notify.org/iss-now.json")   # this "f" string reads: API + "cards/" + setcode
    #resp = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?start_date={startdate}&end_date={enddate}&api_key=XWFii684Yigi9fhGjdFp53vuUr94g6LbafYdUzFV")
    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = resp.json()

#    print(cards)

#    with open("resp_text.txt", "w") as file:
#        file.write(resp.text)

    position = resp.json().get("iss_position")
    lat = position.get("latitude")
    lng = position.get("longitude")


    print("The Current Location of the ISS")
    print(f'Latitude is: {lat}')
    print(f'Longitude is: {lng}')

    

if __name__ == "__main__":
    main()

