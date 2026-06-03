import time

i = 0

while True:
    print("Hello, World from Kubernetes! # " + str(i), flush=True)
    i = i+1
    time.sleep(1.0)
