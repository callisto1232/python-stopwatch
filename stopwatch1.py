from datetime import datetime
start = datetime.now()
seconds = set()
while 1:
    current = datetime.now()
    elapsed = (current - start).total_seconds()
    hour = int(elapsed // 3600)
    minute = int((elapsed % 3600) // 60)
    second = int(elapsed % 60)
    if second not in seconds:
        seconds.add(second)
        print(f"{round(elapsed)} \t {current}")
    if second == 59:
        seconds = set()

