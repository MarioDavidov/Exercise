# As a good friend, you decide to buy presents for your friends.
# Create a program that helps you plan the gifts for your friends and family. First, you are going to receive the gifts you plan on buying on a single line, separated by space, in the following format:
# "{gift1} {gift2} {gift3}… {giftn}"
# Then you will start receiving commands until you read the "No Money" message. There are three possible commands:
# •	"OutOfStock {gift}"
# o	Find the gifts with this name in your collection, if there are any, and change their values to "None".
# •	"Required {gift} {index}"
# o	Replace the value of the current gift on the given index with this gift if the index is valid.
# •	"JustInCase {gift}"
# o	Replace the value of your last gift with this one.
# In the end, print the gifts on a single line, except the ones with value "None", separated by a single space in the following format:
# "{gift1} {gift2} {gift3} … {giftn}"
# Input / Constraints
# •	On the 1st line you are going to receive the names of the gifts, separated by a single space.
# •	On the next lines, until the "No Money" command is received, you will be receiving commands.
# •	The input will always be valid.
# •	Index is valid when it is between 0 and length of the list – 1.

def Easter(gifts):
    list_gifts = gifts.split(" ")
    while True:

        command = input()

        if command == 'No Money':
            break

        command = command.split(" ")

        operation = command[0]

        if operation == 'OutOfStock':
            gift = command[1]
            if gift in list_gifts:
                for gt in range (len(list_gifts)):
                    if list_gifts[gt] == gift:
                        list_gifts[gt] = 'None'

        elif operation == 'Required':
            gift = command[1]
            index = int(command[2])
            if len(list_gifts) > index >= 0:
                list_gifts[index] = gift

        elif operation =='JustInCase':
            gift = command[1]
            list_gifts[-1] = gift

    result = [x for x in list_gifts if x != "None"]
    list_with_Nones = [ x for x in list_gifts if x == "None"]
    print(" ".join(result))
    print(" ".join(list_with_Nones))

Easter(input())
