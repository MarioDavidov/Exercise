def exam_task(lines):
    exam_lang = {}
    stud_points = {}
    while lines != 'exam finished':
        inpts = lines.split('-')
        name = inpts[0]
        lang = inpts[1]

        if len(inpts) > 2:
            points = int(inpts[2])
        else:
            stud_points.pop(name)
            lines = input()
            continue

        if lang not in exam_lang:
            exam_lang[lang] = 0
        exam_lang[lang] += 1

        if name not in stud_points:
            stud_points[name] = {lang: points}
        else:
            if lang not in stud_points[name]:
                stud_points[name].update({lang: points})
            else:
                if stud_points[name][lang] < points:
                    stud_points[name][lang] = points

        lines = input()

    res = {}

    for key, value in stud_points.items():
        for v in value.values():
            res[key] = v

    res = dict(sorted(res.items(), key=lambda kv: (-kv[1], kv[0])))
    exam_lang = dict(sorted(exam_lang.items(), key=lambda kv: (-kv[1], kv[0])))

    result = "Results:\n"
    for k, v in res.items():
        result += f"{k} | {v}\n"

    lang_count_result = "Submissions:\n"
    for k, v in exam_lang.items():
        lang_count_result += f"{k} - {v}\n"

    print(result.rstrip())
    print(lang_count_result)


exam_task(input())

''''will be receiving lines in the following format: "{username}-{language}-{points}" until you receive "exam finished". You should store each username and his submissions and points. 
You can receive a command to ban a user for cheating in the following format: "{username}-banned". In that case, you should remove the user from the contest, but preserve his submissions in the total count of submissions for each language.
After receiving "exam finished" print each of the participants, ordered descending by their max points, then by username, in the following format:
Results:
{username} | {points}
…
After that print each language, used in the exam, ordered descending by total submission count and then by language name, in the following format:
Submissions:
{language} - {submissionsCount}
…
Input / Constraints
Until you receive "exam finished" you will be receiving participant submissions in the following format: "{username}-{language}-{points}".
You can receive a ban command -> "{username}-banned"
The points of the participant will always be a valid integer in the range [0-100];
Output
•	Print the exam results for each participant, ordered descending by max points and then by username, in the following format: 
Results:
{username} | {points}
…
•	After that print each language, ordered descending by total submissions and then by language name, in the following format:
Submissions:
{language} - {submissionsCount}
…
•	Allowed working time / memory: 100ms / 16MB.
Input	
Pesho-Java-84
Gosho-C#-84
Gosho-C#-70
Kiro-C#-94
exam finished

Output	
Results:
Kiro | 94
Gosho | 84
Pesho | 84
Submissions:
C# - 3
Java - 1
'''''

