from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Restaurant, Base, MenuItem

engine = create_engine('sqlite:///restaurant-menu.db')
Base.metadata.bind = engine
# Create all tables in the engine
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Define the locations
locations = ["choba", "rumuokoro", "worji", "rumuola", "rumumasi", "mile one", "eleme", "ada george", "elekahia"]

# Menu for Urban Burger
urban_burger = Restaurant(name="Urban Burger", location=locations[0])
session.add(urban_burger)
session.commit()
menu_items_urban_burger = [
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="7.50", restaurant=urban_burger),
    MenuItem(name="French Fries", description="with garlic and parmesan",
             price="2.99", restaurant=urban_burger),
    MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
             price="5.50", restaurant=urban_burger),
    MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
             price="3.99", restaurant=urban_burger),
    MenuItem(name="Sirloin Burger", description="Made with grade A beef",
             price="7.99", restaurant=urban_burger),
    MenuItem(name="Root Beer", description="16oz of refreshing goodness",
             price="1.99", restaurant=urban_burger),
    MenuItem(name="Iced Tea", description="with Lemon",
             price=".99", restaurant=urban_burger),
    MenuItem(name="Grilled Cheese Sandwich", description="On texas toast with American Cheese",
             price="3.49", restaurant=urban_burger),
    MenuItem(name="Veggie Burger", description="Made with freshest of ingredients and home grown spices",
             price="5.99", restaurant=urban_burger),
]
for item in menu_items_urban_burger:
    session.add(item)
session.commit()

# Menu for Super Stir Fry
super_stir_fry = Restaurant(name="Super Stir Fry", location=locations[1])
session.add(super_stir_fry)
session.commit()
menu_items_super_stir_fry = [
    MenuItem(name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
             price="7.99", restaurant=super_stir_fry),
    MenuItem(name="Peking Duck", description="A famous duck dish from Beijing that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", 
             price="25", restaurant=super_stir_fry),
    MenuItem(name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce",
             price="15", restaurant=super_stir_fry),
    MenuItem(name="Nepali Momo", description="Steamed dumplings made with vegetables, spices and meat.",
             price="12", restaurant=super_stir_fry),
    MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
             price="14", restaurant=super_stir_fry),
    MenuItem(name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
             price="12", restaurant=super_stir_fry),
]
for item in menu_items_super_stir_fry:
    session.add(item)
session.commit()

# Menu for Panda Garden
panda_garden = Restaurant(name="Panda Garden", location=locations[2])
session.add(panda_garden)
session.commit()
menu_items_panda_garden = [
    MenuItem(name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
             price="8.99", restaurant=panda_garden),
    MenuItem(name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
             price="6.99", restaurant=panda_garden),
    MenuItem(name="Gyoza", description="The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner",
             price="9.95", restaurant=panda_garden),
    MenuItem(name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
             price="6.99", restaurant=panda_garden),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="9.50", restaurant=panda_garden),
]
for item in menu_items_panda_garden:
    session.add(item)
session.commit()

# Menu for Thyme for That
thyme_for_that = Restaurant(name="Thyme for That Vegetarian Cuisine", location=locations[3])
session.add(thyme_for_that)
session.commit()
menu_items_thyme_for_that = [
    MenuItem(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
             price="2.99", restaurant=thyme_for_that),
    MenuItem(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
             price="5.99", restaurant=thyme_for_that),
    MenuItem(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
             price="4.50", restaurant=thyme_for_that),
    MenuItem(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a mildly spiced soya, garlic sauce cooked with fresh cilantro, celery, chilies, ginger & green onions",
             price="6.95", restaurant=thyme_for_that),
    MenuItem(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
             price="7.95", restaurant=thyme_for_that),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="6.80", restaurant=thyme_for_that),
]
for item in menu_items_thyme_for_that:
    session.add(item)
session.commit()

# Menu for Tony's Bistro
tonys_bistro = Restaurant(name="Tony's Bistro", location=locations[4])
session.add(tonys_bistro)
session.commit()
menu_items_tonys_bistro = [
    MenuItem(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
             price="13.95", restaurant=tonys_bistro),
    MenuItem(name="Chicken and Rice", description="Chicken... and rice",
             price="4.95", restaurant=tonys_bistro),
    MenuItem(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
             price="6.95", restaurant=tonys_bistro),
    MenuItem(name="Choc Full O' Mint (Smitten's Fresh Mint Chip ice cream)",
             description="Milk, cream, salt, ..., Liquid nitrogen magic", price="3.95", restaurant=tonys_bistro),
    MenuItem(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
             price="7.95", restaurant=tonys_bistro),
]
for item in menu_items_tonys_bistro:
    session.add(item)
session.commit()

# Menu for Andala's
andalas = Restaurant(name="Andala's", location=locations[5])
session.add(andalas)
session.commit()
menu_items_andalas = [
    MenuItem(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
             price="9.95", restaurant=andalas),
    MenuItem(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
             price="7.95", restaurant=andalas),
    MenuItem(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
             price="6.50", restaurant=andalas),
    MenuItem(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
             price="6.75", restaurant=andalas),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="7.00", restaurant=andalas),
]
for item in menu_items_andalas:
    session.add(item)
session.commit()

# Menu for Auntie Ann's
auntie_anns = Restaurant(name="Auntie Ann's", location=locations[6])
session.add(auntie_anns)
session.commit()
menu_items_auntie_anns = [
    MenuItem(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
             price="8.99", restaurant=auntie_anns),
    MenuItem(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe berries turned into frozen (and seedless) awesomeness",
             price="2.99", restaurant=auntie_anns),
    MenuItem(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
             price="10.95", restaurant=auntie_anns),
    MenuItem(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
             price="7.50", restaurant=auntie_anns),
    MenuItem(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal oven",
             price="8.95", restaurant=auntie_anns),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="9.50", restaurant=auntie_anns),
]
for item in menu_items_auntie_anns:
    session.add(item)
session.commit()

# Menu for Cocina Y Amor
cocina_y_amor = Restaurant(name="Cocina Y Amor", location=locations[7])
session.add(cocina_y_amor)
session.commit()
menu_items_cocina_y_amor = [
    MenuItem(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
             price="5.95", restaurant=cocina_y_amor),
    MenuItem(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. The core of cachapa is masa harina, a stone-ground flour made from dried corn.",
             price="7.99", restaurant=cocina_y_amor),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="9.50", restaurant=cocina_y_amor),
]
for item in menu_items_cocina_y_amor:
    session.add(item)
session.commit()

# Menu for State Bird Provisions
state_bird_provisions = Restaurant(name="State Bird Provisions", location=locations[8])
session.add(state_bird_provisions)
session.commit()
menu_items_state_bird_provisions = [
    MenuItem(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
             price="5.95", restaurant=state_bird_provisions),
    MenuItem(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
             price="6.95", restaurant=state_bird_provisions),
    MenuItem(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
             price="4.25", restaurant=state_bird_provisions),
    MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
             price="9.50", restaurant=state_bird_provisions),
]
for item in menu_items_state_bird_provisions:
    session.add(item)
session.commit()

print("added menu items!")
