import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    
    if min < 1 or max > 1000 or (max - min+1) < quantity or quantity < 1:
        return []

    random_nums = random.sample(range(min, max+1), quantity)

    return sorted(random_nums)


lottery_numbers = get_numbers_ticket(3,5,3)

print(f"Your lottery numbers are {lottery_numbers}")


