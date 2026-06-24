import time

attempt = 0
wait_time = 1
max_retries = 5

while attempt < max_retries:
    print("attempt: ",attempt+1,"wait_time:",wait_time)
    time.sleep(wait_time)
    wait_time *=2
    attempt +=1