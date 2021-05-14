import time
 
localtime = time.asctime( time.localtime(time.time()) )
print("Start: ", localtime, "\n")
start = time.time() #start time
 
ticks = 0
while time.time() < start + 10:
   ticks = ticks + 1
localtime = time.asctime( time.localtime(time.time()) )
print("End: ", localtime, "\n")

print("Ticks: ", ticks, "\n")
