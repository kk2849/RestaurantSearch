# Overview

Name: Kevin Kim
Date: December 2021

# Assignment Details

Made with Python 3.8.10 and VS Code

## How to run

1. Place `restaurants.csv` and `cusines.csv` in the same folder as the project.
2. Run RestaurantSearch.py with Python 3.

## Assumptions

1. Data from csv files would be read and stored in a SQL database or similar.  For this demo, we store the data in memory when the program runs.
2. Csv data will not overflow memory when reading and storing.
3. Restaurant name is case insensitive, i.e. "Mcd" and "mcd" are the same when searching.
4. Customer Rating, Distance, and Price are Integers for convenience and within the ranges given
5. Assuming no invalid input (EX: no cusine input that does not exist in csv)
6. Priority order: Distance, Rating, Price, Name/Cusine

## Future considerations

1. Input sanitation
2. Database implementation
3. API development
4. GPS Location data