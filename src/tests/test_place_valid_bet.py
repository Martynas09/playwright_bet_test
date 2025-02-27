from models.open_game import OpenGame
from models.actions import Actions
from models.game_category import GameCategory
from models.game_name import GameName
from playwright.sync_api import Page, expect

def test_place_valid_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')
    
    open_game.open(GameCategory.Top_Games, GameName.Lucky_5)
    
    actions.click('button[data-qa="button-odds-tab-21"]')

    actions.click('div[data-qa="area-odd-item-273"]')

    actions.click('span[data-qa="area-selectable-item-6"]')

    actions.click('button[data-qa="button-odd-item-dropdown-confirm"]')

    actions.click('button[data-qa="button-bet-slip-amount-clear"]')

    actions.click('button[data-qa="button-bet-slip-amount-5"]')

    actions.wait('button[data-qa="button-place-bet"]')

    actions.click('button[data-qa="button-place-bet"]')

    confirmation_message = iframe.locator('span[data-qa="text-bet-slip-notification"]')

    expect(confirmation_message).to_be_visible()
