def ft_water_reminder():
    days_since = input("Days since last watering: ")
    if int(days_since) >= 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
