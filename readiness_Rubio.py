print("Hello, I am Chris Rubio, and my student ID is R02249165.")

def get_stats(numbers):
    mean = sum(numbers) / len(numbers)
    maximum = max(numbers)
    return mean, maximum

numbers = [10, 20, 30, 40, 50]

mean, maximum = get_stats(numbers)

print("Mean:", mean)
print("Maximum:", maximum)