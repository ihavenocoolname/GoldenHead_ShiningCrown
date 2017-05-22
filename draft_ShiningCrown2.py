
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = "Daily Summaries.csv"
file = open(path, newline="")
reader = csv.reader(file)

header = next(reader) # first line is header, contains no data, so we will go to the next line in the CSV

data = []
for row in reader:
    #I need to take note of the different data types under each header. Date= datetime. I may also have strings, floats, and ints
    #row = ['Date', 'Calories (kcal)', 'Distance (m)', 'Average heart rate (bpm)', 'Max heart rate (bpm)', 'Min heart rate (bpm)', 'Low latitude (deg)', 'Low longitude (deg)', 'High latitude (deg)', 'High longitude (deg)', 'Average speed (m/s)', 'Max speed (m/s)', 'Min speed (m/s)', 'Step count', 'Average weight (kg)', 'Max weight (kg)', 'Min weight (kg)', 'Cycling duration (ms)', 'Inactive duration (ms)', 'Walking duration (ms)', 'Running duration (ms)']
    #I am having trouble converting to the correct data types. I may be accidentally including the header, which is a string.
    #possible fixes include (1) real fix (2) do nothing (3) EVERYTHING IS A STRING!
    date = datetime.strptime(row[0], '%Y-%m-%d')
    calories     = row[1]
    distance     = row[2]
    avg_heart    = row[3]
    max_heart    = row[4]
    min_heart    = row[5]
    low_lat      = row[6]
    low_long     = row[7]
    high_lat     = row[8]
    high_long    = row[9]
    avg_speed    = row[10]
    max_speed    = row[11]
    min_speed    = row[12]
    step_count   = row[13]
    avg_weight   = row[14]
    max_weight   = row[15]
    min_weight   = row[16]
    dur_cycling  = row[17]
    dur_inactive = row[18]
    dur_walking  = row[19]
    dur_running  = row[20]

    #data.append([date, calories, distance, avg_heart, max_heart, min_heart, low_lat, low_long, high_lat, high_long, avg_speed, max_speed, min_speed, step_count, avg_weight, max_weight, min_weight, dur_cycling, dur_inactive, dur_walking, dur_running])
    #by jove I've got it! almost. Indentation was wrong.
    #print(date, step_count)

    #the problem was converting an empty string to an int. Can't be done. try/except seems to be able to fix this!

    try:
        step_count_int = int(step_count)
    except ValueError:
        step_count_int = 0

    print(step_count_int)

    #now for the next problem. making a graph with all this nonsense
    # x = date
    # y = step_count_int

    plt.plot(date, step_count_int, label="steps taken", color="red")

    plt.xlabel("Date")
    plt.ylabel("Steps taken")
    plt.title("Steps over time")

    plt.legend()
    plt.show()

