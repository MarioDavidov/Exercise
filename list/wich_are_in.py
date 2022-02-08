task = 'Given two lists of strings print a new list of ' \
       'the strings that contains words from the first list' \
       ' which are substrings of any of the strings in the ' \
       'second list (only unique values)'


def func(first_str, second_str):
    splited_first_input = first_str.split(', ')
    splited_second_input = second_str.split(', ')

    result = []
    for words in splited_first_input:
        for substr in splited_second_input:
            if words in substr:
                if words in result:
                    continue
                result.append(words)
    return result


first_input = input()
second_input = input()

print(func(first_input, second_input))
