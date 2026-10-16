import math

AB = int(input())
BC = int(input())
angle = math.degrees(math.atan(AB / BC))
print(str(int(math.floor(angle + 0.5))) + chr(176))
