from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_undo_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    open_game.open(GameCategory.Top_Games,GameName.Flash_roulette)

    actions.click("#FLASH_ROULETTE_RULES > div > button")

    actions.wait_for('div[data-qa="chips-actions"]',60000)

    iframe.locator('div[data-qa="chip"]', has_text="50").click()

    iframe.locator('button[data-qa="button-game-item-select-SPLIT-17"]').first.click()

    actions.click('button[data-qa="undo"]')

    expect(actions.get('button[data-qa="repeat"]')).to_be_visible()