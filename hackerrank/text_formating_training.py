num_of_lines = int(input())
result = []
for i in range(num_of_lines):
    command = input().split(" ")
    operation = command[0]

    if operation == "insert":
        position = command[1]
        element = command[2]
        result.insert(int(position), int(element))

    elif operation == "print":
        print(result)

    elif operation == "remove":
        element = int(command[1])
        result.remove(element)

    elif operation == "append":
        element = int(command[1])
        result.append(element
                      )
    elif operation == "sort":
        result.sort()

    elif operation == "pop":
        result.pop()

    elif operation == "reverse":
        result.reverse()


