# TODO решите задачу

import json
def task() -> float:

    fname = "input.json"
    with open(fname) as f:
        jd = json.load(f)

    summ = sum([item["score"] * item["weight"] for item in jd])
    return round(summ, 3)


print(task())
