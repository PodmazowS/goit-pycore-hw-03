import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:

    amount = quantity
    random_nums = set()

    if min < 1 or max > 1000 or max - min < quantity:
        return []
    else:
        while amount != 0:
            random_nums.add(random.randint(min,max))
            amount -= 1

    return sorted(list(random_nums))


lottery_numbers = get_numbers_ticket(3,10,9)

print(f"Your lottery numbers are {lottery_numbers}")


