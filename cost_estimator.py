repair_cost = {
    "scratch": 2000,
    "dent": 5000,
    "crack": 7000,
    "broken_glass": 6000,
    "bumper_damage": 8000
}

def estimate_cost(damages):

    total_cost = 0

    for damage in damages:
        total_cost += repair_cost.get(damage, 0)

    return total_cost
