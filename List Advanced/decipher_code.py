print(ord('H'))
print(chr(72))

text = input().split(' ')

counter = 0
answer = ''
for word in text:
    chr_convert = ''
    result = ''
    word_to_add = ''
    for letter in word:
        if letter.isdigit():
            counter += 1
            chr_convert += letter
    charr = chr(int(chr_convert))
    word_to_add = word[counter::]

    result += charr
    result += word_to_add
    sec_cr = result[1]
    last_cr = result[-1]

    result=result.replace(sec_cr, last_cr,1)
    result = result[:-1]
    result += sec_cr
    answer += result
    answer += " "

print(answer)

