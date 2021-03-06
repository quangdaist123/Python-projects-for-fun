from trello import TrelloClient, Board, List, Card
from datetime import datetime
from config import TRELLO_API, TRELLO_TOKEN
client = TrelloClient(
    api_key=TRELLO_API,
    api_secret='your-secret',
    token=TRELLO_TOKEN,
    token_secret='your-oauth-token-secret'
)


# My 4 lists in Daily board:
## <List πͺπͺπͺπͺ>
## <List ππππ>
## <List π₯°πππ>
## <List ββββ>
## <List HαΊ­u Vα» QuΓͺ>


def get_trello_board_from(client: TrelloClient, board_name: str):
    all_boards = client.list_boards()
    for board in all_boards:
        if board.name == board_name:
            return board


def get_trello_list_from(board: Board, list_name: str):
    for item in board.list_lists():
        if item.name == list_name:
            return item


def add_trello_card_to(client, board_name: str, list_name: str, card_name: str):
    print("Adding a Trello card...")
    trello_board = get_trello_board_from(client, board_name)
    trello_list = get_trello_list_from(trello_board, list_name)
    trello_list.add_card(card_name)
    print("Add successfully!")


def today_is(*days_of_week: str) -> bool:
    week_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    week_days_num = {date: index for index, date in enumerate(week_days)}
    today_week_num = datetime.today().weekday()
    return any(today_week_num == week_days_num[d.lower()] for d in days_of_week)


if today_is("Saturday"):
    add_trello_card_to(client, board_name="Daily", list_name="π₯°πππ", card_name="CαΊ―t mΓ³ng tay")

if today_is("Tuesday", "Thursday", "Saturday"):
    add_trello_card_to(client, board_name="Daily", list_name="π₯°πππ", card_name="Lau bΓ n hα»c")

if today_is("Wednesday", "Saturday"):
    add_trello_card_to(client, board_name="Daily", list_name="π₯°πππ", card_name="Cho mαΊ₯y bΓ© uα»ng sα»―a")
    add_trello_card_to(client, board_name="Daily", list_name="π₯°πππ", card_name="Δα» nΖ°α»c vΓ΄ αΊ₯m Δun")

# -----------------------