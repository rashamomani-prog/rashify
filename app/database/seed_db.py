from app.database.database import SessionLocal, engine, Base
from app.models.user import User
from app.models.recipe import Recipe


def seed_data():
    print("🧹 Cleaning old database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        print("🍳 Adding fresh recipes to Rashify...")
        admin_user = User(
            name="Rashify Chef",
            email="chef@rashify.com",
            password="hashed_password_123"
        )
        db.add(admin_user)
        db.flush()

        recipes = [
            # --- Breakfast ---
            Recipe(title="Avocado Toast 🥑", category="Breakfast",
                   ingredients="1 slice whole-grain bread, 1/2 ripe avocado, 1 tsp lemon juice, salt, black pepper, 1 poached egg",
                   instructions="1. Toast the bread. 2. Mash avocado with lemon, salt, and pepper. 3. Spread on toast and top with egg.",
                   owner_id=admin_user.id),
            Recipe(title="Yogurt Fruit Bowl 🍯", category="Breakfast",
                   ingredients="Yogurt, Honey, Fresh fruits (Banana, Strawberry, Apple), Nuts or Oats",
                   instructions="1. Place yogurt in a bowl. 2. Add chopped fruits. 3. Drizzle honey and nuts.",
                   owner_id=admin_user.id),
            Recipe(title="Qallayet Bandora 🍅", category="Breakfast",
                   ingredients="3 tomatoes, 1 onion, 1-2 eggs, 2 tbsp olive oil, salt, pepper",
                   instructions="1. Sauté onions in oil. 2. Add tomatoes and stir. 3. Season and simmer. 4. Optional: Add eggs on top.",
                   owner_id=admin_user.id),

            # --- Lunch ---
            Recipe(title="Jordanian Mansaf 🍖", category="Lunch",
                   ingredients="2kg Lamb, 1kg Jameed, 1kg Rice, Shrak bread, Nuts, Parsley",
                   instructions="1. Boil meat. 2. Blend Jameed with broth and add to meat. 3. Cook rice with turmeric. 4. Layer bread, rice, then meat. Garnish with nuts.",
                   owner_id=admin_user.id),
            Recipe(title="Maqluba 🍆", category="Lunch",
                   ingredients="1kg Chicken, 3 cups Rice, Eggplant, Cauliflower, Potatoes, Spices",
                   instructions="1. Fry vegetables. 2. Layer chicken, veggies, then rice in a pot. 3. Cook with broth and flip when done.",
                   owner_id=admin_user.id),
            Recipe(title="Kabsa 🍗", category="Lunch",
                   ingredients="1kg Chicken, 3 cups Basmati rice, Onions, Tomato puree, Kabsa spices",
                   instructions="1. Brown chicken with onions and spices. 2. Add tomato and water; cook chicken. 3. Add rice to broth and simmer.",
                   owner_id=admin_user.id),

            # --- Dinner ---
            Recipe(title="Grilled Cheese 🧀", category="Dinner",
                   ingredients="2 slices bread, Cheddar cheese, 1 tbsp butter, Oregano",
                   instructions="1. Butter bread. 2. Place cheese between slices. 3. Grill in a pan until golden.",
                   owner_id=admin_user.id),
            Recipe(title="Halloumi Wrap 🥙", category="Dinner",
                   ingredients="Halloumi cheese, Tortilla, Cucumber, Tomato, Mint, Olive oil",
                   instructions="1. Pan-fry halloumi. 2. Place on bread with veggies and mint. 3. Wrap and toast.",
                   owner_id=admin_user.id),
            Recipe(title="Tuna Corn Salad 🥗", category="Dinner",
                   ingredients="1 can Tuna, Sweet corn, 1 tbsp Mayonnaise, Lemon juice, Salt",
                   instructions="1. Mix tuna and corn. 2. Add mayo and lemon. 3. Season and serve.",
                   owner_id=admin_user.id),

            # --- Drinks ---
            Recipe(title="Lemon Mint Juice 🍋", category="Drinks",
                   ingredients="4 Lemons, 1 cup Mint, 4 tbsp Sugar, 3 cups Water, Ice",
                   instructions="1. Blend all ingredients. 2. Strain and serve over ice.", owner_id=admin_user.id),
            Recipe(title="Iced Caramel Macchiato 🧊", category="Drinks",
                   ingredients="Espresso, 1 cup Milk, Vanilla syrup, Caramel sauce, Ice",
                   instructions="1. Put vanilla syrup in glass. 2. Add ice and milk. 3. Pour espresso on top and drizzle caramel.",
                   owner_id=admin_user.id),
            Recipe(title="Iced Mocha 🍫", category="Drinks", ingredients="Espresso, 1 cup Milk, Chocolate syrup, Ice",
                   instructions="1. Mix espresso with chocolate. 2. Add to ice and milk.", owner_id=admin_user.id),
            Recipe(title="Affogato Coffee 🍦", category="Drinks", ingredients="Vanilla ice cream, 1 shot hot Espresso",
                   instructions="1. Put ice cream in a glass. 2. Pour hot espresso over it.", owner_id=admin_user.id),

            # --- Desserts ---
            Recipe(title="Easy Tiramisu 🍮", category="Desserts",
                   ingredients="Ladyfingers, Mascarpone, Whipping cream, Coffee, Cocoa",
                   instructions="1. Mix cream and mascarpone. 2. Dip biscuits in coffee. 3. Layer biscuits and cream. 4. Chill and dust with cocoa.",
                   owner_id=admin_user.id),
            Recipe(title="Chocolate Lava Cake 🍫", category="Desserts",
                   ingredients="Dark chocolate, Butter, 2 Eggs, Sugar, 1 tbsp Flour",
                   instructions="1. Melt chocolate/butter. 2. Mix with whisked eggs and sugar. 3. Add flour and bake at 200°C for 10 mins.",
                   owner_id=admin_user.id),
            Recipe(title="No-Bake Cheesecake 🍓", category="Desserts",
                   ingredients="Digestive biscuits, Butter, Cream cheese, Condensed milk, Jam",
                   instructions="1. Make biscuit base. 2. Mix cheese and milk; pour over base. 3. Chill then top with jam.",
                   owner_id=admin_user.id),

            # --- Healthy ---
            Recipe(title="Quinoa Greek Salad 🥗", category="Healthy",
                   ingredients="Cooked quinoa, Cucumber, Tomatoes, Feta cheese, Olive oil",
                   instructions="1. Mix quinoa and veggies. 2. Add feta and dressing.", owner_id=admin_user.id),
            Recipe(title="Zucchini Chicken Noodles 🍗", category="Healthy",
                   ingredients="Zucchinis, Grilled chicken, Garlic, Pesto, Olive oil",
                   instructions="1. Peel zucchinis into ribbons. 2. Sauté with garlic for 2 mins. 3. Toss with chicken and pesto.",
                   owner_id=admin_user.id),
            Recipe(title="Cinnamon Baked Apples 🍎", category="Healthy",
                   ingredients="1 Apple, Cinnamon, 1 tsp Honey, Walnuts",
                   instructions="1. Slice apples. 2. Top with cinnamon/honey. 3. Microwave for 2 mins. Add walnuts.",
                   owner_id=admin_user.id),
        ]

        db.add_all(recipes)
        db.commit()
        print(f"✅ DONE! {len(recipes)} Rashify recipes are now in the database!")

    except Exception as e:
        print(f"❌ Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()