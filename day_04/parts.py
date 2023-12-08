import re

def part_a(infile):
    cards = parse_file(infile)
    total_points = 0
    for card,data in cards.items():
        card_points = get_card_points(data)
        if card_points>0:
            total_points += pow(2,card_points-1)

    return total_points

def part_b(infile):
    cards = parse_file(infile)

    instances_of_cards = {i:1 for i in cards.keys()}

    for card_num in cards.keys():
        card_matches = get_card_points(cards[card_num])
        for instance in range(instances_of_cards[card_num]):
            for i in range(1,card_matches+1):
                instances_of_cards[str(int(card_num)+i)]+=1

    return sum(instances_of_cards.values())

def get_card_points(data):
    lucky_numbers,my_numbers = (re.findall(r'\d+',d.strip()) for d in data.split("|"))
    card_points = 0
    for number in lucky_numbers:
        card_points += my_numbers.count(number)
    return card_points
    

def parse_file(infile):
    cards = dict()
    for line in infile.readlines():
        card,data = (i.strip() for i in line.strip().split(":"))
        card = re.search(r'\d+',card).group()
        cards[card]=data
    return cards


