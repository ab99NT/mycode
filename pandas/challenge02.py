#!/usr/bin/env python3

import pandas

def main():

    # create a dataframe from json
    df = pandas.read_json("5movies.json")

    sorted_by_gross = df.sort_values(["IMDB Score"], ascending=False)

    # writeout dataframe to CSV
    sorted_by_gross.to_excel("5movies-translated-from-json-and-sorted-by-IMDB-Score.xlsx")

if __name__ == "__main__":
    main()

