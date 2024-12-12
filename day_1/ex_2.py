from collections import Counter
import requests
# Two lists, we need to pair up numbers, compute the difference and sum them. This time we want to compute the similarity score. 

def get_lists_from_aoc(cookie):
# You'll need to include your session cookie
    cookies = {
        'session': cookie  # Get this from your browser after logging in
    }

    response = requests.get(
        'https://adventofcode.com/2024/day/1/input',
        cookies=cookies
    )

    list_1 = []
    list_2 = []

    for line in response.text.strip().split('\n'):
        num1, num2 = map(int, line.split())
        list_1.append(num1)
        list_2.append(num2)

    return list_1, list_2

# Example:
list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [3, 3, 4, 4, 4, 5]

# 1 appears 0 times in list_2
# 2 appears 0 times in list_2
# 3 appears 2 times in list_2: score += 3*2
# 4 appears 3 times in list_2: score += 4*3
# 5 appears 1 time in list_2: score += 5*1

def compute_similarity(list_1, list_2):
    counter = Counter(list_2)
    return sum(i * counter[i] for i in list_1)

if __name__ == "__main__":
    print(f"The answer for the sample is: {compute_similarity(list_1, list_2)}\n")
    print(f"---------- Compute the actual answer -----------")
    list1, list2 = get_lists_from_aoc("")
    print(f"Answer: {compute_similarity(list1, list2)}")