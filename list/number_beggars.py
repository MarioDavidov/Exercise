task = '''Your task here is pretty simple: given a list of numbers and a number of beggars, you are supposed to 
return a list with the sum of what each beggar brings home, assuming they all take regular turns, from the first to 
the last. For example: [1,2,3,4,5] for 2 beggars will return a result of 9 and 6, as the first one takes [1,3,5], 
the second collects [2,4]. The same list with 3 beggars would produce a better outcome for the second beggar: 5, 
7 and 3, as they will respectively take [1, 4], [2, 5] and [3]. Also note that not all beggars have to take the same 
amount of "offers", meaning that the length of the list is not necessarily a multiple of n; length can be even 
shorter, in which case the last beggars will of course take nothing (0). '''

def taks_function(list, num_of_begg):
    list = list.split(',')
    offers = [int(x) for x in list]
    result = {}

    for beggars in range(1, num_of_begg + 1):
        result[beggars] = 0
    beggar_counter = 1
    for offe in offers:
        if beggar_counter in result:
            result[beggar_counter] += offe
            beggar_counter += 1
        else:
            beggar_counter = 1
            result[beggar_counter] += offe
            beggar_counter += 1

    answer = []
    for k, v in result.items():
        answer.append(v)
    return (answer)
list_with_nums = (input())
count_beggars = int(input())

print(taks_function(list_with_nums, count_beggars))
