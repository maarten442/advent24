import re
import os
from dotenv import load_dotenv

load_dotenv()

test_input = """SSSXSSMSXMMAXXAXMSSMSSMSXMASXXMXMMXMSXSMXMMSASXMMAMMMMMXSAXMAMASMASASXSXMMMSMAXMSAMXAAXXXAMXSAMSAAMMXASXMXXXXASXMMSMMMMMMMSMMSAMSSSMXSMMXSX
MXMAMMMSAAMSSSXSMMMMMAMMMXMMXXAAXMAMMAASMSXMASAXSXMAAXAAAMAMXSXXMASMMAMXMAAAXXMASXSSMXAMSXMAMXXSMXXAMXXAXMSMMMMAAAXXAAAXAAAAXSAMMASXAMXXAMAS"""

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
    print(diagonals)
    # print(re.findall(r'(?=(XMAS|SAMX))', test))