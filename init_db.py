from app import create_app, db
from models import Category, Item


# Create the database

categories_items = {
    "Fruits": [
        "Apples",
        "Bananas",
        "Oranges",
        "Lemons",
        "Limes",
        "Grapes",
        "Strawberries",
        "Blueberries",
        "Raspberries",
        "Blackberries",
        "Pineapples",
        "Mangoes",
        "Papayas",
        "Kiwis",
        "Peaches",
        "Plums",
        "Nectarines",
        "Cherries",
        "Pears",
        "Watermelons",
        "Cantaloupes",
        "Honeydews",
        "Grapefruits",
        "Pomegranates",
        "Avocados",
        "Figs",
        "Dates",
        "Apricots",
        "Coconuts",
        "Cranberries",
        "Persimmons",
        "Dragon fruits",
        "Star fruits",
        "Passion fruits"
    ],
    "Vegetables": [
        "Carrots",
        "Broccoli",
        "Cauliflower",
        "Spinach",
        "Kale",
        "Lettuce",
        "Romaine",
        "Arugula",
        "Cabbage",
        "Brussels sprouts",
        "Bell peppers (red, green, yellow, orange)",
        "Jalapeños",
        "Tomatoes",
        "Cucumbers",
        "Zucchini",
        "Squash (butternut, acorn)",
        "Potatoes (russet, red, Yukon Gold)",
        "Sweet potatoes",
        "Onions (red, yellow, white)",
        "Garlic",
        "Ginger",
        "Beets",
        "Radishes",
        "Celery",
        "Green beans",
        "Peas",
        "Corn",
        "Eggplants",
        "Mushrooms (button, portobello, shiitake)",
        "Asparagus",
        "Artichokes",
        "Leeks",
        "Scallions (green onions)",
        "Shallots",
        "Turnips",
        "Rutabagas",
        "Okra",
        "Bok choy",
        "Swiss chard",
        "Collard greens"
    ],
      "Fresh Herbs": [
        "Basil",
        "Parsley (curly, flat-leaf)",
        "Cilantro",
        "Dill",
        "Rosemary",
        "Thyme",
        "Sage",
        "Oregano",
        "Mint",
        "Chives",
        "Tarragon",
        "Marjoram",
        "Bay leaves",
        "Lemongrass",
        "Sorrel",
        "Lovage",
        "Chervil",
        "Lemon balm",
        "Fennel fronds",
        "Curry leaves"
    ],
     "Meat": [
        "Ground beef",
        "Steaks (ribeye, sirloin, T-bone, filet mignon)",
        "Roasts (chuck, rump, brisket)",
        "Beef ribs",
        "Beef liver",
        "Beef stew meat",
        "Corned beef"
        "Pork chops",
        "Pork loin",
        "Pork shoulder (Boston butt)",
        "Pork ribs (baby back, spare ribs)",
        "Ground pork",
        "Pork tenderloin",
        "Pork belly",
        "Ham (fresh, cured, smoked)",
        "Bacon",
        "Sausage (Italian, breakfast, bratwurst)"
        "Lamb chops",
        "Leg of lamb",
        "Lamb shoulder",
        "Ground lamb",
        "Lamb shank",
        "Lamb ribs"
    ],
    "Poultry": [
        "Whole chicken",
        "Chicken breasts (bone-in, boneless)",
        "Chicken thighs (bone-in, boneless)",
        "Chicken drumsticks",
        "Chicken wings",
        "Ground chicken",
        "Chicken liver",
        "Chicken tenders"
        "Whole turkey",
        "Turkey breasts",
        "Ground turkey",
        "Turkey thighs",
        "Turkey wings"
    ],
    "Plant-Based Food": [
        "Vegan burgers",
        "Vegan sausages",
        "Vegan deli slices",
        "Vegan meatballs",
        "Vegan chicken strips",
        "Vegan chicken nuggets",
        "Vegan bacon",
        "Vegan jerky"
        "Vegan cheese"
        "Tofu"
    ],
    "Seafood": [
        "Salmon (fillets, steaks, whole)",
        "Tuna (steaks, canned)",
        "Cod (fillets)",
        "Tilapia (fillets)",
        "Halibut (steaks, fillets)",
        "Trout (whole, fillets)",
        "Haddock (fillets)",
        "Snapper (whole, fillets)",
        "Mahi-mahi (fillets)",
        "Swordfish (steaks)",
        "Sea bass (fillets, whole)",
        "Catfish (fillets)",
        "Sardines (fresh, canned)",
        "Anchovies (fresh, canned)"
        "Shrimp (fresh, frozen, cooked, raw)",
        "Lobster (whole, tails)",
        "Crab (whole, legs, lump crab meat)",
        "Scallops",
        "Clams",
        "Mussels",
        "Oysters"
    ],
    "Dairy": [
        "Eggs",
        "Whole milk",
        "Skim milk",
        "2% milk",
        "1% milk",
        "Lactose-free milk",
        "Almond milk",
        "Soy milk",
        "Oat milk",
        "Coconut milk",
        "Cheese",
        "Cheddar",
        "Mozzarella",
        "Parmesan",
        "Swiss",
        "Greek yogurt",
        "Regular yogurt",
        "Butter",
        "Salted butter",
        "Unsalted butter",
        "Margarine",
        "Plant-based butter",
        "Heavy cream",
        "Whipping cream",
        "Coffee creamer"
    ],
    "Bakery": [
        "White bread",
        "Whole wheat bread",
        "Multigrain bread",
        "Rye bread",
        "Croissants",
        "Muffins",
        "Cakes",
        "Cupcakes",
        "Bagels"
    ],
    "Beverages": [
        "Cola",
        "Lemon-lime soda",
        "Root beer",
        "Ginger ale",
        "Tonic water",
        "Club soda",
        "Orange juice",
        "Apple juice",
        "Grape juice",
        "Cranberry juice",
        "Pineapple juice",
        "Tomato juice",
        "Coffee",
        "Tea",
        "Water",
        "Still water",
        "Sparkling water",
        "Flavored water",
        "Mineral water",
        "Beer",
        "Wine (red, white, rosé)",
        "Spirits (vodka, gin, whiskey, rum)",
        "Sports drinks",
        "Energy drinks"
    ],
    "Pantry Staples": [
        "Pasta",
        "Rice",
        "Canned goods",
        "Cooking oils",
        "Sauces and condiments",
        "Spices and seasonings"
    ],
    "Snacks": [
        "Potato chips",
        "Tortilla chips",
        "Veggie chips",
        "Popcorn",
        "Nuts",
        "Seeds",
        "Saltine crackers",
        "Cheese crackers",
        "Granola bars",
        "Protein bars",
        "Energy bars",
        "Fruit and nut bars",
        "Candy",
        "Cookies"
    ],
    "Baking Supplies": [
        "All-purpose flour",
        "Whole wheat flour",
        "Cake flour",
        "Sugar",
        "Granulated sugar",
        "Brown sugar",
        "Powdered sugar",
        "Baking Mixes",
        "Vanilla extract",
        "Almond extract",
        "Lemon extract",
        "Cocoa powder",
        "Baking chocolate",
        "Sweeteners",
        "Honey",
        "Maple syrup",
        "Coconut flakes",
        "Sprinkles",
        "Spices & Seasonings"
    ],
    "Cereal & Breakfast": [
        "Cereals",
        "Oatmeal",
        "Pancake mix",
        "Syrup",
        "Breakfast bars"
    ],
    "Health & Wellness": [
        "Vitamins",
        "Supplements",
        "Protein bars",
        "Health foods"
    ],
    "Personal Care": [
        "Shampoo and conditioner",
        "Soap and body wash",
        "Dental care products",
        "Deodorant",
        "Skincare products"
    ],
    "Household Items": [
        "Cleaning supplies",
        "Paper towels",
        "Toilet paper",
        "Laundry detergent",
        "Dish soap"
        "Papertowel"
    ],
    "Baby Products": [
        "Baby food",
        "Diapers",
        "Baby wipes",
        "Baby formula"
    ],
    "Flowers & Plants":  [
        "Fresh flowers",
        "Potted plants",
        "Seeds"
    ],
    "Miscellaneous": [
        "Batteries",
        "Light Bulbs",
        "Kitchen Utensils",
        "Tools & Hardware",
        "Office Supplies",
        "First Aid Supplies",
        "Party Supplies"
    ]
}

def init_db():
    app = create_app() #Creates the Flask app
    with app.app_context(): 
        db.create_all() #Creates the database tables
        for category_name, items in categories_items.items(): #Loops through the categories and items
            category = Category.query.filter_by(name=category_name).first() #Queries the database for the category
            if not category:  #Checks if the category exists
                category = Category(name=category_name) 
                db.session.add(category) #Adds the category to the database
                db.session.commit()
            for item_name in items: 
                item = Item.query.filter_by(name=item_name, category_id=category.id).first() #Queries the database for the item
                if not item: #Checks if the item exists
                    item = Item(name=item_name, category_id=category.id) 
                    db.session.add(item) 
                    db.session.commit()

if __name__ == '__main__':
    init_db()
