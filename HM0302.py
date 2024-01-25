import random


def get_numbers_ticket(min, max, quantity):
    """generating a set of unique random numbers for the lottery"""
    lottery_generation = []
    # checking the correctness of input according to the condition
    if (minimum >= 1) and (maximum <= 1000) and (minimum <= quantity <= maximum):
        while len(lottery_generation) < quantity:
            numeric = random.randint(minimum, maximum)
            if numeric not in lottery_generation:
                lottery_generation.append(numeric)
    lottery_generation.sort()
    return lottery_generation


minimum = int(input("Enter the minimum possible number of sets: "))
maximum = int(input("Enter the maximum possible number of sets: "))
quantity = int(input("Enter the number of numbers to be selected: "))
lottery_numbers = get_numbers_ticket(minimum, maximum, quantity)
print(f"Your lottery numbers {lottery_numbers}")
