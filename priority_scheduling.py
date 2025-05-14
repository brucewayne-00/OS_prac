processes = [(1, 0, 10, 2), (2, 0, 1, 1), (3, 0, 2, 3)]  # (id, arrival, burst, priority)
processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival and priority
time = 0
for p in processes:
    start = max(time, p[1])
    time = start + p[2]
    print(f"Process {p[0]} started at {start}, finished at {time}")
