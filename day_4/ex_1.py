import re

test_input = """SSSXSSMSXMMAXXAXMSSMSSMSXMASXXMXMMXMSXSMXMMSASXMMAMMMMMXSAXMAMASMASASXSXMMMSMAXMSAMXAAXXXAMXSAMSAAMMXASXMXXXXASXMMSMMMMMMMSMMSAMSSSMXSMMXSX
MXMAMMMSAAMSSSXSMMMMMAMMMXMMXXAAXMAMMAASMSXMASAXSXMAAXAAAMAMXSXXMASMMAMXMAAAXXMASXSSMXAMSXMAMXXSMXXAMXXAXMSMMMMAAAXXAAAXAAAAXSAMMASXAMXXAMAS"""

rows = test_input.split("\n")
columns = [''.join(j) for j in (zip(*test_input.split("\n")))]


def find_matches(input):
    match_list = re.findall(r'(?=(XMAS|SAMX))', input)
    return len(match_list)



if __name__ == "__main__":
    print(columns)
    # print(re.findall(r'(?=(XMAS|SAMX))', test))