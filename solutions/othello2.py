time1 = int(raw_input("Enter the time the black player thought: "))
time2 = int(raw_input("Enter the time the white player thought: "))

human_time = time1
if time2 > time1 :
    human_time = time2

human_time_h = human_time / 1000 / 60 / 60
human_time_m = human_time / 1000 / 60 % 60
human_time_s = human_time / 1000 % 60

print "The time the human player has spent thinking is %02d:%02d:%02d" % (human_time_h, human_time_m, human_time_s)