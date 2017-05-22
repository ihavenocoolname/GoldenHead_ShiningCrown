import matplotlib.pyplot as plt

#using matplotlib (shortened to plt for simplicity), we are plotting a series of X and Y coordinates to a graph
#the X occupy the first list, and Y the second

#max heart rate = y
#day = x

y = [95,82,128,173,131,128,132,180,121,104,115,180,94,143,140,128,88,123,145,128,121,125,161,104,164,118,122,113,121,128,112,180,140,180,173,128,160,121,131,145,118,180,173,132,113,132,166,180,136,180,117,119,134,180,121,145,177,180,128,132,180,160,173,129]
x = list(range(0,64))

#min heart rate = y2
#day = x2

y2 = [92,81,45,51,56,46,46,48,46,51,47,49,49,46,46,64,49,50,49,57,49,51,52,58,40,43,52,46,39,43,51,54,55,75,51,45,46,47,44,47,42,42,62,45,47,52,48,43,45,41,45,38,49,49,51,47,39,48,46,49,45,56,59,45]
x2 = list(range(0,64))


#since we have 2 lines plotted, a legend comes in handy
plt.plot(x,y, label='maximum heart rate', color="red")
plt.plot(x2,y2, label='minimum hear rate', color="blue")

#graphics. everything is drwn to a background first. then we bring forwardwhatever we've been working on the background. time to bring it to th forefront

#this gives labels to our axes, and a title
plt.xlabel("Days")
plt.ylabel("Heart Rate (BPM)")
plt.title("My heart rate over 64 days")


plt.legend()
#this shows the graph plotted with the above data
plt.show()