from Engine import start_recording, stop_recording

while True:
    cmd = input("1 or 2")
    if cmd == "1":
        start_recording()
    if cmd == "2":
        stop_recording()

