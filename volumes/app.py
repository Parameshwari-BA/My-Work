import time
file_path = "/data/info.txt"
while True:
    with open(file_path, "a") as f:
        f.write("New line written to file...\n")
    print("Line added to file.")
    time.sleep(5)
