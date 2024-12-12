import requests
# Two lists, we need to pair up numbers, compute the difference and sum them. Input: two lists.

# Helper function


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
list_2 = [14, 13, 12, 11, 10]
# output: 45

def compute_sum(list_1, list_2):
    return sum(abs(i - j) for i, j in zip(sorted(list_1), sorted(list_2)))

if __name__ == "__main__":
    print(f"The answer for the sample is: {compute_sum(list_1, list_2)}\n")
    print(f"---------- Compute the actual answer -----------")
    list1, list2 = get_lists_from_aoc()
    print(f"Answer: {compute_sum(list1, list2)}")