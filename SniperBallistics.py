import math

space = ""

gun_selection = """Which firearm are you using?
    M24 Sniper Rifle            700m/s
    0.50 Caliber Barrett M82    800m/s
    Remington 700               900m/s
    Cheytac M200                1000m/s

    """

dictionary_firearms = {"M24 Sniper Rifle":700, "0.50 Caliber Barrett M82":800, 
"Remington 700":900, "Cheytac M200":1000}

def sniper_ballistics():
    # calculates what angle you should aim your weapon to eliminate the target
    # asks for weapon selection
    while True:
        weapon = input(gun_selection)
        if weapon not in dictionary_firearms:
            print(space)
            print("must select from listed weapons!")
            continue
        break
        # could use recursion, but that is memory-inefficient and risks stack overflow
    print(space)
    x_distance(weapon)

def x_distance(weapon):
    # asks for x distance to target
    while True:
        x = input("x distance to target? ")
        try:
            x = int(x)
        except ValueError:
            print(space)
            print("ERROR: x distance must be a positive integer!")
            continue
        if x <= 0:
            print(space)
            print("ERROR: x distance must be a positive integer!")
            continue     
        break
    y_distance(weapon, x)

def y_distance(weapon, x):
    # asks for y distance to target
    while True:
        y = input("y distance to target? ")
        try:
            y = int(y)
        except ValueError:
            print(space)
            print("ERROR: y distance must be an integer!")
            continue
        break
    print(space)
    bullet_calculations(weapon, x, y)
  
def bullet_calculations(weapon, x, y):
    # calculates what angle the rifle should be aimed to eliminate the target

    g = 9.81
    v0 = dictionary_firearms[weapon]

    a = g * x**2
    b = -2 * v0**2 * x
    c = 2 * v0**2 * y + g * x**2
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        print(f"Input Variables: [x, y, v0] = [{x}, {y}, {v0}]")
        print("No solution, target cannot be hit")
        print(space)
    else:
        theta1_radian = math.atan((-b - math.sqrt(discriminant)) / (2 * a))
        theta2_radian = math.atan((-b + math.sqrt(discriminant)) / (2 * a))
        theta1_degrees = round(math.degrees(theta1_radian), 3)
        theta2_degrees = round(math.degrees(theta2_radian), 3)
        print(f"Input Variables: [x, y, v0] = [{x}, {y}, {v0}]")
        print(f"Sniper should aim rifle at {theta1_degrees} degrees (or {theta2_degrees} degrees if you're feeling lucky!)")
        print(space)

sniper_ballistics()