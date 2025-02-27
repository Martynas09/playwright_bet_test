from models.open_game import OpenGame
from models.actions import Actions
from playwright.sync_api import Page, expect
from models.game_category import GameCategory
from models.game_name import GameName

def test_combo_bet(page: Page):

    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    open_game.open(GameCategory.Game_Shows, GameName.Wheel_of_fortune)

    before_balance_str = actions.get_inner_text('span[data-qa="text-balance-amount"]')

    before_balance = float(before_balance_str.replace(',', '').replace('€', '').strip())

    actions.wait_for('div[data-qa="chips-actions"]',60000)

    iframe.locator('div[data-qa="chip"]', has_text="50").click()

    actions.click('button[data-qa="button-game-item-select-3"]')

    expect(actions.get('div[data-qa="area-live-game-timer"]')).to_have_text(" ", timeout=60000)

    after_balance_str = f"{(before_balance - 50):,.2f}€"

    expect(actions.get('span[data-qa="text-balance-amount"]')).to_contain_text(after_balance_str)