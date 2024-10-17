from magicDatabase import magic_db
from match import match
from typing import List, Tuple, Callable, Any

# Basic functions
def get_name(card: Tuple[str,str,int,str,str]) -> str:
    return card[0]
def get_type(card: Tuple[str,str,int,str,str]) -> str:
    return card[1]
def get_year(card: Tuple[str,str,int,str,str]) -> int:
    return card[2]
def get_flavor(card: Tuple[str,str,int,str,str]) -> str:
    return card[3]
def get_color(card: Tuple[str,str,int,str,str]) -> str:
    return card[4]
# Actions
def card_by_year():
    pass
def card_by_year_range():
    pass 
def card_before_year():
    pass
def card_after_year():
    pass
def type_by_card():
    pass
def card_by_type():
    pass
def flavor_by_card():
    pass
def card_by_flavor():
    pass
def year_by_card():
    pass
def color_by_card():
    pass
def card_by_color():
    pass
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
    (str.split("Give me a list of % cards"), card_by_color)
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
    print("Welcome to the movie database!\n")
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



#query_loop()

