def jobSequencingProblem(jobs):
    jobs.sort(key=lambda x: (x[2]), reverse = True)
    result = []
    totalProfit = 0
    time = 0
    for job in jobs:
        deadline,profit = job[1], job[2]
        if deadline > time:
            result.append(job)
            totalProfit += profit
            time+=1
    return result,totalProfit

jobs = [
    ('a', 2, 100),
    ('b', 1, 19),
    ('c', 2, 27),
    ('d', 1, 25),
    ('e', 3, 15)
]
print(jobSequencingProblem(jobs))