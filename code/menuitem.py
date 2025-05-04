from dataclasses import dataclass, asdict

@dataclass
class MenuItem:
    # these are built-in properties
    category: str
    name: str
    price: float
    description: str

    # convert to a dictionary
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return MenuItem(**data)
    
    # add a string representation for nicer print output
    def __str__(self):
        return f"{self.category}: {self.name} - ${self.price:.2f}\n{self.description}"
    
if __name__ == '__main__':
    # example of how to use the dataclass

    # create a new MenuItem    
    mozz = MenuItem(name="Mozzarella Sticks", 
                    price=8.99, 
                    category="Apps", 
                    description="Fried cheese sticks served with marinara sauce.")

    # can assign a new category
    mozz.category = "Appetizers"
    print(mozz)  # prints nicely formatted menu item

    # convert back to a dictionary
    print(mozz.to_dict())

    # create a new MenuItem from a dictionary
    burger = MenuItem.from_dict({"name": "Burger", 
                                 "price": 9.99, 
                                 "description": "A delicious burger.", 
                                 "category": "Entrees"})
    print(burger)  # prints nicely formatted menu item

    # # add example: list of menu items and convert all to dicts
    menu_items = [mozz, burger]
    menu_dicts = [item.to_dict() for item in menu_items]
    print(menu_dicts)

    # # add example: load menu items from a list of dicts
    new_items = [MenuItem.from_dict(d) for d in menu_dicts]
    for item in new_items:
        print(item)

