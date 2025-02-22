from datetime import datetime
start = datetime.now()
seconds = set()
while 1:
    current = datetime.now()
    hour = current.hour - start.hour
    minute = current.minute - start.minute
    second = current.second - start.second
    print(hour, minute, second)

