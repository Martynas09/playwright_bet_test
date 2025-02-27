import re
from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_place_above_max_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    open_game.open(GameCategory.Top_Games, GameName.Lucky_5)

    actions.click('button[data-qa="button-odds-tab-21"]')

    actions.click('div[data-qa="area-odd-item-273"]')

    actions.click('span[data-qa="area-selectable-item-6"]')

    actions.click('button[data-qa="button-odd-item-dropdown-confirm"]')

    limit_text = actions.get_inner_text('span[data-qa="text-bet-slip-limits"]')

    # Getting the max bet amount number
    match = re.findall(r'(\d+\.\d+)', limit_text)
    if match:
        max_limit = float(match[-1])

    actions.click('button[data-qa="button-bet-slip-amount-clear"]')

    iframe.locator('input[data-qa="input-bet-slip-amount"]').fill(str(max_limit+1))

    expect(actions.get('button[data-qa="button-place-bet disabled"]')).to_be_visible(timeout=1000)
    