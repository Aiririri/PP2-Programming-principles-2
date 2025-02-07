def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return "Noor"


chickens, rabbits = solve(35, 94)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")
