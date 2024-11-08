import random
import matplotlib.pyplot as plt

def main():
    sx = 59  # [m]
    sy = 0.0  # [m]
    gx = 0   # [m]
    gy = 50  # [m]

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
        
    plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
    # plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2

    plt.grid(True) # plot the grid to the plot panel
    plt.axis("equal") # set the same resolution for x and y axis 

    plt.show()

if __name__ == '__main__':
    main()