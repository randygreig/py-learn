import nxt
b = nxt.find_one_brick()
l = nxt.Motor(b, nxt.PORT_C)
r = nxt.Motor(b, nxt.PORT_B)
m = nxt.SynchronizedMotors(l, r, 0) #the last arg is turn ratio
m.turn(70, 360) #forward  
m = nxt.SynchronizedMotors(l, r, 6)
m.turn(70, 360) #turn left
nxt.SynchronizedMotors(r, l, 6).turn(70, 360) #shorthand for turn right
m.brake()

