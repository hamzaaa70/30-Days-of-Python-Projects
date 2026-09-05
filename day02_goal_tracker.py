print("GOAL TRACKER")

goal = input("what is your target?")

target_days = int(input("in how many days you want to acheive this goal?"))


day_completed  = int(input("what is your current day of working on that goal?"))

progress = (target_days / day_completed)  * 100

days_remaining = target_days - day_completed

print("YOUR PROGRESS")

print("Goal:",goal)
print("Target days:",target_days)
print("Days Completed:",day_completed)
print("Your progress:",progress)
print("Days remaining:",days_remaining)

if progress >= 80:
    print("Your doing great")
elif progress >=50:
    print("your are doing ok")
else:
    print("your failing")
