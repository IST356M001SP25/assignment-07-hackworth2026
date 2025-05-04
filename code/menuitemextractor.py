if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price: str) -> float:
    # Remove currency symbols and whitespace, replace comma with dot if needed
    price = price.replace('$', '').replace('€', '').strip()
    price = price.replace(',', '.')
    try:
        return float(price)
    except ValueError:
        raise ValueError(f"Invalid price format: {price}")

def clean_scraped_text(scraped_text: str) -> list[str]:
    # Split scraped text by newlines, remove empty lines, strip whitespace
    lines = scraped_text.strip().split('\n')
    return [line.strip() for line in lines if line.strip()]

def extract_menu_item(title: str, scraped_text: str) -> MenuItem:
    """
    Extracts a MenuItem from a title and scraped text block.
    Assumes the scraped_text lines are:
    [description, price]
    """
    lines = clean_scraped_text(scraped_text)
    if len(lines) < 2:
        raise ValueError("scraped_text must have at least description and price")
    
    description = lines[0]
    price = clean_price(lines[1])
    category = title  # assuming title is the category
    
    return MenuItem(name=title, category=category, price=price, description=description)



if __name__=='__main__':
    pass
