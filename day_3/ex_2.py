import re
import requests

def get_lists_from_aoc(cookie):

# You'll need to include your session cookie
    cookies = {
        'session': cookie  # Get this from your browser after logging in
    }

    response = requests.get(
        'https://adventofcode.com/2024/day/3/input',
        cookies=cookies
    )

    return response.text.strip()

test_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def find_counting_mul(input):
    result = re.findall(r'do\(\)|don\'t\(\)|mul\(\d+,\d+\)', input)
    flag = 1
    counts = []
    for i in result:
        if "mul" in i and flag:
            counts.append(i)
        if "don't" in i:
            flag = 0
        if "do()" in i:
            flag = 1
    print(counts)
    return counts

def find_sum(input):
    result = [int(x) * int(y) for s in input for x, y in re.findall(r'mul\((\d+),(\d+)\)', s)]
    return sum(result)

if __name__ == "__main__":
    data = get_lists_from_aoc("53616c7465645f5fcaf56c0ba80c36e571e19af439640117102e08c1077e3bfebecfb0f0ffd8212f6c3621362dbabbe2d378de409195c97295a9a7f7fcfd4acf") 
    print(find_sum(find_counting_mul(data)))