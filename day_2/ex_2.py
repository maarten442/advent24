import math
import requests
from dotenv import load_dotenv

load_dotenv()

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

sample_matrix = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [8, 4, 7, 6, 4]]

def check_row(list):
    differences = [i - j for i, j in zip(list, list[1:])]
    # Need to check this in a different manner 
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
    data = get_lists_from_aoc("53616c7465645f5fcaf56c0ba80c36e571e19af439640117102e08c1077e3bfebecfb0f0ffd8212f6c3621362dbabbe2d378de409195c97295a9a7f7fcfd4acf") 
    print(sum([check_row(i) for i in data]))
