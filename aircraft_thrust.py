import math
# Calculating thrust of Aircraft Propeller

def thrust_props(diameter , velocity , velocity1 , density):
    # According to formula
    return math.pi / 4 * diameter ** 2 * (velocity + velocity1/2) * density * velocity1

print('Hello Aircraft Lovers,')
while(True):
    start_or_end = str(raw_input('start or end : ')).strip().lower()
    if start_or_end == 'start':
        res = thrust_props(float(input('Diameter of propeller: ')) , float(input('Velocity of air flow: ')) , float(input('Additional propeller acceleration, velocity: ')) , float(input('Fluid density: ')))
        print("Thrust of propeller: {}".format(res)) 
        continue
    else:
        quit()
# I dont know much about airplane physics this formula maybe wrong
