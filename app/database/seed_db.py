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
            Recipe(
                title="Shakshuka 🍳",
                category="Breakfast",
                ingredients="4 Eggs, 3 Tomatoes, 1 Onion, 2 Garlic cloves, 1 Bell pepper, 2 tbsp Olive oil, Cumin, Salt, Black pepper",
                instructions="1. Sauté chopped onion, garlic, and pepper in olive oil until soft. 2. Add chopped tomatoes and spices, simmer for 10 mins. 3. Crack eggs on top, cover and cook for 5 mins until eggs are set.",
                calories=320, time=15, image_path="assets/images/shakshuka.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Fava Beans (Foul) 🧆",
                category="Breakfast",
                ingredients="1 can Fava beans, 3 tbsp Olive oil, 1 Lemon (juiced), 1 clove Garlic (minced), 1/2 tsp Cumin, Fresh parsley, Chopped tomatoes",
                instructions="1. Heat the beans in a pot and mash them slightly. 2. Add garlic, lemon juice, and cumin; mix well. 3. Pour into a serving dish, top with olive oil, parsley, and tomatoes.",
                calories=280, time=10, image_path="assets/images/foul.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Hummus with Tahini 🥣",
                category="Breakfast",
                ingredients="2 cups Cooked chickpeas, 1/2 cup Tahini, 1/4 cup Lemon juice, 1 Garlic clove, Salt, Ice water, Olive oil, Paprika",
                instructions="1. Blend chickpeas, garlic, and salt in a food processor. 2. Gradually add tahini and lemon juice, then ice water until smooth. 3. Serve in a bowl with a well of olive oil and a sprinkle of paprika.",
                calories=350, time=15, image_path="assets/images/hummus.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Labneh with Zaatar 🥛",
                category="Breakfast",
                ingredients="1 cup Labneh, 2 tbsp Zaatar, 3 tbsp Extra virgin olive oil, Fresh mint, Black olives, Sliced cucumbers",
                instructions="1. Spread the labneh on a small plate using a spoon to create a swirl. 2. Sprinkle zaatar in the center and drizzle generously with olive oil. 3. Garnish with mint, olives, and serve with bread.",
                calories=210, time=5, image_path="assets/images/labneh.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Falafel with Arabic Bread 🥙",
                category="Breakfast",
                ingredients="6-8 Falafel pieces, 2 Arabic breads, Tahini sauce, Chopped pickles, Tomatoes, Mint leaves",
                instructions="1. Reheat falafel if needed. 2. Open the bread and spread a layer of tahini. 3. Stuff with crushed falafel, tomatoes, pickles, and mint.",
                calories=450, time=10, image_path="assets/images/falafel.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Hummus Fatteh 🥣",
                category="Breakfast",
                ingredients="2 cups Toasted bread cubes, 2 cups Warm chickpeas, 1 cup Yogurt, 2 tbsp Tahini, 1 Garlic clove, Roasted pine nuts, Butter",
                instructions="1. Place toasted bread in a dish and soak with a little chickpea broth. 2. Layer chickpeas over bread. 3. Mix yogurt, tahini, and garlic, pour over top. Garnish with nuts fried in butter.",
                calories=520, time=20, image_path="assets/images/fatteh.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Honey Pancakes 🥞",
                category="Breakfast",
                ingredients="1 cup Flour, 1 cup Milk, 1 Egg, 2 tbsp Sugar, 1 tsp Baking powder, Butter, Honey, Berries",
                instructions="1. Whisk flour, sugar, and baking powder. Add egg and milk; mix until smooth. 2. Cook small ladles of batter on a buttered pan until bubbles form, then flip. 3. Stack and serve with honey and fruit.",
                calories=380, time=20, image_path="assets/images/pancakes.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="French Toast 🍞",
                category="Breakfast",
                ingredients="2 slices Thick bread, 2 Eggs, 1/4 cup Milk, 1/2 tsp Cinnamon, 1/2 tsp Vanilla, Butter, Maple syrup",
                instructions="1. Whisk eggs, milk, cinnamon, and vanilla in a shallow bowl. 2. Dip bread slices into the mixture until soaked. 3. Fry in a buttered pan until golden on both sides. Serve with syrup.",
                calories=410, time=12, image_path="assets/images/french_toast.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Avocado Toast with Egg 🥑",
                category="Breakfast",
                ingredients="1 slice Sourdough bread, 1/2 ripe Avocado, 1 Fried or Poached egg, Lemon juice, Chili flakes, Salt",
                instructions="1. Toast the bread. Mash avocado with lemon and salt, then spread on toast. 2. Top with the egg. 3. Sprinkle with chili flakes and serve immediately.",
                calories=340, time=10, image_path="assets/images/avocado_egg.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Cheese & Veggie Omelette 🍳",
                category="Breakfast",
                ingredients="3 Eggs, 1/4 cup Cheddar cheese, 2 tbsp Chopped bell peppers, 1 tbsp Onions, Salt, Pepper, Butter",
                instructions="1. Whisk eggs with salt and pepper. 2. Sauté peppers and onions in butter, then pour in eggs. 3. When set, sprinkle cheese on one side, fold over, and cook until melted.",
                calories=310, time=8, image_path="assets/images/omelette.png",
                owner_id=admin_user.id
            ),
            Recipe(
                title="Waffles with Fruits 🧇",
                category="Breakfast",
                ingredients="2 Waffles, 1/2 cup Whipped cream, Sliced strawberries, Blueberries, Maple syrup",
                instructions="1. Toast waffles until crispy. 2. Top with a dollop of whipped cream and fresh fruits. 3. Drizzle with maple syrup and serve.",
                calories=420, time=15, image_path="assets/images/waffles.png",
                owner_id=admin_user.id
            ),
        ]
        recipes = [
            Recipe(
                title="Jordanian Mansaf 🍖",
                category="Lunch",
                ingredients="1kg Lamb, 500g Jameed, 2 cups Rice, Shrak bread, Almonds, Pine nuts, Turmeric, Ghee",
                instructions="1. Cook lamb in water with spices until half-done. 2. Blend jameed and add to the meat broth; simmer until tender. 3. Lay shrak bread, top with rice and meat, then pour sauce and garnish with nuts.",
                calories=950, time=120, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Maqluba 🍲",
                category="Lunch",
                ingredients="1 Chicken, 2 cups Rice, 1 Eggplant, 1 Cauliflower, 2 Potatoes, Maqluba spices, Onions",
                instructions="1. Fry eggplant, cauliflower, and potatoes. 2. Cook chicken with spices. 3. Layer veggies and chicken in a pot, cover with rice and broth. Cook then flip upside down.",
                calories=620, time=70, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Kabsa 🇸🇦",
                category="Lunch",
                ingredients="Chicken, Basmati rice, Kabsa spices, Tomatoes, Onions, Raisins, Almonds",
                instructions="1. Sauté onions and chicken with spices and tomato puree. 2. Add water and cook chicken. 3. Add rice to the broth and cook until fluffy. Serve with roasted nuts.",
                calories=580, time=55, owner_id=admin_user.id
            ),
            Recipe(
                title="Stuffed Zucchini & Eggplant 🍆",
                category="Lunch",
                ingredients="Zucchini, Eggplant, Rice, Minced meat, Tomato paste, Garlic, Dried mint",
                instructions="1. Core the veggies. 2. Mix rice, meat, and spices; stuff the veggies. 3. Simmer in tomato sauce with garlic and mint until tender.",
                calories=450, time=90, owner_id=admin_user.id
            ),
            Recipe(
                title="Vine Leaves (Warak Enab) 🍇",
                category="Lunch",
                ingredients="Vine leaves, Rice, Parsley, Tomatoes, Lemon juice, Olive oil, Lamb ribs (optional)",
                instructions="1. Mix rice with herbs and spices. 2. Roll the leaves tightly. 3. Layer in a pot with lemon and oil; slow cook for 3 hours.",
                calories=480, time=180, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Musakhan 🇵🇸",
                category="Lunch",
                ingredients="Taboon bread, 1kg Onions, Chicken, Sumac, Extra virgin olive oil, Pine nuts",
                instructions="1. Sauté onions in plenty of olive oil and sumac. 2. Roast chicken separately. 3. Dip bread in oil, layer with onions and chicken, then bake for 5 mins.",
                calories=780, time=60, owner_id=admin_user.id
            ),
            Recipe(
                title="Molokhia with Rice 🍃",
                category="Lunch",
                ingredients="Minced Molokhia, Chicken broth, Garlic, Coriander, Chicken, Vermicelli rice",
                instructions="1. Boil chicken for broth. 2. Cook molokhia in broth. 3. Make 'Taklia' by frying garlic and coriander, pour over molokhia. Serve with rice.",
                calories=420, time=45, owner_id=admin_user.id
            ),
            Recipe(
                title="Mujadara 🍛",
                category="Lunch",
                ingredients="Brown lentils, Rice (or Bulgur), Plenty of onions, Olive oil, Cumin",
                instructions="1. Boil lentils until half-done. 2. Add rice and cumin; cook together. 3. Top with crispy deep-fried onion slices.",
                calories=380, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Fatteh 🥣",
                category="Lunch",
                ingredients="Shredded chicken, Toasted bread, Yogurt, Tahini, Garlic, Chickpeas, Pine nuts",
                instructions="1. Layer bread and chickpeas. 2. Add shredded chicken and broth. 3. Cover with yogurt-tahini mix and garnish with sizzling nuts.",
                calories=510, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title="Shish Tawook with Rice 🍢",
                category="Lunch",
                ingredients="Chicken breast, Yogurt, Garlic, Mustard, Lemon, Paprika, Basmati rice",
                instructions="1. Marinate chicken and grill on skewers. 2. Cook yellow rice with turmeric. 3. Serve grilled chicken over rice with garlic sauce.",
                calories=490, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Pasta Bolognese 🍝",
                category="Lunch",
                ingredients="Spaghetti, Minced beef, Tomato sauce, Onion, Garlic, Herbs, Parmesan",
                instructions="1. Sauté meat with onions and garlic. 2. Add tomato sauce and herbs; simmer. 3. Mix with boiled pasta and top with cheese.",
                calories=520, time=35, owner_id=admin_user.id
            ),
            Recipe(
                title="Classic Lasagna 🥘",
                category="Lunch",
                ingredients="Lasagna sheets, Bolognese sauce, Béchamel sauce, Mozzarella, Parmesan",
                instructions="1. Layer pasta, meat sauce, and bechamel in a dish. 2. Repeat layers. 3. Top with cheese and bake for 45 mins.",
                calories=680, time=60, owner_id=admin_user.id
            ),
            Recipe(
                title="Fettuccine Alfredo ⚪",
                category="Lunch",
                ingredients="Fettuccine pasta, Heavy cream, Butter, Garlic, Parmesan cheese, Black pepper",
                instructions="1. Boil pasta. 2. Melt butter with garlic, add cream and cheese until thick. 3. Toss pasta in the sauce until coated.",
                calories=720, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Steak with Potatoes 🥩",
                category="Lunch",
                ingredients="Beef steak, Potatoes, Rosemary, Butter, Garlic, Black pepper",
                instructions="1. Sear steak in a hot pan with butter and rosemary. 2. Roast or mash potatoes. 3. Serve steak with a side of potatoes.",
                calories=650, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title="Beef Burger 🍔",
                category="Lunch",
                ingredients="Beef patty, Brioche bun, Cheese, Lettuce, Tomato, Special sauce",
                instructions="1. Grill the beef patty. 2. Toast the bun. 3. Assemble with cheese, veggies, and sauce.",
                calories=710, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Pizza 🍕",
                category="Lunch",
                ingredients="Pizza dough, Tomato sauce, Mozzarella, Pepperoni, Basil",
                instructions="1. Roll the dough. 2. Spread sauce and toppings. 3. Bake at high heat for 10-15 mins.",
                calories=450, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Parmesan 🍗",
                category="Lunch",
                ingredients="Breaded chicken breast, Marinara sauce, Mozzarella, Spaghetti",
                instructions="1. Fry the breaded chicken. 2. Top with sauce and cheese; bake until melted. 3. Serve with a side of spaghetti.",
                calories=610, time=45, owner_id=admin_user.id
            ),
            Recipe(
                title="Mac & Cheese 🧀",
                category="Lunch",
                ingredients="Macaroni, Cheddar cheese, Milk, Butter, Flour, Breadcrumbs",
                instructions="1. Make a cheese sauce with butter, flour, and milk. 2. Mix with boiled macaroni. 3. Top with breadcrumbs and bake.",
                calories=550, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Caesar Salad 🥗",
                category="Lunch",
                ingredients="Grilled chicken, Romaine lettuce, Croutons, Caesar dressing, Parmesan",
                instructions="1. Grill chicken strips. 2. Toss lettuce with dressing and croutons. 3. Top with chicken and cheese shavings.",
                calories=380, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Pesto Pasta 🌿",
                category="Lunch",
                ingredients="Pasta, Basil pesto, Pine nuts, Parmesan, Olive oil, Cherry tomatoes",
                instructions="1. Boil pasta. 2. Mix with fresh pesto and a splash of pasta water. 3. Garnish with nuts and cheese.",
                calories=490, time=15, owner_id=admin_user.id
            )
        ]
        # --- Dinner (وجبات العشاء المتنوعة) ---

        recipes = [
            Recipe(
                title="Vegetable Noodles 🍜",
                category="Dinner",
                ingredients="Egg noodles, Cabbage, Carrots, Soy sauce, Ginger, Garlic, Sesame oil",
                instructions="1. Boil noodles. 2. Stir-fry garlic, ginger, and veggies in sesame oil. 3. Toss noodles with soy sauce on high heat.",
                calories=380, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Stir-Fry 🥢",
                category="Dinner",
                ingredients="Chicken breast, Broccoli, Bell peppers, Soy sauce, Honey, Cornstarch",
                instructions="1. Sauté chicken strips. 2. Add veggies and stir-fry. 3. Pour honey-soy sauce mixture and simmer until thickened.",
                calories=420, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Assorted Sushi 🍣",
                category="Dinner",
                ingredients="Sushi rice, Nori, Salmon/Tuna, Avocado, Cucumber, Rice vinegar",
                instructions="1. Spread rice on nori. 2. Place fish and veggies. 3. Roll tightly and slice into bite-sized pieces.",
                calories=320, time=45, owner_id=admin_user.id
            ),
            Recipe(
                title="Japanese Ramen 🥣",
                category="Dinner",
                ingredients="Ramen noodles, Broth, Boiled egg, Seaweed, Scallions, Soy sauce",
                instructions="1. Prepare savory broth. 2. Cook noodles. 3. Combine in a bowl and top with egg, seaweed, and onions.",
                calories=550, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title="Pad Thai 🍝",
                category="Dinner",
                ingredients="Rice noodles, Shrimp or Chicken, Bean sprouts, Peanuts, Lime, Pad Thai sauce",
                instructions="1. Soak noodles. 2. Stir-fry protein and sprouts. 3. Toss with noodles and sauce; garnish with crushed peanuts.",
                calories=480, time=25, owner_id=admin_user.id
            ),
            Recipe(
                title="Vegetable Fried Rice 🍚",
                category="Dinner",
                ingredients="Cooked rice, Peas, Carrots, Eggs, Soy sauce, Green onions",
                instructions="1. Scramble eggs in a pan. 2. Sauté veggies. 3. Add rice and soy sauce, stir-fry on high heat.",
                calories=350, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title="Sweet & Sour Chicken 🍗",
                category="Dinner",
                ingredients="Crispy chicken, Pineapple, Peppers, Vinegar, Ketchup, Sugar",
                instructions="1. Fry breaded chicken. 2. Make sauce with vinegar and ketchup. 3. Toss chicken and pineapple in the sauce.",
                calories=580, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Teriyaki 🍗",
                category="Dinner",
                ingredients="Chicken thighs, Teriyaki sauce, Garlic, Ginger, Sesame seeds",
                instructions="1. Grill chicken until golden. 2. Pour teriyaki sauce and simmer. 3. Garnish with sesame seeds and serve with rice.",
                calories=440, time=25, owner_id=admin_user.id
            ),
            Recipe(
                title="Steamed Dumplings 🥟",
                category="Dinner",
                ingredients="Dumpling wrappers, Minced meat/veggies, Cabbage, Soy-ginger dip",
                instructions="1. Fill wrappers with meat mix. 2. Pleat the edges to seal. 3. Steam for 10-12 minutes and serve with dip.",
                calories=290, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Beef Burger 🍔",
                category="Dinner",
                ingredients="Beef patty, Bun, Cheese, Lettuce, Tomato, Burger sauce",
                instructions="1. Grill the patty. 2. Toast the bun. 3. Assemble with cheese, veggies, and sauce.",
                calories=710, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Pizza Margherita 🍕",
                category="Dinner",
                ingredients="Pizza dough, Tomato sauce, Mozzarella, Basil, Olive oil",
                instructions="1. Roll dough and add sauce. 2. Add cheese and bake at 220°C for 10 mins. 3. Top with fresh basil.",
                calories=450, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title="Grilled Chicken Sandwich 🥪",
                category="Dinner",
                ingredients="Chicken breast, Toasted bread, Mayo, Lettuce, Pickles",
                instructions="1. Grill seasoned chicken. 2. Spread mayo on bread. 3. Assemble sandwich with chicken and lettuce.",
                calories=450, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Quesadilla 🌮",
                category="Dinner",
                ingredients="Tortillas, Shredded chicken, Cheddar cheese, Peppers",
                instructions="1. Sauté chicken and peppers. 2. Fill tortilla with chicken and cheese. 3. Grill on a pan until cheese melts.",
                calories=480, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title="Beef Tacos 🌮",
                category="Dinner",
                ingredients="Taco shells, Minced beef, Taco spices, Salsa, Cheese",
                instructions="1. Cook beef with spices. 2. Fill shells with meat. 3. Top with salsa, cheese, and lettuce.",
                calories=410, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title="Hot Dog 🌭",
                category="Dinner",
                ingredients="Sausage, Bun, Mustard, Ketchup, Onions",
                instructions="1. Boil or grill the sausage. 2. Place in bun. 3. Add toppings of your choice.",
                calories=350, time=10, owner_id=admin_user.id
            ),
            Recipe(
                title="Light Pasta 🍝",
                category="Dinner",
                ingredients="Pasta, Olive oil, Garlic, Chili flakes, Parsley",
                instructions="1. Boil pasta. 2. Sauté garlic and chili in oil. 3. Toss pasta with oil and fresh parsley.",
                calories=350, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title="Chicken Soup with Toast 🥣",
                category="Dinner",
                ingredients="Chicken breast, Carrots, Broth, Bread, Butter",
                instructions="1. Boil chicken and carrots in broth. 2. Toast bread with butter. 3. Serve soup hot with toast.",
                calories=290, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title="BBQ Wings 🍗",
                category="Dinner",
                ingredients="Chicken wings, BBQ sauce, Honey, Garlic powder",
                instructions="1. Bake or fry wings until crispy. 2. Toss in BBQ sauce mixture. 3. Serve with ranch dip.",
                calories=520, time=35, owner_id=admin_user.id
            ),
            Recipe(
                title="Steak Bites 🥩",
                category="Dinner",
                ingredients="Beef cubes, Butter, Garlic, Rosemary",
                instructions="1. Sear beef cubes in a hot pan. 2. Add butter, garlic, and rosemary. 3. Cook to desired doneness.",
                calories=480, time=15, owner_id=admin_user.id
            )
        ]
        # --- Salads (السلطات والمقبلات) ---

        recipes = [
            Recipe(
                title='Fattoush 🥗',
                category='Salads',
                ingredients='Lettuce, Cucumber, Tomatoes, Radish, Green onions, Mint, Toasted Arabic bread, Sumac, Pomegranate molasses, Olive oil, Lemon',
                instructions='1. Chop all vegetables into medium chunks. 2. For the dressing, mix olive oil, lemon juice, sumac, and pomegranate molasses. 3. Toss the vegetables with the dressing and top with crispy toasted bread before serving.',
                calories=160, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title='Tabbouleh 🌿',
                category='Salads',
                ingredients='3 bunches Parsley, 2 Tomatoes, 1 Onion, 2 tbsp Fine bulgur, Lemon juice, Olive oil, Dried mint, Salt',
                instructions='1. Soak bulgur in lemon juice. 2. Finely chop the parsley, tomatoes, and onion. 3. Mix all ingredients together with olive oil and salt; serve chilled.',
                calories=180, time=25, owner_id=admin_user.id
            ),
            Recipe(
                title='Greek Salad 🧀',
                category='Salads',
                ingredients='Cucumber, Tomatoes, Red onion, Kalamata olives, Feta cheese, Dried oregano, Olive oil, Lemon juice',
                instructions='1. Slice cucumbers, tomatoes, and onions. 2. Combine in a bowl with olives. 3. Top with a large cube of feta cheese, sprinkle oregano, and drizzle with olive oil and lemon.',
                calories=210, time=10, owner_id=admin_user.id
            ),
            Recipe(
                title='Caesar Salad 🥗',
                category='Salads',
                ingredients='Romaine lettuce, Croutons, Parmesan cheese, Caesar dressing (Mayonnaise, Garlic, Lemon, Anchovy paste)',
                instructions='1. Tear the lettuce into large pieces. 2. Toss with Caesar dressing and half of the parmesan cheese. 3. Top with crunchy croutons and the remaining cheese shavings.',
                calories=320, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title='Tuna Salad 🐟',
                category='Salads',
                ingredients='1 can Tuna (drained), Corn, Celery, Red onion, Mayonnaise, Lemon juice, Black pepper',
                instructions='1. Flake the tuna in a bowl. 2. Add finely chopped celery, onion, and corn. 3. Mix with mayonnaise, lemon juice, and pepper until well combined.',
                calories=290, time=10, owner_id=admin_user.id
            ),
            Recipe(
                title='Potato Salad 🥔',
                category='Salads',
                ingredients='3 Potatoes (boiled), Green onions, Parsley, Mayonnaise (or Olive oil & Lemon), Mustard, Salt',
                instructions='1. Peel and cube the boiled potatoes. 2. Add chopped green onions and parsley. 3. Mix with a dressing of mayonnaise and mustard (or oil and lemon) and season with salt.',
                calories=350, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title='Pasta Salad 🍝',
                category='Salads',
                ingredients='Fusilli pasta, Bell peppers, Black olives, Corn, Cherry tomatoes, Italian dressing (Olive oil, Vinegar, Herbs)',
                instructions='1. Boil the pasta and let it cool. 2. Mix with chopped peppers, olives, corn, and tomatoes. 3. Pour the Italian dressing over the mixture and toss well.',
                calories=410, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title='Coleslaw 🥗',
                category='Salads',
                ingredients='Green cabbage (shredded), 2 Carrots (grated), Mayonnaise, 1 tbsp Sugar, 1 tsp Vinegar, Pinch of salt',
                instructions='1. Shred the cabbage and grate the carrots. 2. In a small bowl, whisk mayonnaise, sugar, and vinegar. 3. Mix the dressing with the vegetables and refrigerate for at least 30 minutes before serving.',
                calories=150, time=15, owner_id=admin_user.id
            )
        ]
        # --- Appetizers (المقبلات والوجبات الجانبية) ---

        appetizer_recipes = [
            Recipe(
                title='Creamy Hummus 🥣',
                category='Appetizers',
                ingredients='2 cups Chickpeas (boiled), 1/2 cup Tahini, 1/4 cup Lemon juice, 1 Garlic clove, Ice cubes, Olive oil, Salt',
                instructions='1. Blend chickpeas and garlic in a food processor with an ice cube until smooth. 2. Add tahini and lemon juice while blending. 3. Serve in a shallow bowl topped with a generous amount of olive oil.',
                calories=250, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title='Baba Ganoush 🍆',
                category='Appetizers',
                ingredients='2 large Eggplants, 3 tbsp Tahini, 2 tbsp Lemon juice, 1 Garlic clove (minced), Pomegranate seeds, Olive oil',
                instructions='1. Roast the eggplants until soft, then peel and mash the flesh. 2. Mix with tahini, lemon juice, and minced garlic. 3. Garnish with olive oil and pomegranate seeds.',
                calories=180, time=35, owner_id=admin_user.id
            ),
            Recipe(
                title='Crispy Sambousek 🥟',
                category='Appetizers',
                ingredients='Sambousek dough sheets, 250g Minced meat (or Cheese), 1 Onion, Spices (Pine nuts optional)',
                instructions='1. Sauté onions and meat with spices until cooked. 2. Place a spoonful of filling on the dough and fold into triangles. 3. Deep fry in hot oil until golden brown.',
                calories=120, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title='Potato Wedges 🍟',
                category='Appetizers',
                ingredients='4 Potatoes, 2 tbsp Olive oil, 1 tsp Paprika, 1/2 tsp Garlic powder, Dried oregano, Salt',
                instructions='1. Cut potatoes into thick wedges. 2. Toss with oil and all the spices in a bowl. 3. Bake in the oven or air fryer at 200°C for 25-30 mins until crispy.',
                calories=210, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title='Mozzarella Sticks 🧀',
                category='Appetizers',
                ingredients='10 Mozzarella cheese sticks, 1/2 cup Flour, 1 Egg, 1 cup Breadcrumbs, Italian herbs',
                instructions='1. Dip cheese sticks in flour, then beaten egg, then breadcrumbs mixed with herbs. 2. Freeze for 30 mins (crucial step). 3. Fry quickly in very hot oil until golden.',
                calories=380, time=45, owner_id=admin_user.id
            ),
            Recipe(
                title='Fried Kibbeh 🥟',
                category='Appetizers',
                ingredients='500g Fine bulgur, 500g Minced meat (for crust & filling), 1 Onion, Cinnamon, Allspice, Pine nuts',
                instructions='1. Make the dough by blending bulgur with meat and onion. 2. Prepare the filling by sautéing meat with spices and nuts. 3. Shape the dough into oval shells, stuff them, and deep fry until dark golden.',
                calories=150, time=60, owner_id=admin_user.id
            ),
            Recipe(
                title='Cold Vine Leaves (Yalanji) 🍇',
                category='Appetizers',
                ingredients='Vine leaves, Rice, Parsley, Tomato, Onion, Pomegranate molasses, Olive oil, Lemon juice',
                instructions='1. Stuff vine leaves with a mixture of rice and finely chopped vegetables. 2. Slow cook in a pot with a liquid made of water, lemon, and molasses. 3. Serve cold as a refreshing appetizer.',
                calories=220, time=120, owner_id=admin_user.id
            ),
            Recipe(
                title='French Fries 🍟',
                category='Appetizers',
                ingredients='3 large Potatoes, Frying oil, Salt',
                instructions='1. Peel and cut potatoes into thin sticks. 2. Soak in cold water for 15 mins then dry well. 3. Fry in hot oil until crispy and sprinkle with salt immediately.',
                calories=310, time=20, owner_id=admin_user.id
            )
        ]
        # --- Desserts (الحلويات الشرقية والغربية) ---

        recipes = [
            Recipe(
                title='Cheese Kunafa 🧀',
                category='Desserts',
                ingredients='500g Kunafa pastry, 200g Melted butter, 300g Nabulsi or Akkawi cheese, 1 cup Sugar syrup, Pistachios',
                instructions='1. Shred the kunafa pastry and mix with melted butter. 2. Spread half in a tray, add a thick layer of desalted cheese, then cover with the rest of the pastry. 3. Bake until golden, pour cold syrup over it while hot, and garnish with pistachios.',
                calories=450, time=40, owner_id=admin_user.id
            ),
            Recipe(
                title='Baklava 🥟',
                category='Desserts',
                ingredients='Phyllo dough sheets, 2 cups Crushed walnuts or pistachios, 1 cup Melted ghee, 1.5 cups Sugar syrup',
                instructions='1. Layer phyllo sheets in a tray, brushing each with ghee. 2. Add a thick layer of nuts in the middle. 3. Top with more layers, cut into diamonds, bake until crispy, and soak in syrup.',
                calories=380, time=50, owner_id=admin_user.id
            ),
            Recipe(
                title='Harissa (Basbousa) 🍰',
                category='Desserts',
                ingredients='3 cups Semolina, 1 cup Yogurt, 1/2 cup Sugar, 1/2 cup Melted butter, 1 tsp Baking powder, Almonds, Syrup',
                instructions='1. Mix semolina, yogurt, sugar, butter, and baking powder. 2. Spread in a tray, garnish with almonds, and let it rest for 30 mins. 3. Bake until edges are brown, then broil the top and pour hot syrup.',
                calories=320, time=45, owner_id=admin_user.id
            ),
            Recipe(
                title='Maamoul 🍪',
                category='Desserts',
                ingredients='Semolina, Flour, Ghee, Rose water, Date paste (or crushed walnuts/pistachios)',
                instructions='1. Mix semolina and ghee and leave overnight. 2. Knead with flour and rose water. 3. Stuff with date paste, press into molds, and bake until slightly pale golden.',
                calories=250, time=60, owner_id=admin_user.id
            ),
            Recipe(
                title='Qatayef 🥟',
                category='Desserts',
                ingredients='Qatayef dough, Cheese or Walnut filling, Sugar syrup, Oil for frying (or butter for baking)',
                instructions='1. Stuff the circles with cheese or nuts and seal the edges tightly. 2. Fry in hot oil or brush with butter and bake. 3. Dip immediately in cold sugar syrup and serve.',
                calories=290, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title='New York Cheesecake 🍰',
                category='Desserts',
                ingredients='200g Digestive biscuits, 100g Butter, 600g Cream cheese, 1 cup Sugar, 3 Eggs, 1 tsp Vanilla, Sour cream',
                instructions='1. Crush biscuits and mix with butter for the base. 2. Beat cream cheese, sugar, eggs, and vanilla; pour over the base. 3. Bake in a water bath at 160°C for 60 mins, then refrigerate for 6 hours.',
                calories=410, time=90, owner_id=admin_user.id
            ),
            Recipe(
                title='Classic Tiramisu ☕',
                category='Desserts',
                ingredients='Ladyfingers, 250g Mascarpone cheese, 2 Eggs, 1/2 cup Espresso, 2 tbsp Cocoa powder, 1/4 cup Sugar',
                instructions='1. Dip ladyfingers quickly in coffee and layer them. 2. Mix mascarpone with egg yolks and sugar, then fold in whipped egg whites. 3. Spread cream over biscuits, repeat layers, and dust with cocoa.',
                calories=320, time=30, owner_id=admin_user.id
            ),
            Recipe(
                title='Chocolate Brownies 🍫',
                category='Desserts',
                ingredients='200g Dark chocolate, 100g Butter, 3 Eggs, 1 cup Sugar, 3/4 cup Flour, 1/4 cup Cocoa powder',
                instructions='1. Melt chocolate and butter together. 2. Whisk eggs and sugar, then stir in the chocolate. 3. Fold in flour and cocoa, bake at 180°C for 20-25 mins for a fudgy center.',
                calories=280, time=35, owner_id=admin_user.id
            ),
            Recipe(
                title='Glazed Donuts 🍩',
                category='Desserts',
                ingredients='3 cups Flour, 1/4 cup Sugar, 1 cup Warm milk, 2 tsp Yeast, 50g Butter, Glaze (Powdered sugar & milk)',
                instructions='1. Knead dough and let it rise for an hour. 2. Cut into rings and let rise again for 30 mins. 3. Fry in oil until golden and dip in sugar glaze.',
                calories=240, time=120, owner_id=admin_user.id
            ),
            Recipe(
                title='Chocolate Chip Cookies 🍪',
                category='Desserts',
                ingredients='1/2 cup Butter, 1/2 cup Brown sugar, 1 Egg, 1.5 cups Flour, 1 cup Chocolate chips, Vanilla',
                instructions='1. Cream butter and sugar, then add egg and vanilla. 2. Fold in flour and chocolate chips. 3. Scoop onto a tray and bake at 180°C for 10-12 mins.',
                calories=190, time=25, owner_id=admin_user.id
            )
        ]
        # --- Drinks (المشروبات الباردة والساخنة) ---

        recipes = [
            Recipe(
                title='Mint Lemonade 🍋',
                category='Drinks',
                ingredients='3 Lemons, Fresh mint leaves, 4 tbsp Sugar, 2 cups Water, Ice cubes',
                instructions='1. Peel lemons and remove seeds. 2. Blend lemon, mint, sugar, and water together. 3. Strain and serve in a glass with plenty of ice.',
                calories=120, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Chocolate Milkshake 🍫',
                category='Drinks',
                ingredients='2 scoops Chocolate ice cream, 1 cup Cold milk, 1 tbsp Chocolate syrup, Whipped cream',
                instructions='1. Place ice cream, milk, and syrup in a blender. 2. Blend until smooth and thick. 3. Pour into a glass and top with whipped cream and more syrup.',
                calories=450, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Strawberry Smoothie 🍓',
                category='Drinks',
                ingredients='1 cup Frozen strawberries, 1/2 cup Yogurt, 1/2 cup Milk, 1 tbsp Honey',
                instructions='1. Combine all ingredients in a blender. 2. Blend on high speed until creamy. 3. Serve immediately in a chilled glass.',
                calories=180, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Iced Coffee 🧊',
                category='Drinks',
                ingredients='Double shot Espresso (or strong coffee), 1 cup Milk, 1 tbsp Caramel or Vanilla syrup, Ice',
                instructions='1. Fill a glass with ice cubes. 2. Pour in the syrup and milk. 3. Top with the espresso and stir gently.',
                calories=150, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Mango Juice 🥭',
                category='Drinks',
                ingredients='2 ripe Mangoes, 1/2 cup Water, 1 tbsp Sugar (optional), Ice',
                instructions='1. Peel and chop mangoes. 2. Blend with water and sugar until smooth. 3. Serve cold over ice.',
                calories=160, time=7, owner_id=admin_user.id
            ),
            Recipe(
                title='Fresh Orange Juice 🍊',
                category='Drinks',
                ingredients='4-5 fresh Oranges',
                instructions='1. Cut oranges in half. 2. Squeeze using a manual or electric juicer. 3. Serve fresh immediately to retain vitamins.',
                calories=110, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Avocado Shake 🥑',
                category='Drinks',
                ingredients='1 ripe Avocado, 1.5 cups Milk, 2 tbsp Honey, 3-4 Almonds',
                instructions='1. Scoop out avocado flesh. 2. Blend with milk and honey until very creamy. 3. Garnish with crushed almonds and a drizzle of honey.',
                calories=320, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Classic Mojito 🍃',
                category='Drinks',
                ingredients='Fresh mint, 1/2 Lime (sliced), 1 tbsp Sugar, Soda water, Ice',
                instructions='1. Muddle mint, lime, and sugar in a glass. 2. Fill with crushed ice. 3. Top with soda water and stir.',
                calories=90, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Arabic Coffee ☕',
                category='Drinks',
                ingredients='3 tbsp Ground Arabic coffee, 1 tbsp Cardamom, 3 cups Water, Saffron (optional)',
                instructions='1. Boil water in a Dallah. 2. Add coffee and simmer for 15 mins. 3. Add cardamom and saffron, let it settle, then pour.',
                calories=5, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title='Cappuccino ☕',
                category='Drinks',
                ingredients='Espresso shot, 1/2 cup Milk, Cocoa powder',
                instructions='1. Prepare espresso in a cup. 2. Froth the milk until thick and foamy. 3. Pour milk over espresso and top with a sprinkle of cocoa.',
                calories=120, time=10, owner_id=admin_user.id
            ),
            Recipe(
                title='Caffe Latte 🥛',
                category='Drinks',
                ingredients='Espresso shot, 1 cup Steamed milk, thin layer of Foam',
                instructions='1. Pour espresso into a large mug. 2. Add steamed milk slowly. 3. Top with a very light layer of foam.',
                calories=150, time=8, owner_id=admin_user.id
            ),
            Recipe(
                title='Classic Tea ☕',
                category='Drinks',
                ingredients='Tea bag or loose leaves, Water, Sugar or Mint (optional)',
                instructions='1. Boil water. 2. Steep tea for 3-5 mins depending on desired strength. 3. Add sugar or fresh mint as preferred.',
                calories=2, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Karak Tea ☕',
                category='Drinks',
                ingredients='Black tea, Evaporated milk, Cardamom, Cloves, Saffron, Sugar',
                instructions='1. Boil tea with spices and sugar for 5 mins. 2. Add evaporated milk and bring to a boil again. 3. Simmer on low heat for 10 mins until rich in color.',
                calories=180, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title='Hot Chocolate 🍫',
                category='Drinks',
                ingredients='1 cup Milk, 2 tbsp Cocoa powder, 1 tbsp Sugar, Marshmallows',
                instructions='1. Heat milk in a small pot. 2. Whisk in cocoa and sugar until dissolved. 3. Pour into a mug and top with marshmallows.',
                calories=250, time=7, owner_id=admin_user.id
            ),
            Recipe(
                title='Cinnamon Milk 🥛',
                category='Drinks',
                ingredients='1 cup Milk, 1 Cinnamon stick, 1/2 tsp Ground cinnamon, 1 tbsp Honey',
                instructions='1. Warm milk with the cinnamon stick. 2. Stir in honey and ground cinnamon. 3. Serve hot, perfect for cold nights.',
                calories=160, time=10, owner_id=admin_user.id
            )
        ]
        # --- Healthy (الوجبات الصحية والدايت) ---
        recipes = [
            Recipe(
                title='Grilled Chicken Salad 🥗',
                category='Healthy',
                ingredients='150g Chicken breast, Lettuce, Cucumber, Cherry tomatoes, 1 tbsp Olive oil, Lemon, Oregano',
                instructions='1. Season chicken with oregano and grill until cooked, then slice into strips. 2. Chop all vegetables and place in a bowl. 3. Mix lemon juice and olive oil for the dressing, then toss everything together.',
                calories=280, time=20, owner_id=admin_user.id
            ),
            Recipe(
                title='Oats with Fruits 🥣',
                category='Healthy',
                ingredients='1/2 cup Rolled oats, 1 cup Skimmed milk, 1 tsp Honey, Sliced strawberries, Blueberries, Cinnamon',
                instructions='1. Cook oats with milk on medium heat until thickened. 2. Pour into a bowl and stir in honey and cinnamon. 3. Top with fresh berries and serve warm.',
                calories=250, time=10, owner_id=admin_user.id
            ),
            Recipe(
                title='Salmon with Veggies 🐟',
                category='Healthy',
                ingredients='200g Salmon fillet, Asparagus, Carrots, Lemon slices, Black pepper, 1 tsp Olive oil',
                instructions='1. Place salmon and vegetables on a baking tray. 2. Drizzle with olive oil and season with pepper and lemon juice. 3. Bake at 200°C for 15-18 minutes until the salmon is flaky.',
                calories=380, time=25, owner_id=admin_user.id
            ),
            Recipe(
                title='Quinoa Salad 🥗',
                category='Healthy',
                ingredients='1/2 cup Cooked quinoa, Parsley, Red bell pepper, Cucumber, Chickpeas, Lemon, 1 tsp Olive oil',
                instructions='1. Combine cooled quinoa with chopped vegetables and chickpeas. 2. Whisk olive oil and lemon juice together. 3. Toss the salad with the dressing and chill before serving.',
                calories=220, time=15, owner_id=admin_user.id
            ),
            Recipe(
                title='Healthy Avocado Toast 🥑',
                category='Healthy',
                ingredients='1 slice Whole-grain bread, 1/2 Avocado, 1 Boiled egg, Red pepper flakes, Lemon juice',
                instructions='1. Toast the whole-grain bread. 2. Mash avocado with a squeeze of lemon and spread on toast. 3. Top with slices of boiled egg and a pinch of red pepper flakes.',
                calories=290, time=8, owner_id=admin_user.id
            ),
            Recipe(
                title='Greek Yogurt with Honey 🍯',
                category='Healthy',
                ingredients='1 cup Greek yogurt (low fat), 1 tbsp Raw honey, 5 Raw almonds, Dash of Cinnamon',
                instructions='1. Place the yogurt in a bowl. 2. Drizzle with honey and sprinkle with cinnamon. 3. Add crushed almonds on top for a healthy crunch.',
                calories=190, time=5, owner_id=admin_user.id
            ),
            Recipe(
                title='Grilled Chicken with Broccoli 🥦',
                category='Healthy',
                ingredients='150g Chicken breast, 2 cups Broccoli florets, 1 clove Garlic, Lemon, Salt, Pepper',
                instructions='1. Grill the seasoned chicken until golden and cooked. 2. Steam the broccoli for 5 minutes, then sauté quickly with garlic. 3. Serve the chicken alongside the broccoli with a squeeze of lemon.',
                calories=310, time=25, owner_id=admin_user.id
            ),
            Recipe(
                title='Vegetable Soup 🥣',
                category='Healthy',
                ingredients='Zucchini, Carrots, Celery, Green beans, Onion, Vegetable broth, Herbs',
                instructions='1. Sauté onions, then add chopped vegetables. 2. Pour in the vegetable broth and bring to a boil. 3. Simmer for 20 minutes until veggies are tender; garnish with fresh herbs.',
                calories=150, time=30, owner_id=admin_user.id
            )
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