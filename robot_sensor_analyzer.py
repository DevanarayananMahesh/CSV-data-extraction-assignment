import csv
import numpy as np


#=============================
#  VARIABLES                    
#=============================

readings = []
unusual_readings = 0
under_20 = 0
over_60 = 0
Stop_count = 0
MoveSlow_count = 0
MoveForward_count = 0
percentage_u_readings = 0
previous_dataPoint = 0


#=============================
#  FUNCTIONS                    
#=============================


def unusual_specifics(specific):
    global under_20, over_60, unusual_readings
    unusual_readings += 1
    if specific == "under":
        under_20 += 1
    else:
        over_60 += 1

def percentage():
    if not readings:
        return 0
    return (unusual_readings / len(readings)) * 100


def summarize_sensor_data(readings_params):
    global percentage_u_readings

    if readings_params:
        percentage_u_readings = percentage()

        num_readings = len(readings_params)
        min_readings = min(readings_params)
        max_readings = max(readings_params)
        avg_readings = sum(readings_params)/len(readings_params)

        return num_readings, min_readings, max_readings, avg_readings, under_20, over_60, unusual_readings, percentage_u_readings
    else:
        print("No data found in the CSV file.")
        return 0, 0, 0, 0, 0, 0, 0, 0
        



def robot_decision(distance):
    global Stop_count, MoveSlow_count, MoveForward_count
    for value in distance:
        if value < 20:
            Stop_count += 1
        elif value > 50:
            MoveForward_count += 1
        else:
            MoveSlow_count += 1



#=======================================
#  USER THRESHOLD INPUT                    
#=======================================

# IS COMMENTED OUT AS IT WAS FOR LEVEL 3 AND LEVEL 4 REQUIRES AUTOMATED RULES TO ISOLATE INVALID DATA POINTS
# THIS BASICALLY ASKS THE USER FOR THRESHOLDS AND ENSURES THEY ARE NUMBERS


# is_valid_min_threshold = False

# while not is_valid_min_threshold:
#     user_min_threshold = input("Decide the Minimum Threshold for the data to be valid: ")
#     try:
#         testNumMin = float(user_min_threshold)
#         is_valid_min_threshold = True 
#     except ValueError:
#         print("That is not a valid number. Try again.")

# is_valid_max_threshold = False

# while not is_valid_max_threshold:
#     user_max_threshold = input("Decide the Maximum Threshold for the data to be valid: ")
#     try:
#         testNumMax = float(user_max_threshold)
#         is_valid_max_threshold = True 
#     except ValueError:
#         print("That is not a valid number. Try again.")



#=============================
#  OPEN CSV FILE                    
#=============================

# HAS ALSO BEEN TESTED WITH TEST_A.CSV FILE
with open('Robot_Sensor_Readings_1000.csv', 'r') as file:
    
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        
        current_reading = float(row["distance_cm"]) #converts to float
        readings.append(current_reading) #appends the converted value to list




#==============================================
#  DETERMINING THRESHOLD AUTOMATICALLY                    
#==============================================
current_streak = 0
longest_streak = 0

current_start = 0
longest_start = 0
longest_end = 0

# Determining IQR to auto-decide the min and max thresholds

readingsQ1, readingsQ3 = np.percentile(readings, [25, 75])  
iqr = readingsQ3 - readingsQ1

LowerFence = max(0, readingsQ1 - (1.5 * iqr))
UpperFence = readingsQ3 + (1.5 * iqr)



for i, reading in enumerate(readings):

    if reading < LowerFence or reading > UpperFence:
        if reading < LowerFence:
            unusual_specifics("under")
        else:
            unusual_specifics("over")
        
        current_streak += 1

        # beginning of new streak
        if current_streak == 1:
            current_start = i

        # Deciding whether its longest streak
        if current_streak > longest_streak:
            longest_streak = current_streak
            longest_start = current_start
            longest_end = i

    else:
        # streak is broken
        current_streak = 0
    


#=============================
#  READINGS                   
#=============================


num, min_r, max_r, avg, under_20, over_60, unusual, pct = summarize_sensor_data(readings)
robot_decision(readings)


print(f"""
Total Readings: {num}
Minimum Reading: {min_r}
Maximum Reading: {max_r}
Average Reading: {avg}
Readings under {LowerFence:.2f}: {under_20}
Readings over {UpperFence:.2f}: {over_60}
Unusual Readings: {unusual}
Unusual Readings Percentage: {pct:.2f}%
Longest Unusual Streak: {longest_streak}
Longest Streak Begins: Reading #{longest_start + 1}
Longest Streak Ends: Reading #{longest_end + 1}

STOP: {Stop_count}
MOVE SLOWLY: {MoveSlow_count}
MOVE FORWARD: {MoveForward_count}
""")
   


