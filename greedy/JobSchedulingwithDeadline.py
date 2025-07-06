def maks(jobs):
    total_cost = 0
    jobs.sort(key=lambda x: (x["profit"]), reverse = True)
    time = 0
    job_list = []
    for job in jobs:
        deadline,profit = job["deadline"], job["profit"]
        if deadline > time:
            job_list.append(job)
            total_cost += profit
            time+=1
    return job_list,total_cost

jobs = [
    {'id': 'a', 'deadline': 2, 'profit': 100},
    {'id': 'b', 'deadline': 1, 'profit': 19},
    {'id': 'c', 'deadline': 2, 'profit': 27},
    {'id': 'd', 'deadline': 1, 'profit': 25},
    {'id': 'e', 'deadline': 3, 'profit': 15}
]

print(maks(jobs))