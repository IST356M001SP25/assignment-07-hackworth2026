import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tullysgoodtimes.com/menus/")

    # TODO Write code here
    categories = page.query_selector_all('.menu-category')
    menu_items = []

    for category_element in categories:
        category_title = category_element.query_selector('h2').inner_text().strip()
        item_elements = category_element.query_selector_all('.menu-item')

        for item_element in item_elements:
            item_title = item_element.query_selector('.menu-item-title').inner_text().strip()
            item_description = item_element.query_selector('.menu-item-description').inner_text().strip()
            item_price = item_element.query_selector('.menu-item-price').inner_text().strip()

            scraped_text = f"{item_description}\n{item_price}"

            try:
                menu_item = extract_menu_item(item_title, scraped_text)
                menu_item.category = category_title  # override category with section title
                menu_items.append(menu_item.to_dict())
            except Exception as e:
                print(f"Error extracting {item_title}: {e}")

    # Save to DataFrame and CSV
    df = pd.DataFrame(menu_items)
    df.to_csv('tullys_menu.csv', index=False)
    print("Saved tullys_menu.csv")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
