import math
import requests
# We get a matrix and for each row we need to check that it is either increasing or decreasing monotonically with step size between 1 and 3

def get_lists_from_aoc(cookie):

# You'll need to include your session cookie
    cookies = {
        'session': cookie  # Get this from your browser after logging in
    }

    response = requests.get(
        'https://adventofcode.com/2024/day/2/input',
        cookies=cookies
    )

    list_1 = []

    for line in response.text.strip().split('\n'):
        list_1.append(list(map(int, line.split())))
    return list_1

sample_matrix = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1]]

def check_row(list):
    differences = [i - j for i, j in zip(list, list[1:])]
    increasing = differences[0] < 0
    for i in differences:
        if (increasing and i >= 0) or (not increasing and i <= 0):
            return 0
        if abs(i) < 1 or abs(i) > 3:
            return 0
    return 1

if __name__ == "__main__":
    result = [check_row(i) for i in sample_matrix]
    print(result)
    print("--------- ACTUAL RESULT ----------")
    data = get_lists_from_aoc("") 
    print(sum([check_row(i) for i in data]))
