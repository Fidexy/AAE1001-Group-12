"""

D* grid planning

author: Nirnay Roy

See Wikipedia article (https://en.wikipedia.org/wiki/D*)

"""
import math


from sys import maxsize

import matplotlib.pyplot as plt

show_animation = True


class State:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None
        self.state = "."
        self.t = "new"  # tag for state
        self.h = 0
        self.k = 0

    def cost(self, state):
        if self.state == "#" or state.state == "#":
            return maxsize

        return math.sqrt(math.pow((self.x - state.x), 2) +
                         math.pow((self.y - state.y), 2))

    def set_state(self, state):
        """
        .: new
        #: obstacle
        e: oparent of current state
        *: closed state
        s: current state
        """
        if state not in ["s", ".", "#", "e", "*"]:
            return
        self.state = state


class Map:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = self.init_map()

    def init_map(self):
        map_list = []
        for i in range(self.row):
            tmp = []
            for j in range(self.col):
                tmp.append(State(i, j))
            map_list.append(tmp)
        return map_list

    def get_neighbors(self, state):
        state_list = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if state.x + i < 0 or state.x + i >= self.row:
                    continue
                if state.y + j < 0 or state.y + j >= self.col:
                    continue
                state_list.append(self.map[state.x + i][state.y + j])
        return state_list

    def set_obstacle(self, point_list):
        for x, y in point_list:
            if x < 0 or x >= self.row or y < 0 or y >= self.col:
                continue

            self.map[x][y].set_state("#")


class Dstar:
    def __init__(self, maps):
        self.map = maps
        self.open_list = set()

    def process_state(self):
        x = self.min_state()

        if x is None:
            return -1

        k_old = self.get_kmin()
        self.remove(x)

        if k_old < x.h:
            for y in self.map.get_neighbors(x):
                if y.h <= k_old and x.h > y.h + x.cost(y):
                    x.parent = y
                    x.h = y.h + x.cost(y)
        if k_old == x.h:
            for y in self.map.get_neighbors(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y) \
                        or y.parent != x and y.h > x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
        else:
            for y in self.map.get_neighbors(x):
                if y.t == "new" or y.parent == x and y.h != x.h + x.cost(y):
                    y.parent = x
                    self.insert(y, x.h + x.cost(y))
                else:
                    if y.parent != x and y.h > x.h + x.cost(y):
                        self.insert(x, x.h)
                    else:
                        if y.parent != x and x.h > y.h + x.cost(y) \
                                and y.t == "close" and y.h > k_old:
                            self.insert(y, y.h)
        return self.get_kmin()

    def min_state(self):
        if not self.open_list:
            return None
        min_state = min(self.open_list, key=lambda x: x.k)
        return min_state

    def get_kmin(self):
        if not self.open_list:
            return -1
        k_min = min([x.k for x in self.open_list])
        return k_min

    def insert(self, state, h_new):
        if state.t == "new":
            state.k = h_new
        elif state.t == "open":
            state.k = min(state.k, h_new)
        elif state.t == "close":
            state.k = min(state.h, h_new)
        state.h = h_new
        state.t = "open"
        self.open_list.add(state)

    def remove(self, state):
        if state.t == "open":
            state.t = "close"
        self.open_list.remove(state)

    def modify_cost(self, x):
        if x.t == "close":
            self.insert(x, x.parent.h + x.cost(x.parent))

    def run(self, start, end):

        rx = []
        ry = []

        self.insert(end, 0.0)

        while True:
            self.process_state()
            if start.t == "close":
                break

        start.set_state("s")
        s = start
        s = s.parent
        s.set_state("e")
        tmp = start

        AddNewObstacle(self.map) # add new obstacle after the first search finished

        while tmp != end:
            tmp.set_state("*")
            rx.append(tmp.x)
            ry.append(tmp.y)
            if show_animation:
                plt.plot(rx, ry, "-r")
                plt.pause(0.01)
            if tmp.parent.state == "#":
                self.modify(tmp)
                continue
            tmp = tmp.parent
        tmp.set_state("e")

        return rx, ry

    def modify(self, state):
        self.modify_cost(state)
        while True:
            k_min = self.process_state()
            if k_min >= state.h:
                break

def AddNewObstacle(map:Map):
    ox, oy = [], []
    for i in range(5, 21):
        ox.append(i)
        oy.append(40)
    map.set_obstacle([(i, j) for i, j in zip(ox, oy)])
    if show_animation:
        plt.pause(0.001)
        plt.plot(ox, oy, ".g")

def main():
    sx = 59  # [m]
    sy = 0.0  # [m]
    gx = 0   # [m]
    gy = 50  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    # set obstacle positions for group 9
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

    for i in range(5, 25): # draw the free border
        ox.append(20.0)
        oy.append(i)

    for i in range(10, 20):
        ox.append(i)
        oy.append(-1 * i + 60)
    
    for j in range(40, 50): # draw the free border 
         ox.append(j)
         oy.append(-2 * j + 130)


    # set cost intesive area 1
    tc_x, tc_y = [], []
    for i in range(0, 5):
        for j in range(0, 30):
            tc_x.append(i)
            tc_y.append(j)
    
    # set cost intesive area 2
    fc_x, fc_y = [], []
    for i in range(30, 50):
        for j in range(15,25):
            fc_x.append(i)
            fc_y.append(j)



    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(sx, sy, "og") # plot the start position 
        plt.plot(gx, gy, "xb") # plot the end position
        
        plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
        plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    d_star = Dstar(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = d_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot



if __name__ == '__main__':
    main()
