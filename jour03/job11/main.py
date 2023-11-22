def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        if hours == 1:
            hours_text = "1 heure"
        else:
            hours_text = str(hours) + " heures"
        
        if remaining_minutes == 1:
            minutes_text = "1 minute"
        else:
            minutes_text = str(remaining_minutes) + " minutes"
        
        print(hours_text + " et " + minutes_text)


time_to_text(145)
