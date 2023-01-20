import math


def substring(sstr, subs):
    subs_start_letter = subs[0]
    subs_end_letter = subs[-1]

    if subs_end_letter != subs_start_letter and subs in sstr:
        return sstr.count(subs)

    elif subs_end_letter == subs_start_letter and subs in sstr:
        start = sstr.find(subs_start_letter)
        end = sstr.rfind(subs_end_letter)
        slicded_sstr = sstr[start:end + 1]
        return math.ceil(len(slicded_sstr) / len(subs))

    elif subs not in sstr:
        return 0


print(substring(input(), input()))
