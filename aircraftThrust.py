import math
# Calculating thrust of Aircraft Propeller

# function to calculate propeller thrust
def thrustProps(diameter , velocity , velocity1 , density):
    # According to formula
    thrust = math.pi / 4 * diameter ** 2 * (velocity + velocity1/2) * density * velocity1
    return(thrust) # returning  calculated thrust

# Main user interaction
print('Hello Aircraft Lovers,\n')
while(True):
    startOrEnd = str(input('Start or End : '))
    if startOrEnd == 'Start': # condition if user says start program
        diaOfPropeller = float(input('Diameter of propeller : '))
        velocityOfFlow = float(input('Velocity of Air Flow : '))
        additionalVelocity = float(input('Additional propeller acceleration , velocity : '))
        fluidDensity = float(input('Fluid Density : '))
        print(thrustProps(diaOfPropeller , velocityOfFlow , additionalVelocity , fluidDensity)) # function with parameters
        continue
    else:
        quit() # exiting console
# I dont know much about airplane physics this formula maybe wrong
