import re
import os
from dotenv import load_dotenv

load_dotenv()

test_input = """
SSSXSSMSXMMAXXAXMSSMSSMSXMASXXMXMMXMSXSMXMMSASXMMAMMMMMXSAXMAMASMASASXSXMMMSMAXMSAMXAAXXXAMXSAMSAAMMXASXMXXXXASXMMSMMMMMMMSMMSAMSSSMXSMMXSX
MXMAMMMSAAMSSSXSMMMMMAMMMXMMXXAAXMAMMAASMSXMASAXSXMAAXAAAMAMXSXXMASMMAMXMAAAXXMASXSSMXAMSXMAMXXSMXXAMXXAXMSMMMMAAAXXAAAXAAAAXSAMMASXAMXXAMAS
"""
# test_dim = 10 x 2
# (0, 0), (1, 1), (2, 2)
# (1, 0), (2, 1)

# A B C
# D E F
# G H I

test_string = "ABC\nDEF\nGHI"

rows = test_input.split("\n")
columns = [''.join(j) for j in (zip(*test_input.split("\n")))]
diagonals = []

test1 = "ABCD"
test2 = "EFGH"
test3 = "IJKL"

diagonals = []

def find_matches(input):
    match_list = re.findall(r'(?=(XMAS|SAMX))', input)
    return len(match_list)

if __name__ == "__main__":
    # print(columns)
    print(os.environ.get("cookie"))
    print(test_string.split("\n"))
    print(list(zip(*[row[idx:] for idx, row in enumerate(test_string.split("\n"))])))
    # print(re.findall(r'(?=(XMAS|SAMX))', test))