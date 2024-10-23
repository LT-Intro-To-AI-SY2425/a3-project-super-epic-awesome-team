from magicDatabase import magic_db
from match import match
from typing import List, Tuple, Callable, Any

# Basic functions
def get_name(card: Tuple[str,List[str],int,str,List[str]]) -> str:
    return card[0]
def get_type(card: Tuple[str,List[str],int,str,List[str]]) -> List[str]:
    return card[1]
def get_year(card: Tuple[str,List[str],int,str,List[str]]) -> int:
    return card[2]
def get_flavor(card: Tuple[str,List[str],int,str,List[str]]) -> str:
    return card[3]
def get_color(card: Tuple[str,List[str],int,str,List[str]]) -> List[str]:
    return card[4]
# Actions
def card_by_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    result = []
    for card in magic_db:
        if get_year(card) == year:
            result.append(get_name(card))
    return result
def card_by_year_range(matches: List[str]) -> List[str]:
    year1 = int(matches[0])
    year2 = int(matches[1])
    result = []
    for card in magic_db:
        if get_year(card)>=year1 and get_year(card) <= year2:
            result.append(get_name(card))
    return result
def card_before_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    result = []
    for card in magic_db:
        if get_year(card) < year:
            result.append(get_name(card))
    return result
def card_after_year(matches: List[str]) -> List[str]:
    year = int(matches[0])
    result = []
    for card in magic_db:
        if get_year(card) > year:
            result.append(get_name(card))
    return result
def type_by_card(matches: List[str]) -> List[str]:
    name = matches[0]
    for card in magic_db:
        if name == get_name(card):
            return get_type(card)
    return []
def card_by_type(matches: List[str]) -> List[str]:
    cardType = matches[0]
    result = []
    for card in magic_db:
        types = get_type(card)
        if cardType in types:
            result.append(get_name(card))
    return result
def flavor_by_card(matches: List[str]) -> List[str]:
    name = matches[0]
    for card in magic_db:
        if get_name(card) == name:
            flavor = get_flavor(card)
            if flavor == "":
                return ["This card has no flavor text!"]
            else: return [flavor]
    return []
def card_by_flavor(matches: List[str]) -> List[str]:
    flavor = matches[0]
    result = []
    for card in magic_db:
        if get_flavor(card) == flavor:
            result.append(flavor)
    return result

def year_by_card(matches: List[str]) -> List[str]:
    name = matches[0]
    for card in magic_db:
        if get_name(card) == name:
            return [get_year(card)]
    return []
def color_by_card(matches: List[str]) -> List[str]:
    name = matches[0]
    for card in magic_db:
        if get_name(card) == name:
            return get_color(card)
    return []

def card_by_color(matches: List[str]) -> List[str]:
    cardColor = matches[0]
    result = []
    for card in magic_db:
        if cardColor in get_color(card):
            result.append(get_name(card))
    return result
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt
 # PA and query loop
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what cards were made in _"), card_by_year),
    (str.split("what cards were made between _ and _"), card_by_year_range),
    (str.split("what cards were made before _"), card_before_year),
    (str.split("what cards were made after _"), card_after_year),
    (str.split("what card type is %"), type_by_card),
    (str.split("what cards have the % type"), card_by_type),
    (str.split("what is the flavor text of %"), flavor_by_card),
    (str.split("when was % made"), year_by_card),
    (str.split("what color is %"), color_by_card),
    (str.split("give me a list of % cards"), card_by_color),
    (["bye"], bye_action),
]

def search_pa_list(src: List[str]) -> List[str]:

    for pa in pa_list:
        if match(pa[0],src) != None:
            answer = pa[1](match(pa[0],src))
            if answer == []:
                return ["No answers"]
            else: return answer
    return ["I don't understand"] 


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the magic database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")

query_loop() 