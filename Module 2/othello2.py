'''
Assignment: Othello 2
Created on 13 jun. 2018
@author: LetsLearnIP.com
'''


think_time_black = float(raw_input("Enter the time the black player thought: "))
think_time_white = float(raw_input("Enter the time the white player thought: "))

think_time_human = think_time_black
if (think_time_white > think_time_black):
    think_time_human = think_time_white

seconds_thought = (think_time_human / 1000) % 60
minutes_thought = (think_time_human / (1000 * 60)) % 60
hours_thought = think_time_human / ( 1000 * 60 * 60)

print "The time the human player has spent thinking is: %02d:%02d:%02d." %(hours_thought, minutes_thought, seconds_thought)

''' Example input/output
Enter the time the black player thought: 21363
Enter the time the white player thought: 36
The time the human player has spent thinking is: 00:00:21.
'''