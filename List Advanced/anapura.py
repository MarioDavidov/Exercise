task = '''
Create a program, that lists stores and the items that can be found in them. 
You are going to be receiving commands with the information you need until you get the "End" command. 
There are three possible commands:
•	"Add->{Store}->{Item}"
o	Add the store and the item in your diary. If the store already exists, add just the item.
•	"Add->{Store}->{Item},{Item1}…,{ItemN}"
o	Add the store and the items to your notes. If the store already exists in the diary – 
add just the items to it. 
•	"Remove->{Store}"
o	Remove the store and its items from your diary, if it exists.
In the end, print the collection sorted by the count of the items in descending order
 and then by the names of the stores, again, in descending order in the following format:
Stores list:
{Store}
<<{Item}>>
<<{Item}>>
<<{Item}>>

'''
commands = input()
diary = {}
while commands != 'END':
    operation = commands.split('->')
    store = operation[1]
    if operation[0] == 'Remove':
        if store in diary:
            del diary[store]
            commands = input()
            continue
        else:
            commands = input()
            continue
    items = operation[2]
    stores_items = "".join(operation[2]).split(',')

    if operation[0] == 'Add' and len(stores_items) == 1:
        if store not in diary:
            diary[store] = [items]
    elif operation[0] == 'Add' and len(stores_items) > 1:
        if store not in diary:
            diary[store] = []
            for item in stores_items:
                diary[store].append(item)
            commands = input()
            continue
        for item in stores_items:
            if item not in diary[store]:
                diary[store].append(item)

    commands = input()

diary = dict(sorted(diary.items(), key=lambda kv: (-len(kv[1]), kv[0])))

result = 'Store list\n'

for key, value in diary.items():
    result += f'{key}\n'
    for single_item in value:
        result += f'<<{single_item}>>\n'
print(result)
