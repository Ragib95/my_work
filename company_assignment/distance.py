#python2
import math
#starting point is origin
X0 = 0
Y0 = 0
#given steps. let 1 step = 1 unit
UP = 6
DOWN = 4
RIGHT = 3
LEFT = 2
#calculate final co-ordinate
X1 = UP - DOWN
Y1 = RIGHT - LEFT
#distance calculate
distance = math.sqrt(pow((X1-X0),2) + pow((Y1-Y0),2))
print distance