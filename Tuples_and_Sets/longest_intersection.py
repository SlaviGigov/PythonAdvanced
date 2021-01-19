def print_result(data):
    print(f"Longest intersection is {list(data)} with length {len(data)}")


def is_it_longest(longest, a, b):
    current = a.intersection(b)
    if len(current) > len(longest):
        return current
    else:
        return longest


def create_set(data):
    start, end = data.split(",")
    ss = set()
    for n in range(int(start), int(end) + 1):
        ss.add(n)
    return ss


def create_two_sets(data):
    first, second = data.split("-")
    a = create_set(first)
    b = create_set(second)
    return a, b


longest = set()
for _ in range(int(input())):
    a, b = create_two_sets(input())
    longest = is_it_longest(longest, a, b)

print_result(longest)