with open('data.csv', 'r') as file:
    data = file.read()
    values = [int(value) for value in data.split(',')]
    average = sum(values) / len(values)
    print(average)