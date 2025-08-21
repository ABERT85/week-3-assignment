def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # check if discount is 20% or more
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    # Example:
print(calculate_discount(1000, 25))  # 25% discount → 750.0
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # apply discount only if >= 20%
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for inputs
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
print(f"The final price is: {final_price:.2f}")