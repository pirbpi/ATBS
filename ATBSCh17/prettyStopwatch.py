#! python3
# prettyStopwatch.py - Allow for a lapping stopwatch, printed in a prettier format
import time
# Display the program's instructions
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()  # Press Enter to begin
print('Started.')
startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2))
        totalTime = str(round(time.time() - startTime, 2))
        # print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNumString = 'Lap #' + str(lapNum).ljust(3)
        print(lapNumString, end='')
        # print(str(totalTime) + ' ('.ljust(len(lapNumString)), end='')
        print(str(totalTime) + ' (' + str(lapTime) + ')'.rjust(0))
        lapNum += 1
        lastTime = time.time()  # Reset the last lap time

except KeyboardInterrupt:
    # Handle the Ctrl-C exception
    print('\nDone.')
