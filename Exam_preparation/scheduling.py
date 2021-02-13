# jobs = [int(el) for el in input().split(", ")]
# target_index = int(input())
# target_job = jobs[target_index]
# cycles = 0
# dublle = False
#
# for job in jobs:
#     if jobs.index(job) < target_index and job == target_job:
#         cycles += job
#         dublle = True
#     elif job < target_job:
#         cycles += job
#
# if dublle:
#     print(cycles)
# else:
#     print(cycles + target_job)

# Correct but ridiculous

# Doncho solution
def read_input():
    return([3, 1, 10, 1, 2], 0)

def min_cycles_for_job(jobs, job_index):
    sorted_jobs = sorted([(value, index) for (index, value) in enumerate(jobs)])
    cycles = 0
    for (job, index) in sorted_jobs:
        cycles += job
        if index == job_index:
            break
    return cycles

def using_heap(jobs, job_index):
    from heapq import heapify, heappop, heappush
    heap = []
    for (index, job) in enumerate(jobs):
        heappush(heap, (job, index))

    cycles = 0
    while True:
        (job, index) = heappop(heap)
        cycles += job
        if index == job_index:
            break

    return cycles


def print_result(result):
    print(result)

jobs, job_index = read_input()
# result = min_cycles_for_job(jobs, job_index)
result = using_heap(jobs, job_index)
print(result)

# using heap


