import psutil
pid = int(input("PID: "))
process = psutil.Process(pid)
m = 0
while process.is_running():
    try:
        m = max(m, process.memory_info().rss)
    except:
        break

print(f"Peak usage: {m / (1024 ** 2):.2f} MB")