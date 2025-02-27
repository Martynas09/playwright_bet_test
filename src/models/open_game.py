import os
from dotenv import load_dotenv

class OpenGame:
        def __init__(self, page):
                load_dotenv()
                self.page = page
                self.url = os.getenv("BETGAMES_URL")

        def open(self, category, game_name):
    
                # Navigate to the demo page
                self.page.goto(self.url)
        
                # Locate the iframe by its ID
                iframe = self.page.frame_locator('#betgames_iframe')
                
                # Wait for iframe to fully load
                iframe.locator('button.tabs-bar-item').first.wait_for(state='visible')

                # Game category buttons
                buttons = iframe.locator('button.tabs-bar-item').all()

                if buttons:
                        buttons[category.value].wait_for(state='visible')
                        buttons[category.value].click()

                game_selector = f'a[data-qa="area-game-card-{game_name.value}"]'

                iframe.locator(game_selector).wait_for(state='visible')
                iframe.locator(game_selector).click()
