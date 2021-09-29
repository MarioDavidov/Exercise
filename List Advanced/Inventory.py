def inventory(items):
    items = items.split(', ')
    commands = input().split(' - ')
    while commands[0] != 'Craft!':

        operation = commands[0]

        if operation == 'Collect':
            item = commands[1]
            if item not in items:
                items.append(item)

        elif operation == 'Drop':
           item = commands[1]
           if item in items:
               items.remove(item)

        elif operation == 'Combine Items':
            old_new_items = commands[1].split(':')
            old_item = old_new_items[0]
            new_item = old_new_items[1]

            if old_item in items:
                index = items.index(old_item)
                items.insert(index + 1, new_item)

        elif operation == 'Renew':
            item = commands[1]

            if item in items:
                items.remove(item)
                items.append(item)

        commands = input().split(' - ')

    print(", ".join(items))

inventory(input())


'''You will receive a journal with some Collecting items, separated with ', ' (comma and space). After that, until receiving "Craft!" you will be receiving different commands. 
Commands (split by " - "):
•	"Collect - {item}" – Receiving this command, you should add the given item to your inventory. If the item already exists, you should skip this line.
•	"Drop - {item}" – You should remove the item from your inventory if it exists.
•	"Combine Items - {oldItem}:{newItem}" – You should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
•	"Renew – {item}" – If the given item exists, you should change its position and put it last in your inventory.
Output
After receiving "Craft!" print the items in your inventory, separated by ", " (comma and space).

Input	
Iron, Sword
Drop - Bronze
Combine Items - Sword:Bow
Renew - Iron
Craft!	

Output
Sword, Bow, Iron

'''






