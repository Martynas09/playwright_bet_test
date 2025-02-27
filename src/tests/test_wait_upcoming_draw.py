from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_place_valid_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    open_game.open(GameCategory.Top_Games, GameName.Lucky_7)

    actions.click('button[data-qa="button-odds-tab-15"]')

    actions.click('div[data-qa="area-odd-item-1"]')

    actions.click('span[data-qa="area-selectable-item-8"]')

    actions.click('button[data-qa="button-odd-item-dropdown-confirm"]')

    actions.wait_for('div[data-qa="area-game-info-timer"]', 60000)

    time_str = iframe.locator('div[data-qa="area-game-info-timer"]').inner_text()

    # Calculating amount of time until next draw
    minutes, seconds = map(int, time_str.split(':'))
    total_seconds = minutes * 60 + seconds

    actions.wait_for('div[data-qa="text-selected-odd-message"]', (total_seconds * 1000) + 5000)

    actions.wait_for('div[data-qa="text-selected-odd-message"]',60000)

    actions.wait('div[data-qa="text-game-draw-code"]')
    
    actions.click('button[data-qa="button-bet-slip-amount-clear"]')

    actions.click('button[data-qa="button-bet-slip-amount-5"]')

    actions.wait('button[data-qa="button-place-bet"]')

    actions.click('button[data-qa="button-place-bet"]')
    
    confirmation_message = iframe.locator('span[data-qa="text-bet-slip-notification"]')
    
    expect(confirmation_message).to_be_visible()
