from textwrap import wrap

string, k = input(), int(input())


def merge_the_tools(string, k):
    wrapped_text = wrap(string, k)

    for substring in wrapped_text:
        substring_to_add_in_Result = ''
        for letter in substring:
            if letter not in substring_to_add_in_Result:
                substring_to_add_in_Result += letter
        print(substring_to_add_in_Result)

(merge_the_tools(string,k))
