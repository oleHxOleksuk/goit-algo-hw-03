from random import randint

def get_numbers_ticket(min:int, max:int, quantity:int):
    if not (1<=min<max<=1000):
        return []
    lottery_numbers = set()
    while len (lottery_numbers) != quantity:
        lottery_numbers.add(randint(min, max))
    return list(lottery_numbers)

print(get_numbers_ticket(1, 30, 10))