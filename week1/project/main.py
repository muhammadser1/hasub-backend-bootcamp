def square_generator(limit):
    num = 1
    while num <= limit:
        yield num ** 2
        num += 1

# Example usage:
generator = square_generator(5)
for square in generator:
    print(square)
