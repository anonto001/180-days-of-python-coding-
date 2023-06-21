def is_senior(age):
    return age >= 60

def calculate_discount(age, total_price):
    discount = 0
    if is_senior(age):
        discount = 0.10 * total_price
    return discount

def main():
    age = int(input("Enter the customer's age: "))
    total_price = float(input("Enter the total price of the groceries: "))
    discount = calculate_discount(age, total_price)
    print("The customer is eligible for a discount of $" + str(discount))

if __name__ == "__main__":
    main()
