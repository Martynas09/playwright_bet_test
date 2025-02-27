from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_combo_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    open_game.open(GameCategory.Top_Games, GameName.Lucky_7)

    actions.click('button[data-qa="button-odds-tab-15"]')

    actions.click('div[data-qa="area-odd-item-1"]')

    actions.click('span[data-qa="area-selectable-item-8"]')

    actions.click('button[data-qa="button-odd-item-dropdown-confirm"]')

    actions.click('button[data-qa="button-bet-slip-combo-game-selection"]')

    actions.click('a[data-qa="button-combo-game-link-3"]')

    actions.click('button[data-qa="button-odds-tab-21"]')

    actions.click('div[data-qa="area-odd-item-273"]')
    
    actions.click('span[data-qa="area-selectable-item-6"]')

    actions.click('button[data-qa="button-odd-item-dropdown-confirm"]')

    total_odd = iframe.locator('span[data-qa="label-total-odd"]')

    expect(total_odd).to_be_visible()


   