"""
Class 3 - Food Combo Puzzle 🍗🍟🥤

We want to buy exactly 100 food items with exactly $100.

Prices:
- Fried Chicken 🍗 = $5
- Fries 🍟 = $3
- Nuggets 🥤 (cheap ones 😅) = $1/3

Yes… nuggets are basically free at this point 💀
"""

# Loop through possible chicken orders
for chicken in range(0, 21):  # max 20 → 20 * 5 = 100
    
    # Loop through fries
    for fries in range(0, 34):  # max 33 → 33 * 3 = 99
        
        # Remaining items are nuggets
        nuggets = 100 - chicken - fries

        # Conditions:
        # nuggets must be positive and divisible by 3
        if nuggets >= 0 and nuggets % 3 == 0:

            # Total cost check
            total_cost = 5 * chicken + 3 * fries + nuggets // 3

            if total_cost == 100:
                print(f"🍗 Chicken: {chicken:2}, 🍟 Fries: {fries:2}, 🥤 Nuggets: {nuggets:2}")
