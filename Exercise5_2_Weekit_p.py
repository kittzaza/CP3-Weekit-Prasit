#Input
speed_of_movement = 120
time_objects_to_move = 10

'''
Process  
 คือสูตร v=s/t ซึ่งคือสูตรในการคำนวณหาระยะทางที่เคลื่อนที่ได้ ต่อ 1 หน่วยเวลา
v คืออัตราเร็วของการเคลื่อนที่ หน่วย (m/s หรือ km/hr)
t คือเวลาที่วัตถุใช้เคลื่อนที่จริง หน่วย (s หรือ hr)
'''
rate_of_speed = speed_of_movement//time_objects_to_move


#Output
print(f"{rate_of_speed} Km/h ")
