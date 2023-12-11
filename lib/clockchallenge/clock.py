def clock(period, hour, minute):
    if period.lower() == "am":
        if hour == 12:
            hour = 0
    else:
        if hour !=12:
            hour += 12
    return f"{hour:02d}{minute:02d}"


print(clock("am", 8, 30))
print(clock("pm", 8, 30))



           
