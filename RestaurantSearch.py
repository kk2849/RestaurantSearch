import csv
from typing import List, Optional, Tuple

def search_restaurants(restaurants: List[Tuple[str,int,int,int,int]], 
                        cusines: dict, 
                        name: Optional[str]="", 
                        rating: Optional[int]=0, 
                        distance: Optional[int]=0, 
                        price: Optional[int]=0, 
                        cusine: Optional[str]="") -> List[Tuple[str,int,int,int,int]]:
    """Function to find up to 5 best matching restaurants based on the provided criteria

    Args:
        restaurants: restaurants from csv
        cusines: cusines from csv
        name: string representing name
        rating: int representing rating, expected values from 1-5
        distance: int representing distance, expected values from 1-10
        price: int representing price, expected values from 10-50
        cusine: int representing cusine_id

    Returns:
        List[Tuple[str,int,int,int,int]]: List of up to 5 best matching restaurants
    """

    # Build a new List in sorted order of best match
    best_match_list = []

    for restaurant in restaurants:
        length_best_match_list = len(best_match_list)
        index_to_insert = length_best_match_list # init to index of last element of list

        # Filter by name and cusine if present
        if name:
            if not name.lower() in restaurant[0].lower():
                continue # No match, do not add

        if cusine:
            matching_cusine_id = 0
            for key,value in cusines.items():
                if cusine.lower() in key.lower():
                    matching_cusine_id = value
                    break

            if not matching_cusine_id == restaurant[4]:
                continue # No match, do not add

        # Distance is priority 1, lower is better
        if distance:
            idx = 0
            if restaurant[2] > distance:
                continue
            while idx < length_best_match_list:
                if best_match_list[idx][2] <= restaurant[2]:
                    idx += 1
                else:
                    if idx < index_to_insert:
                        index_to_insert = idx
                        break
            # If we reach here then it is the highest distance restaurant

        # Rating is priority 2, higher is better
        if rating:
            idx = 0
            if restaurant[1] < rating:
                continue
            while idx < length_best_match_list:
                if best_match_list[idx][1] >= restaurant[1]:
                    idx += 1
                else:
                    if idx < index_to_insert:
                        index_to_insert = idx
                        break
            # If we reach here then it is the lowest rated restaurant

        # Price is priority 3, lower is better
        if price:
            idx = 0
            if restaurant[3] > price:
                continue
            while idx < length_best_match_list:
                if best_match_list[idx][3] <= restaurant[3]:
                    idx += 1
                else:
                    if idx < index_to_insert:
                        index_to_insert = idx
                        break
            # If we reach here there it is the highest priced restaurant

        # Add sorted restaurant to list
        best_match_list.insert(index_to_insert, restaurant)

    return best_match_list[0:5]

def read_restaurant_info_from_csv(filepath: str) -> List[Tuple[str,int,int,int,int]]:
    """Function to read in a csv containing restaurant data.
    
    Note: Based on Assumption 1, this function would store into the DB if we were using one.
    For this demo, we will just store it into a dict.

    Args:
        filepath (str): Location of the restaurants csv (should be same as project root)

    Returns:
        List[Tuple[]]: Contains restaurant info
    """
    restaurants = []
    with open(filepath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            if "name" in row: # HACK to avoid first row
                continue
            if len(row) == 5:
                restaurants.append(([row[0],int(row[1]),int(row[2]),int(row[3]),int(row[4])]))
    
    return restaurants


def read_cusine_info_from_csv(filepath: str) -> dict:
    """Function to read in a csv containing cusine data.
    
    Note: Based on Assumption 1, this function would store into the DB if we were using one.
    For this demo, we will just store it into a dict.

    Args:
        filepath (str): Location of the restaurants csv (should be same as project root)

    Returns:
        dict: Contains restaurant info
    """
    cusines = {}
    with open(filepath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in csvreader:
            if "id" in row: # HACK to avoid first row
                continue
            if len(row) == 2:
                cusines[row[1]] = int(row[0]) # row[0] has id, row[1] has cusine
    
    return cusines

if __name__ == '__main__':
    print("--------------------------------")
    print("|      Restaurant Search       |")
    print("--------------------------------")
    print("v0.1")

    restaurants = read_restaurant_info_from_csv('restaurants.csv')
    print('Loaded restaurants')

    cusines = read_cusine_info_from_csv('cusines.csv')
    print('Loaded cusines')

    print("Enter help or h for help")
    print("Enter quit or q to exit")

    while True:
        try:
            user_string = input("Enter comma separated search for restaurant\n")

            if user_string == 'help' or user_string == 'h':
                print("Input: Restaurant Name (str), Customer Rating (int), Distance (int), Price (int), Cusine (str)")
                print("Example: grill,,,,chinese\n")
            elif user_string == 'quit' or user_string == 'q':
                print("Shutting down...Thank you and have a nice day! :o)")
                exit(0)
            else:
                user_inputs = user_string.split(',')
                num_inputs = len(user_inputs)

                if num_inputs < 5:
                    print("Error: Check input format and try again")
                else:
                    print("\nResults:\n")
                    print(search_restaurants(restaurants, 
                                        cusines, 
                                        user_inputs[0], 
                                        int(user_inputs[1]) if user_inputs[1] else 0,
                                        int(user_inputs[2]) if user_inputs[2] else 0, 
                                        int(user_inputs[3]) if user_inputs[3] else 0,
                                        user_inputs[4], 
                                        ))
                    print("\n")
        except Exception as error:
            # TODO - would normally check for each Error and avoid this but we are assuming no issues with input for now
            print("Unknown Error! Please check input and try again")