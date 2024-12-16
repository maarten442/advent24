from itertools import groupby, product, combinations

test_string = """................................y.................
............9.....Q................y..............
..................................................
..................................................
..........Q.......................x..N..1.........
.....9......6.e......................x.......j....
............e..x6Q9...............................
...........6..................................j...
...e....................................j.........
.............Q8.......................x..1........
.....w.......8...................y................
..n.......................y...................s...
.n................................................
.........n...............e........................
8..C..............r.....F......................j..
.......C......................................1..s
................n.u..................W...t........
......w..........r.........W..5J..................
.....p..............................J.............
.....T.................................d..........
......prw................uW.....Z.....t..6........
....p.r.....f............7........................
........C.f...q..................3.Y..............
.......w.f..........M.....C..5.......t............
....S..f.q.........................5..............
.............p......J........c................Z...
......................5...........................
....T...........u........D.....8........R.........
..0....T.............7M..........J....RZ..........
......t.Iu......................P.......W..Z......
...............D.......M.....i.......z..........s.
...........F..DM..q............R..................
........T....0............................c....s..
.E........0..............N........................
.......................................1........2X
..........Y....0.q....F..................X........
...............F.I..........................X.....
....U......z..............7i.........S..c.........
E.D..S...............................4.....2......
..S.........z..I......i.........m.............2...
.......E............I.....i..................R....
..................N...............................
....................................m.............
...Y...............P.............m...2............
................N...z................c............
.......................................4..........
........U.........P...............7..d..........4.
........................X....3....d...............
Y................P.U..........3...........d.......
...U..................................3...........
"""

rows = test_string.split("\n")
height = len(rows)
width = len(rows[1])

# map the grid to a representation of smt like
# (x, y, antenna_type)

antennaes = [(i, j, letter)for i, string in enumerate(rows) for j, letter in enumerate(string)]
antennae_groups = groupby(sorted(antennaes, key= lambda x: x[2]), key = lambda x : x[2])
grouped_dict = {key: list(group) for key, group in antennae_groups}

# you can connect any two points on a 2d grid. So let's find the coordinates of the
# antinode overlap. 
'# . .' #(0,0)
'. # .' #(1, 1) a (1, 1) + (1, 1)


def find_overlap(ant_1, ant_2):
    x_coord = ant_2[0] - ant_1[0]
    y_coord = ant_2[1] - ant_1[1]
    
    pos_1 = (x_coord * 2 + ant_1[0], y_coord * 2 + ant_1[1])
    pos_2 = (x_coord * -2 + ant_1[0], y_coord * -2 + ant_1[1])
    return pos_1, pos_2




if __name__ == "__main__":
    print(antennaes)
    antinodes = set()
    for k in grouped_dict.keys():
        if k == ".": continue
        cart_products = combinations(grouped_dict.get(k), 2)
        for ant_1, ant_2 in cart_products:
            a, b = find_overlap(ant_1[:-1], ant_2[:-1])
            if 0 < a[0] < height and 0 < a[1] < width:
                antinodes.add(a)
            if 0 < b[0] < height and 0 < b[1] < width:
                antinodes.add(b)
    print(antinodes)
    print(len(antinodes))