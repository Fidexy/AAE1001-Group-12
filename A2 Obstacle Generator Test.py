import random
import matplotlib.pyplot as plt
import math

def main():
    obstacle_density = 0.1
    obstacle_clearance = 5

    while True:
        sx = random.randint(-9,59)  # [m]
        sy = random.randint(-9,59)  # [m]
        gx = random.randint(-9,59)   # [m]
        gy = random.randint(-9,59)  # [m]

        distance = math.sqrt((gx - sx)**2 + (gy - sy)**2)

        if distance >= 40:
            break

    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)
    
    # generate random obstacles
    Rox, Roy = [], []
    for i in range(int(obstacle_density * 60 * 60)):
        ox_temp = random.randint(-9, 59)
        oy_temp = random.randint(-9, 59)
        if math.sqrt((ox_temp - sx)**2 + (oy_temp - sy)**2) < obstacle_clearance or math.sqrt((ox_temp - gx)**2 + (oy_temp - gy)**2) < obstacle_clearance:
            continue
        Rox.append(ox_temp)
        Roy.append(oy_temp)

    fc_x, fc_y = [], []
    randx = random.randint(-9, 20)
    randy = random.randint(-9,20)
    for i in range(randx, randx + 20):
        for j in range(randy, randy + 20):
            fc_x.append(i)
            fc_y.append(j)

    # begin plotting
    plt.plot(ox, oy, ".k") # plot the obstacle
    plt.plot(sx, sy, "og") # plot the start position 
    plt.plot(gx, gy, "xb") # plot the end position
    plt.plot(Rox, Roy, ".k")
        
    plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
    # plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2

    plt.grid(True) # plot the grid to the plot panel
    plt.axis("equal") # set the same resolution for x and y axis 

    plt.show()

if __name__ == '__main__':
    main()