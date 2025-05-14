processes = [(1, 0, 3), (2, 1, 6), (3, 2, 1)]  # (id, arrival, burst)
processes.sort(key=lambda x: x[1])
time = 0
for p in processes:
    start = max(time, p[1])
    time = start + p[2]
    print(f"Process {p[0]} started at {start}, finished at {time}")
