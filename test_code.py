
# ------------------------------------------------------------------------------------------------
#                                        TEST A
# ------------------------------------------------------------------------------------------------


# import csv

# def unusual_specifics(specific):
#     global under_20, over_60
#     if specific == "under":
#         under_20 += 1
#     else:
#         over_60 += 1

# def percentage():
#     if not readings:
#         return 0

#     return (unusual_readings / len(readings))*100





# readings = []
# unusual_readings = 0
# under_20 = 0
# over_60 = 0
# percentage_u_readings = 0



# with open('test_a.csv', 'r') as file:
#     csv_reader = csv.reader(file)
    
#     # Loop through and print each row (returned as a list)
#     next(csv_reader)

#     for row in csv_reader:
#         current_reading = float(row[1])
#         readings.append(current_reading)
#         # print(readings)
#         if current_reading < 15:
#             unusual_readings += 1
#             unusual_specifics("under")

#         elif current_reading > 40:
#             unusual_readings += 1
#             unusual_specifics("over")
    
# percentage_u_readings = percentage()

# print(f"Number of readings: {len(readings)}")
# print(f"Minimum Reading: {min(readings)}")
# print(f"Maximum Reading: {max(readings)}")
# print(f"Average Reading: {sum(readings)/len(readings)}")
# print(f"Readings under 20: {under_20}")
# print(f"Readings over 60: {over_60}")
# print(f"Unusual Readings: {unusual_readings}")
# print(f"Percentage of Unusual Readings: {percentage_u_readings:.2f}%")

#  ------------------------------------------------------------------------------------------------
#                                         TEST B
#  ------------------------------------------------------------------------------------------------


# import csv

# def unusual_specifics(specific):
#     global under_20, over_60
#     if specific == "under":
#         under_20 += 1
#     else:
#         over_60 += 1

# def percentage():
#     if not readings:
#         return 0

#     return (unusual_readings / len(readings))*100





# readings = []
# unusual_readings = 0
# under_20 = 0
# over_60 = 0
# percentage_u_readings = 0



# with open('test_b.csv', 'r') as file:
#     csv_reader = csv.reader(file)
    
#     # Loop through and print each row (returned as a list)
#     next(csv_reader)

#     for row in csv_reader:
#         current_reading = float(row[1])
#         readings.append(current_reading)
#         # print(readings)
#         if current_reading < 15:
#             unusual_readings += 1
#             unusual_specifics("under")

#         elif current_reading > 40:
#             unusual_readings += 1
#             unusual_specifics("over")
    
# percentage_u_readings = percentage()

# print(f"Number of readings: {len(readings)}")
# print(f"Minimum Reading: {min(readings)}")
# print(f"Maximum Reading: {max(readings)}")
# print(f"Average Reading: {sum(readings)/len(readings)}")
# print(f"Readings under 20: {under_20}")
# print(f"Readings over 60: {over_60}")
# print(f"Unusual Readings: {unusual_readings}")
# print(f"Percentage of Unusual Readings: {percentage_u_readings:.2f}%")

# ------------------------------------------------------------------------------------------------
#                                        TEST C
# ------------------------------------------------------------------------------------------------


# import csv

# def unusual_specifics(specific):
#     global under_20, over_60
#     if specific == "under":
#         under_20 += 1
#     else:
#         over_60 += 1

# def percentage():
#     if not readings:
#         return 0

#     return (unusual_readings / len(readings))*100





# readings = []
# unusual_readings = 0
# under_20 = 0
# over_60 = 0
# percentage_u_readings = 0



# with open('test_c.csv', 'r') as file:
#     csv_reader = csv.reader(file)
    
#     # Loop through and print each row (returned as a list)
#     next(csv_reader)

#     for row in csv_reader:
#         current_reading = float(row[1])
#         readings.append(current_reading)
#         # print(readings)
#         if current_reading < 15:
#             unusual_readings += 1
#             unusual_specifics("under")

#         elif current_reading > 40:
#             unusual_readings += 1
#             unusual_specifics("over")
    
# percentage_u_readings = percentage()

# print(f"Number of readings: {len(readings)}")
# print(f"Minimum Reading: {min(readings)}")
# print(f"Maximum Reading: {max(readings)}")
# print(f"Average Reading: {sum(readings)/len(readings)}")
# print(f"Readings under 20: {under_20}")
# print(f"Readings over 60: {over_60}")
# print(f"Unusual Readings: {unusual_readings}")
# print(f"Percentage of Unusual Readings: {percentage_u_readings:.2f}%")

# ------------------------------------------------------------------------------------------------
#                                        TEST D
# ------------------------------------------------------------------------------------------------


# import csv

# def unusual_specifics(specific):
#     global under_20, over_60
#     if specific == "under":
#         under_20 += 1
#     else:
#         over_60 += 1

# def percentage():
#     if not readings:
#         return 0

#     return (unusual_readings / len(readings))*100





# readings = []
# unusual_readings = 0
# under_20 = 0
# over_60 = 0
# percentage_u_readings = 0



# with open('test_d.csv', 'r') as file:
#     csv_reader = csv.reader(file)

#     next(csv_reader)

#     for row in csv_reader:

#         if not row or not "".join(row).strip():
#             continue


#         current_reading = float(row[0].strip())
#         readings.append(current_reading)    
#         # print(readings)
#         if current_reading < 20:
#             unusual_readings += 1
#             unusual_specifics("under")

#         elif current_reading > 60:
#             unusual_readings += 1
#             unusual_specifics("over")
    

# if readings:
#     percentage_u_readings = percentage()

#     print(f"Number of readings (Ages counted): {len(readings)}")
#     print(f"Minimum Age: {min(readings)}")
#     print(f"Maximum Age: {max(readings)}")
#     print(f"Average Age: {sum(readings)/len(readings):.2f}")
#     print(f"Ages under 20: {under_20}")
#     print(f"Ages over 60: {over_60}")
#     print(f"Unusual Readings: {unusual_readings}")
#     print(f"Percentage of Unusual Readings: {percentage_u_readings:.2f}%")
# else:
#     print("No valid reading data was found.")
