task = """
On the first line, you will be given the population (numbers separated by comma and space ", "). 
On the second line, you will be given the minimum wealth. 
You should distribute the wealth so that no part of the population has less than the minimum wealth. 
To do that, you should always take wealth from the wealthiest part of the population. 
There will be cases where the distribution will not be possible. 
In that case, print: "No equal distribution possible". 
"""

population = input().split(', ')
minimum_wealth_needed = int(input())
population = list(map(lambda x: int(x), population))
action = None
wealthiest_country = 0

while True:
    if sum(population) < len(population) * minimum_wealth_needed:
        print('No equal distribution possible')
        break

    for c in range(len(population)):
        if int(population[c]) >= wealthiest_country:
            wealthiest_country = c

    for c in range(len(population)):
        action = 0
        if (population[c]) < minimum_wealth_needed:
            action += 1
            population[wealthiest_country] -= minimum_wealth_needed - population[c]
            population[c] += minimum_wealth_needed - population[c]
            for c in range(len(population)):
                if int(population[c]) >= wealthiest_country:
                    wealthiest_country = c
    if action == 0:
        print(population)
        break
