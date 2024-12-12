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

test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

def compute_sum(input):
    result = re.findall(r'mul\((\d+),(\d+)\)', input)
    digits = [(int(x), int(y)) for x, y in result]
    final = sum([x * y for x, y in digits])
    return final

if __name__ == "__main__":
    data = get_lists_from_aoc("53616c7465645f5fcaf56c0ba80c36e571e19af439640117102e08c1077e3bfebecfb0f0ffd8212f6c3621362dbabbe2d378de409195c97295a9a7f7fcfd4acf") 
    print(compute_sum(data))