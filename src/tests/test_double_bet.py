from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_undo_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)

    open_game.open(GameCategory.Top_Games, GameName.Flash_roulette)

    iframe = page.frame_locator('#betgames_iframe')

    actions.click("#FLASH_ROULETTE_RULES > div > button")

    actions.wait_for('div[data-qa="chips-actions"]',60000)

    iframe.locator('div[data-qa="chip"]', has_text="25").click()

    iframe.locator('button[data-qa="button-game-item-select-BLACK-9"]').first.click()

    actions.click('button[data-qa="double"]')

    actions.wait_for('div[data-qa="area-game-message"]',60000)
    
    actions.click('button[data-qa="link-top-navigation-history"]')

    bet_amount = iframe.locator('div[data-qa="text-bet-item-amount"]').first

    expect(bet_amount).to_contain_text("50.00€")