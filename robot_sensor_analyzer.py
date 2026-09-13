import csv

readings = []
unusual_readings = 0
under_20 = 0
over_60 = 0
Stop_count = 0
MoveSlow_count = 0
MoveForward_count = 0
percentage_u_readings = 0


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

        num_readings = len(readings)
        min_readings = min(readings)
        max_readings = max(readings)
        avg_readings = sum(readings)/len(readings)

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




is_valid_min_threshold = False

while not is_valid_min_threshold:
    user_min_threshold = input("Decide the Minimum Threshold for the data to be valid: ")
    try:
        testNumMin = float(user_min_threshold)
        is_valid_min_threshold = True 
    except ValueError:
        print("That is not a valid number. Try again.")

is_valid_max_threshold = False

while not is_valid_max_threshold:
    user_max_threshold = input("Decide the Maximum Threshold for the data to be valid: ")
    try:
        testNumMax = float(user_max_threshold)
        is_valid_max_threshold = True 
    except ValueError:
        print("That is not a valid number. Try again.")




# Open your file normally
with open('Robot_Sensor_Readings_1000.csv', 'r') as file:
    
    csv_reader = csv.DictReader(file)
    for row in csv_reader:

        current_reading = float(row["distance_cm"]) 
        readings.append(current_reading)
        
        if current_reading < testNumMin:
            unusual_specifics("under")
            # print(row["reading_id"])

        elif current_reading > testNumMax:
            unusual_specifics("over")
            # print(row["reading_id"])
    
num, min_r, max_r, avg, under_20, over_60, unusual, pct = summarize_sensor_data(readings)
robot_decision(readings)

print(f"""
Total Readings: {num}
Minimum Reading: {min_r}
Maximum Reading: {max_r}
Average Reading: {avg}
Readings under {testNumMin}: {under_20}
Readings over {testNumMax}: {over_60}
Unusual Readings: {unusual}
Unusual Readings Percentage: {pct}%

STOP: {Stop_count}
MOVE SLOWLY: {MoveSlow_count}
MOVE FORWARD: {MoveForward_count}
""")
   


