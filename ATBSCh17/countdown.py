#! python3
# countdown.py - A simple countdown script.
import time
import subprocess
timeLeft = 20
while timeLeft > 0:
    print(str(timeLeft), end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file
subprocess.Popen(['see', 'alarm.wav'])
