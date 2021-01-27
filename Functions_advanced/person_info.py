def get_info(**kwargs):
    info = []
    for _ in range(len(kwargs)):
        for k, v in kwargs.items():
            info.append(v)
    return f"This is {info[0]} from {info[1]} and he is {info[2]} years old"

# 100/100 - too slow and complicated with list. While the solution is one line

def get_info_lab(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"

print(get_info_lab(**{"name": "George", "town": "Sofia", "age": 20}))
