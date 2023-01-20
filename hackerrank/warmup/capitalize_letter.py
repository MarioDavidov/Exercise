def capitalised(full_name):
    answer_two = [x.capitalize() + " " for x in full_name.split(" ")]
    return "".join(answer_two).rstrip()

    # list_of_little_names = full_name.split(" ")
    # answer = ""
    # for names in (list_of_little_names):
    #     answer += names.capitalize() + " "
    # return answer.rstrip()


print(capitalised(input()))