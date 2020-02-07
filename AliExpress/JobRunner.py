import os
import sys
import threading
import time

class Webscrape(threading.Thread):
    def run(self):
        print("running command: " + command)
        print("\n")
        os.system(command)

node_number = 0
increment_number = 100
numThreads = 20
#start_number = 32965410914+(increment_number*node_number*numThreads)
start_number = 32995028266+(increment_number*node_number*numThreads)
end_number = start_number+increment_number

#os.mkdir('Scans')
print("Running the script : test.py....\n")
print("Starting and running thread 1")

for t in range(numThreads):

    command = "python AliScraper.py " + str(start_number)+ " " + str(end_number)
    print(command)
    t = Webscrape()
    t.start()
    time.sleep(.4)

    start_number = end_number + 1
    end_number = start_number + increment_number



while(threading.active_count()!=1):
    list = threading.enumerate()
    for each in list:
        print(each)

    time.sleep(25)

