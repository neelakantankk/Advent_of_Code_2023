from functools import reduce

def part_a(infile):
    result = 0
    games = parse_file(infile)
    for g_id, game in games.items():
        if game['red']<=12 and game['green']<=13 and game['blue']<=14:
            result += g_id
    return result


def part_b(infile):
    result = 0
    games = parse_file(infile)
    for game in games.values():
        power = reduce(lambda a,b: a*b,game.values())
        result+=power

    return result

def parse_file(infile):
    games = dict()
    for line in infile.readlines():
        game_id,game_data = line.strip().split(":")
        game_id = int(game_id.strip().split(" ")[1])
        games[game_id]=dict()
        game_data = game_data.strip()
        for game in game_data.split(";"):
            for cube_count in game.strip().split(","):
                cube_num,cube_name = cube_count.strip().split(" ")
                cube_num = int(cube_num)
                current_num = games[game_id].get(cube_name,0)
                if cube_num > current_num:
                    games[game_id][cube_name] = cube_num
    return games


