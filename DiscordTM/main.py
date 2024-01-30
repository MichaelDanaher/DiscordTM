import subprocess

print("Please run all in different terminals.")
question = input("1 to Start Monitoring Incoming Messages , 2 to Start Sending Messages, and 3 for Startup, and 4 to Exit: ")

# eh, starts stuff. sometimes throws an error but it doesnt stop running so idc 
if question == "1":
    print("Starting message logger...")
    subprocess.run(["python", "listen.py"])
elif question == "2":
    print("Starting message sender...")
    subprocess.run(["python", "portal.py"])
elif question == "3":
    print("Entering Setup...")
    subprocess.run(["python", "setup.py"])
elif question == "4":
    print("Exiting program.")
    exit()
else:
    print("Invalid input. Exiting program.")
    exit()