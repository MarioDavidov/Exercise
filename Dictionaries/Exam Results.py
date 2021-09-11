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
