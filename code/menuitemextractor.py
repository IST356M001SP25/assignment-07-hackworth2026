if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price: str) -> float:
    # Remove currency symbols and whitespace, replace comma with dot if needed
    price = price.replace('$', '').replace('€', '').strip()
    price = price.replace(',', '')
    try:
        return float(price)
    except ValueError:
        raise ValueError(f"Invalid price format: {price}")

def clean_scraped_text(scraped_text: str) -> list[str]:
    # Split scraped text by newlines, remove empty lines, strip whitespace
    lines = scraped_text.strip().split('\n')
    return [line.strip() for line in lines if line.strip()]

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    lines = clean_scraped_text(scraped_text)
    price = 0.0
    description = "No description available"

    for line in lines:
        try:
            price = clean_price(line)
            lines.remove(line)
            break
        except ValueError:
            continue

    if lines:
        description = lines[0]

    return MenuItem(name=title, category=title, price=price, description=description)



if __name__=='__main__':
    pass
