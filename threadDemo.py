import threading, time

print('Start of Program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target = takeANap)
threadObj.start()

print('End of program.')
