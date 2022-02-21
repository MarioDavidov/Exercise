task = '''
You will be given a number n representing how many rooms there are.
 On the next n lines for each room you will get how many chairs there are and how many of them will be taken.
  The chairs will be represented by "X"s, then there will be a space " " and a number representing the taken places.
   Example: "XXXXX 4" (5 chairs and 1 of them is left free). Keep track of the free chairs, you will need them later.
    However if you get to a room where there are more people than chairs, print the following message: 
    "{needed_chairs_in_room} more chairs needed in room {number_of_room}". 
If there is enough chairs in each room print: "Game On, {total_free_chairs} free chairs left"
Input
4
XXXX 4
XX 1
XXXXXX 3
XXX 3

Output
Game On, 4 free chairs left

'''

def func(number_of_floors):
    free_chairs = 0
    enough_chairs_in_each_room = True
    for floor in range(1,int(number_of_floors) +1):
        room = input()
        room = room.split(" ")
        seats = room[0]
        chairs = room[1]
        room_seats = seats.count('X')
        if int(room_seats) == int(chairs):
            continue
        if int(room_seats) > int(chairs):
            free_chairs += int(room_seats) - int(chairs)
        else:
            chairs_needed = int(chairs) - int(room_seats)
            print(f'{chairs_needed} more chairs needed in room {floor}')
            enough_chairs_in_each_room = False
    if enough_chairs_in_each_room:
        print(f"Game On, {free_chairs} free chairs left")

func(input())

