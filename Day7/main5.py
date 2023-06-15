# Prompt the user to enter ages separated by commas
age_input = input("Enter the ages of the individuals (comma-separated): ")

# Split the input into a list of age values
age_values = age_input.split(",")

# Initialize variables for sum and count
total_age = 0
count = 0

# Iterate over the age values and calculate the total sum
for age in age_values:
    try:
        # Typecast each age value to an integer
        age = int(age)
        total_age += age
        count += 1
    except ValueError:
        print(f"Invalid age value: {age}")

# Calculate the average age
if count > 0:
    average_age = total_age / count
    print(f"The average age is: {average_age}")
else:
    print("No valid age values were entered.")
