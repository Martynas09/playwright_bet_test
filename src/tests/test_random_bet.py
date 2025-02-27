from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_combo_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    
    open_game.open(GameCategory.Top_Games, GameName.Lucky_7)

    actions.click('button[data-qa="button-add-random-betting-option"]')

    actions.click('button[data-qa="button-bet-slip-amount-clear"]')

    actions.click('button[data-qa="button-bet-slip-amount-5"]')
    
    actions.wait('button[data-qa="button-place-bet"]')

    actions.click('button[data-qa="button-place-bet"]')

    confirmation_message = actions.get('span[data-qa="text-bet-slip-notification"]')

    expect(confirmation_message).to_be_visible()


   