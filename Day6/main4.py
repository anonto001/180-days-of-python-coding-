# Get the distance traveled from the user
distance = float(input("Enter the distance traveled in kilometers: "))

# Define the base fare and the fare per kilometer
base_fare = 5.00
fare_per_km = 2.50

# Calculate the total fare based on the distance
total_fare = base_fare + (fare_per_km * distance)

# Check for any discounts based on the total fare
if total_fare > 50.00:
    total_fare -= 10.00

# Output the total fare to the user
print("The total fare for the taxi ride is $", total_fare)
