def bread_factory(list_of_events):
    energy = 100
    coins = 100

    events = list_of_events.split("|")
    print_res = True

    for turns in (events):
        turns = turns.split("-")
        event_or_ingredient = turns[0]
        number = int(turns[1])
        if event_or_ingredient == "rest":
            if energy == 100:
                print('You gained 0 energy.')
                print(f'Current energy: {energy}.')
            else:
                energy += number
                if energy > 100:
                    energy = 100
                print(f'You gained {number} energy.')
                print(f'Current energy: {energy}.')

        elif event_or_ingredient == "order":
            if energy >= 30:
                energy -= 30
                coins += number
                print(f'You earned {number} coins.')
            else:
                energy += 50
                print('You had to rest!')
        else:
            if coins > 0 and coins >= number:
                coins -= number
                print(f'You bought {event_or_ingredient}.')
            else:
                print(f'Closed! Cannot afford {event_or_ingredient}.')
                print_res= False
                break
    if print_res:
        print(f'Day completed!''\n'
            f'Coins: {coins}''\n'
            f'Energy: {energy}''\n')

bread_factory(input())

# You have initial energy 100 and initial coins 100. You will be given a string, representing the working day events. Each event is separated with '|' (vertical bar): "event1|event2|event3…"
# Each event contains event name or item and a number, separated by dash("{event/ingredient}-{number}")
# •	If the event is "rest": you gain energy, the number in the second part. But your energy cannot exceed your initial energy (100). Print: "You gained {0} energy.".
# After that, print your current energy: "Current energy: {0}.".
# •	If the event is "order": You've earned some coins, the number in the second part. Each time you get an order, your energy decreases with 30 points.
# o	If you have energy to complete the order, print: "You earned {0} coins.".
# o	Otherwise, you should skip the order and gain 50 energy points. Print: "You had to rest!".
# •	In any other case you are having an ingredient, you have to buy. The second part of the event, contains the coins you have to spent and remove from your coins.
# o	If you are not bankrupt (coins <= 0) you've bought the ingredient successfully, and you should print ("You bought {ingredient}.")
# o	If you went bankrupt, print "Closed! Cannot afford {ingredient}." and your bakery rush is over.
# If you managed to handle all events through the day, print on the next three lines:
# "Day completed!", "Coins: {coins}", "Energy: {energy}".
# Input / Constraints
# You will receive a string, representing the working day events, separated with '|' (vertical bar): " event1|event2|event3…".
# Each event contains event name or ingredient and a number, separated by dash("{event/ingredient}-{number}")