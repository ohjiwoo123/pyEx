def SecondConverter2(x):
    day = int(x/86400)
    x-=(day*86400)
    hour = int(x/3600)
    x-=(hour*3600)
    min = int(x/60)
    x -= (min*60) 
    sec = x
    
    print("Your input is equal to ",day, " days, ", hour, " hours, ", min, " minutes, and ", sec, "seconds.")
SecondConverter2(-100000)
#gives 1 day, 3 hours, 46 minutes, and 40 seconds.

