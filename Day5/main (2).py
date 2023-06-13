num_items = 10
price_per_item = 5.99

subtotal = num_items * price_per_item

tax_rate = 0.08  # 8% sales tax
tax_amount = subtotal * tax_rate

total_cost = subtotal + tax_amount

print("The total cost is:", total_cost)
