print([[int(n) for n in line.split(", ") if int(n)%2 == 0] for line in [input() for _ in range(int(input()))]])