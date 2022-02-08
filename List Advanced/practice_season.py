task = ''''Write a program, that keeps information about roads and the racers who practice on them.  
    When the practice begins, you’re going to start receiving data until you get the "END" message. There are three possible commands:
•	"Add->{road}->{racer}"
o	Add the road if it doesn't exist in your collection and add the racer to it.
•	"Move->{currentRoad}->{racer}->{nextRoad}"
o	Find the racer on the current road and move him to the next one, only if he exists in the current road. B
oth roads will always be valid and will already exist.
•	"Close->{road}"
o	Find the road and remove it from the sessions, along with the racers on it if it exists.
In the end, print all of the roads with the racers who have practiced and ordered by the count of the racers in descending order, then by the roads in ascending order. The output must be in the following format:
'''
lines = input()
road_colection = {}
while lines != 'END':
    command = lines.split("->")
    operator = command[0]

    if operator == "Add":
        road = command[1]
        racer = command[2]
        if road not in road_colection:
            road_colection[road] = [racer]
        else:
            road_colection[road].append(racer)

    elif operator == "Move":
        current_road = command[1]
        racer = command[2]
        next_road = command[3]

        if racer in road_colection[current_road]:
            road_colection[next_road].append(racer)
            road_colection[current_road].remove(racer)

    elif operator == "Close":
        road = command[1]
        if road in road_colection:
            del road_colection[road]

    lines = input()

road_colection = dict(sorted(road_colection.items(), key=lambda kv: (len(kv[0]), kv[0])))

result = 'Practice session:\n'

for key, value in road_colection.items():
    result += f'{key}\n'
    for v in value:
        result += f'++{v}\n'
print(result)
