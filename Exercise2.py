import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp_H = time.strftime('%H')
hour = int(timestamp_H) + 5 
print("Hour:",hour)
timestamp_M = time.strftime('%M')
minutes = int(timestamp_M) + 30 
sum = minutes
print("sum:",sum)
if (sum >= 59):
  hour = hour + 1
  minutes = minutes - 60
if (minutes >= 59):
  minutes = minutes - 30
print("Minutes:",minutes)
Seconds = time.strftime('%S')
print("Seconds:",Seconds)

print(int(hour),':',int(minutes),':',Seconds)
if (hour >= 0 and hour < 12):
  print("Good Morning")
elif(hour >= 12 and hour < 17):
  print("Good Afternoon")
elif(hour >= 17 and hour < 20):
  print("Good Evening")
elif(hour >= 20 and hour < 24):
  print("Good Night")
  
  