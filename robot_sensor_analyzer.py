import csv

readings = []
unusual_readings = 0
under_20 = 0
over_60 = 0

def u20():
    under_20 += 1
def o60():
    over_60 += 1
def percentage() :
    print("idk")



with open('Robot_Sensor_Readings_1000.csv', 'r') as file:
    csv_reader = csv.reader(file)
    
    # Loop through and print each row (returned as a list)
    next(csv_reader)

    for row in csv_reader:
        current_reading = float(row[2])
        readings.append(current_reading)
        # print(readings)
        if current_reading < 20:
            unusual_readings += 1
            u20()
        elif current_reading > 60:
            unusual_readings += 1
            o60()
        else:
            continue

print(f"Number of readings: {len(readings)}")
print(f"Minimum Reading: {min(readings)}")
print(f"Maximum Reading: {max(readings)}")
print(f"Average Reading: {sum(readings)/len(readings)}")
print(f"Readings under 20: {def}")
print(f"Readings over 60: {def}")
print(f"Unusual Readings: {unusual_readings}")
print(f"Percentage of Unusual Readings: {def}")
