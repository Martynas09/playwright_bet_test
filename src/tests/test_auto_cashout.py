from models.open_game import OpenGame
from models.actions import Actions
from models.game_category import GameCategory
from models.game_name import GameName
from playwright.sync_api import Page, expect

def test_combo_bet(page: Page):
    
    actions = Actions(page)
    open_game = OpenGame(page)
    iframe = page.frame_locator('#betgames_iframe')

    first_interaction = True

    while True:
        open_game.open(GameCategory.Top_Games, GameName.Skyward)

        iframe.locator('div[data-qa="area-bet-slip"]').first.wait_for(state='visible')

        left_betslip = iframe.locator('div[data-qa="area-bet-slip"]').first

        # Setting up betslip only for first time, because it caches the selection on reload
        if first_interaction:
            left_betslip.locator('input[data-qa="undefined-checkbox"]').click(force=True)
            left_betslip.locator('button[data-qa="button-bet-slip-amount-3"]').click()
            first_interaction = False

        actions.wait_for('div[data-qa="area-game-message"]', 60000)
            
        left_betslip.locator('button[data-qa="button-place-bet"]').wait_for(state='visible')

        left_betslip.locator('button[data-qa="button-place-bet"]').click()

        left_betslip.locator('button[data-qa="button-place-bet"][class*="PlaceBetButton_cancel"]').wait_for(state='visible', timeout=60000)

        left_betslip.locator('button[data-qa="button-place-bet"][class*="PlaceBetButton_cash-out"]').wait_for(state='visible')

        # Getting current draw code and waiting for to change
        draw_code = actions.get('[data-qa="text-game-draw-code"]')
        current_draw_code = draw_code.inner_text()
        numeric_value = int(current_draw_code.lstrip('#')) 
        new_draw_code = f"#{numeric_value + 1}"
        expect(draw_code).to_have_text(new_draw_code, timeout=60000)


        actions.click('button[data-qa="link-top-navigation-results"]')

        last_result = iframe.locator('div[data-qa="area-bet-item-result"]').first.inner_text()

        multiplier_amount_str  = left_betslip.locator('input[data-qa="input-bet-slip-amount"]').nth(1).input_value()
        multiplier_amount = float(multiplier_amount_str.replace('x', '').strip())
        formatted_multiplier_amount = f"{multiplier_amount:.2f}"

        # Checking did the multiplier reached the requested cashout multiplier
        try:
            last_result_value = float(last_result) 

            if last_result_value > multiplier_amount:
                break

        except:
            break 

    actions.click('button[data-qa="link-top-navigation-history"]')
    actions.click('button[data-qa="button-history-tab-single"]')

    expect(actions.get('div[data-qa="area-bet-item-odd-value"]').first).to_have_text(formatted_multiplier_amount)
