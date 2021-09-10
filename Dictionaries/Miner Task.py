def minor_task(commands):
    res ={}
    odd_event_cheker = 1
    current_resources = ""
    while commands != 'stop':
        if odd_event_cheker % 2 != 0:
            current_resources = commands
            if commands not in res:
                res[commands] = 0
        else:
            number = int(commands)
            res[current_resources] += number

        odd_event_cheker +=1
        commands =input()

    for key, value in res.items():
        print(f'{key} -> {value}')

minor_task(input())

# You will be given sequences of strings, each on a new line, until you receive the command "stop".
# Every odd line on the console is representing a resource (e.g. Gold, Silver, Copper, and so on) and every even - quantity.
# Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:

