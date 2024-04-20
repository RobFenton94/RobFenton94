def calculate_total_time(swimming_time, cycling_time, running_time):
    """
    calculate the total time taken to complete the triathlon
    """
    return swimming_time + cycling_time + running_time

def determine_award(total_time):
    """
    determine award granted based on total time taken
    """
    if total_time <= 100:
        return "Provincial colours"
    elif 100< total_time <= 105:
        return "Provincial half colours"
    elif 105 <total_time <= 110:
        return "Provincial scroll"
    else:
        return "No award"
    
# times in minutes for all three events
swimming_time = float(input("Enter swimming time (minutes): "))
cycling_time = float(input("Enter cycling time (minutes): "))
running_time = float(input("Enter running time (minutes): "))

# calculate the total time taken to complete the triathlon
total_time = calculate_total_time(swimming_time, cycling_time, running_time)

# determine award based on time taken
award = determine_award(total_time)

# display the total time and which award is granted
print(f"Total time taken: {total_time} minutes")
print("Award:", award)
