import re
from functools import reduce

def part_a(infile):
    symbols,gears,engine_parts = parse_file(infile)
    adjacent = list()

    for engine_loc,part in engine_parts.items():
        pts_to_check = get_adjacent_points(engine_loc,part)
        if len(pts_to_check.intersection(symbols))>0:
            adjacent.append(part)


    return sum(int(i) for i in adjacent)

def part_b(infile):
    symbols,gears,engine_parts = parse_file(infile)
    ratios = list()
    engine_points = make_engine_points(engine_parts)
    all_points = set(engine_points.keys())

    for gear in gears:
        pts_to_check = get_adjacent_points(gear,'*')
        adjacent_points = pts_to_check.intersection(all_points)
        adjacent_engine = {engine_points[point] for point in adjacent_points}
        if len(adjacent_engine) == 2:
            ratios.append(reduce(lambda a,b:int(engine_parts[a])*int(engine_parts[b]),adjacent_engine))
    
    return sum(ratios)

    

def parse_file(infile):
    symbols = set()
    engine_parts = dict()
    gears = set()
    
    for l_no,line in enumerate(infile.readlines()):
        symbols.update((x.span()[0],l_no) for x in re.finditer(r"[^.0-9]",line.strip()))
        gears.update((x.span()[0],l_no) for x in re.finditer(r'\*',line.strip()))
        engine_parts.update(
                {(x.span()[0],l_no):x.group() 
                    for x in 
                    re.finditer(r"\d+",line.strip())})

    return (symbols,gears,engine_parts)

def get_adjacent_points(engine_loc,part):
    ops = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    pts_of_eng = {(engine_loc[0]+i,engine_loc[1]) for i in range(len(part))}
    pts = set()
    for pt in pts_of_eng:
        pts.update(
                (pt[0]+op[0],pt[1]+op[1]) for op in ops)

    return pts

def make_engine_points(engine_parts):
    engine_points = dict()
    for loc,part in engine_parts.items():
        engine_points.update({(loc[0]+i,loc[1]):loc for i in range(len(part))})
    return engine_points



