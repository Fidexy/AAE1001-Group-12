
　<p align="center">

  <h3 align="center">PolyU AAE1001 GitHub Project Group 12 </h3>
  
# Members name

**Leader:**
AU bai qiao

**Member 1:** 
LEUNG tsz hei

**Member 2:** 
Sun Jiajun

**Member 3:**
Xiong jianyu

**Member 4:**
LIU wingyin

**Member 5:**
Li Bowen

**Member 6:**
WONG Tin Ching


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>

* [Introduction](#introduction)
* [Task 1](#task-1)
* [Task 1 (Bonus)](#Calculation-with-code)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Additional Task 1](#Additional-Task-1)
* [Additional Task 2](#Additional-Task-2)
* [Additional Task 3](#Additional-Task-3)
* [Reflections](#reflections)
* [Contacts](#contacts)


## Introduction
With so many competing airlines, the cost of flights became critical to profitability and pricing strategies. Besides operational efficiency, fuel and maintenance make up the high costs that determine pricing and flying routes. In choosing aircraft, airlines have to consider operational cost, range, capacity, and technology characteristics, together with market trends and passenger preference. Effective flight cost management and strategic aircraft choices would eventually lead carriers to optimize operations and improve profitability.

In this project, we will apply path planning in order to have a basis to obtain the shortest and best path. In this case, we enhance and apply the A* method in order to determine the low-cost flight path across different scenarios..

#### The Programme Path:
<img src="https://github.com/user-attachments/assets/e800c87a-83fb-4ab7-a524-1daaf3ae7748" alt="螢幕擷取畫面 2024-11-06 231752" width="700" height="350">

### Path planning
<img src="https://github.com/user-attachments/assets/e8b2fbbd-10c8-47fe-8ad6-8ac94439c068" alt="![Figure_1]" width="450" height="350">

#### Adjusting the obstacles
By changing the value in the range ( -10,60 ) which provide from the power point ,the border will move to our designated coordinate.  For the cost intensive area, the coordinate can be move by adjusting the i/j range ( X,Y ). Therefore, the shortest flight time (83.225 mins) will be generated through A* algorithm
~~~python
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
~~~

## Task 1
### Description
Choose the best aircraft model for each scenario by evaluating the cost required to complete the scenario.

### General Calculation Method
C = C<sub>F</sub>  ⋅ ΔF ⋅ ΔT + C<sub>T</sub> ⋅ T<sub>best</sub> + C<sub>C</sub>

C<sub>F</sub> = cost of fuel per kg

C<sub>T</sub> = time related cost per minute of flight

C<sub>C</sub> = fixed cost independent of time

ΔF = rate of fuel consumption

ΔT = trip time

## Scenario 1
- **Passengers**: 3000 people
- **Time Limit**: 1 week
- **Maximum Flights**: 12 per week
- **Time Cost**: Medium
- **Fuel Cost**: $0.76/kg

### Flight Calculations (By Manual)

- **A321**: 
  - Flights needed:  $3000/200$ = 15  flights
  - Result: Rejected (exceeds 12 flights/week)

- **A330**: 
  - Flights needed: $3000/300$ = 10  flights

- **A350**: 
  - Flights needed: $3000/350$ = 9  flights

### Trip Cost

- **A330**: 
  
  ($0.76 \times 8483.225$ + 2183.225 + 2000) $\times 10$ = $90,608.09
  

- **A350**: 
  
  ($0.76 \times 9083.225$ + 2783.225 + 2500) $\times 9$ = $93,956.99
  

**Conclusion**: *A330-900 Neo* is chosen.

---

## Scenario 2

- **Passengers**: 1250 people
- **Time Limit**: 1 month
- **Maximum Flights**: 5 per week
- **Time Cost**: High
- **Fuel Cost**: $0.88/kg

### Flight Calculations (By Manual)

- **A321**: 
  - Flights needed:  $1250/200$ = 7  flights

- **A330**: 
  - Flights needed:  $1250/300$  = 5  flights

- **A350**: 
  - Flights needed: $1250/350$ = 4  flights

### Cost

- **A321**: 
  
  ($0.88 \times 5483.225$ + 2083.225 + 1800) $\times 7$ = $51,935.46
  

- **A330**: 
  
  ($0.88 \times 8483.225$ + 2783.225 + 2000) $\times 5$ = $51,995.34
  

- **A350**: 
  
  ($0.88 \times 9083.225$ + 3483.225 + 2500) $\times 4$ = $47,684.28
  

**Conclusion**: *A350-900* is chosen.

---

## Scenario 3

- **Passengers**: 2500 people
- **Time Limit**: 1 week
- **Maximum Flights**: 25 per week
- **Time Cost**: Low
- **Fuel Cost**: $0.95/kg

### Flight Calculations (By Manual)

- **A321**: 
  - Flights needed: $2500/200$ = 13  flights

- **A330**: 
  - Flights needed: $2500/300$ = 9  flights

- **A350**: 
  - Flights needed: $2500/350$ = 8  flights

### Cost

- **A321**: 
  
  ($0.95 \times 5483.225$ + 1083.225 + 1800) $\times 13$ = $89,722.00
  

- **A330**: 
  
  ($0.95 \times 8483.225$ + 1583.225 + 2000) $\times 9$ = $89,007.57
  

- **A350**: 
  
  ($0.95 \times 9083.225$ + 2083.225 + 2500) $\times 8$ = $90,241.90
  

**Conclusion**: *A321 Neo* is chosen.

***

## Calculation with code 
### Setting constants
Each scenario has the following attributes:

- Fuel cost (FCost)
- Passenger number (Pnum)
- Time cost [low/mid/high] (TCostFactor)
- Maximum flights (MaxFlight)
~~~python
class Scenario:
    def __init__(self, FCost, Pnum, TCostFactor, MaxFlight):
        self.FCost = FCost
        self.PNum = Pnum
        self.TCostFactor = TCostFactor  
        self.MaxFlight = MaxFlight      
    def __str__(self):
        return str(self.FCost) + "," + str(self.PNum) + "," + str(self.TCostFactor) + "," + str(self.MaxFlight)
S1 = Scenario(0.76, 3000, 2, 12)
S2 = Scenario(0.88, 1250, 3, 25)
S3 = Scenario(0.95, 2500, 1, 25)
~~~
Each aircraft model has the following attributes:
- Fuel consumption rate (FComp)
- Passenger capacity (PCap)
- Time Cost (TCostLow/Mid/Hi)
- Fixed Cost (FCost)
~~~python
class Aircraft:
    def __init__(self, name, FComp, PCap, TCostLow, TCostMid, TCostHi, FixedCost):
        self.name = name
        self.FComp = FComp
        self.PCap = PCap
        self.TCostLow = TCostLow
        self.TCostMid = TCostMid
        self.TCostHi = TCostHi
        self.FixedCost = FixedCost
    def __str__(self):
            return str(self.name) + "," + str(self.FComp) + "," + str(self.PCap) + "," + str(self.TCostLow) + "," + str(self.TCostMid) + "," + str(self.TCostHi)
A321Neo = Aircraft("A321 Neo", 54, 200, 10, 15, 20, 1800)
A330 = Aircraft("A330-900 Neo", 84, 300, 15, 21, 27, 2000)
A350 = Aircraft("A350-900", 90, 250, 20, 27, 34, 2500) 
~~~
With these attributes, the cost needed to complete a scenario can be calculated
### Cost function
Given that the cost equation is:

C = C<sub>F</sub>  ⋅ ΔF ⋅ ΔT + C<sub>T</sub> ⋅ T<sub>best</sub> + C<sub>C</sub>
The cost function can be made with the aforementioned variables as:
~~~python
  flightnum = math.ceil(scenario.PNum/aircraft.PCap)
  perFcost = scenario.FCost*aircraft.FComp*current.cost + TCost*current.cost + aircraft.FixedCost
  cost = perFcost * flightnum
~~~
Where current.cost contains the value of the flight time, flightnum calculates the number of flights needed to complete the scenario, perFcost calculates the cost per flight, and cost multiplies the two together to obtain the total cost for each scenario.

An if statement is used to select the appropriate time cost based on the scenario:
~~~python
if scenario.TCostFactor == 1:
      TCost = aircraft.TCostLow
  elif scenario.TCostFactor == 2:
      TCost = aircraft.TCostMid
  else:
      TCost = aircraft.TCostHi
~~~
### Outputs
~~~python
  exceedlim = flightnum > scenario.MaxFlight
  statement1 = f"Per flight cost with {name}: {perFcost}, total cost: {cost}"
  statement2 = f"This plan would require {flightnum} flights"
  if exceedlim == True:
      statement3 = ", which exceeds the flight limit of the scenario"
  else:
      statement3 = "" 
  print(statement1)
  print(statement2, statement3)
~~~
![螢幕擷取畫面 2024-11-12 171955](https://github.com/user-attachments/assets/af45789b-7aec-4fa2-ae12-95b782f0026f)

## Task 2
### Jetstream
### Introduction
Set up a minus-cost area which spans across the map laterally and 5 units vertically and determine the optimal placement of the minus-cost area
### Setting up the jetstream
Creating a jetstream:
~~~python
js_x, js_y = [], []
    for i in range(-10, 60):
        for j in range(index, index+5):
            js_x.append(i)
            js_y.append(j)
~~~
Removing cost in jetstream area:
~~~python
Delta_C3 = 0.05
...
if self.calc_grid_position(node.x, self.min_x) in self.js_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.js_y:
                        # print("jetstream area!!")
                        node.cost = node.cost - self.Delta_C3 * self.motion[i][2]
~~~
### Calculating optimal placement
This code block runs multiple iterations of the path planning algorithm, setting up the jetstream in a different area in each iteration. The resulting cost, as well as the y-value of the jetstream, is stored in an array jetstream_list. Plotting is disabled in this stage.
~~~python
for k in range(-11, 55):        
        js_x, js_y = [], []
        for i in range(-10, 60):
            for j in range(k, k+5):
                js_x.append(i)
                js_y.append(j)
        a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y, js_x, js_y)
        rx, ry = a_star.planning(sx, sy, gx, gy)
        # print(global_cost)      
        jetstream_list.append((k, global_cost))
~~~
A simple algorithm searches for the array item with the lowest path cost, indicating the optimal path, and obtains the y-value of the jetstream for reconstruction of the optimal path. Plotting is enabled after this function to allow the optimal path to be displayed.
~~~python
    lowest = 9999999999
    for i in range(1, 66):
        if jetstream_list[i][1] < lowest:
            lowest = jetstream_list[i][1]
            index = jetstream_list[i][0]
    show_animation = True
~~~
### Result:
<img src="https://github.com/user-attachments/assets/c5586965-5167-41e5-abef-99858ce7604e" alt="![image]" width="300" height="250">


<img src="https://github.com/user-attachments/assets/c0219a52-c966-486a-9796-cd136775812d" alt="![螢幕擷取畫面 2024-11-12 180408]" width="450" height="50">


-From the result, the programme code found out that the optimal jet stream position is 13-18 and the flight time is 80.17991693419718



# Task 3
#### Introduction
In this task, the new aircraft will be designed to achieve minimum cost for [scenario 1](#Scenario-1) in task 1. Different aircraft designs will be compared through the table and the explanation will be mentioned below. Currently, the airline sometimes use different aircraft for the same route of flight during peak seaon in order to maximize the profit. 

## Scenario 1
- **Passengers**: 3000 people
- **Time Limit**: 1 week
- **Maximum Flights**: 12 per week
- **Time Cost**: Medium

## Aircraft Spectifications
#### Aircraft Name: A350-800 Max
#### Flight: VHHH to RCTP

#### Passenger Capacity
- Minimum: 100
- Maximum: 450

#### Cost Calculations (CT)
- **Base Cost Time (CT):** $12/min
- **Increments:** For every 50 passengers, CT increases by $2/min

#### Engine Configuration
- **Twin-Engine:** For capacity < 300
- **Four-Engine:** For capacity ≥ 300

#### Fuel Consumption
- Each engine consumes 20 kg/min

#### Fixed Costs (CC)
- = 2000 for twin-engine
- = 2500 for four-engine

#### Fuel Cost
![螢幕擷取畫面 2024-11-05 193551](https://github.com/user-attachments/assets/82a46e6b-aaa4-440a-b7c6-cab5f1d5aeda)
- The global average jet fuel price last week fell 0.5% compared to the week before to $88.26/bbl. -> $0.649/kg (Asia)
  
#### General Calculation Method
C = C<sub>F</sub>  ⋅ ΔF ⋅ ΔT + C<sub>T</sub> ⋅ T<sub>best</sub> + C<sub>C</sub>

C<sub>F</sub> = cost of fuel per kg

C<sub>T</sub> = time related cost per minute of flight

C<sub>C</sub> = fixed cost independent of time

ΔF = rate of fuel consumption

ΔT = trip time


## Our calculation
| **Passenger Capacity** | **Time cost**| **Fixed cost** | **Engines** | **Fuel consumption** | **Flights needed** | **Cost per flight** | **Scenario 1 cost** | **Exceeds Flight Limit** |
| ------------------ | --------- | ---------- | ------- | ---------------- | -------------- | --------------- | --------------- | --------------------- |
| 100                | 16        | 2000       | 2       | 40               | 30             | 5491.07         | 164732.16        | *yes*                   |
| 150                | 18        | 2000       | 2       | 40               | 20             | 5657.47         | 113149.44        | *yes*                   |
| 200                | 20        | 2000       | 2       | 40               | 15             | 5823.87         | 87358.08         | *yes*                   |
| 250                | 22        | 2000       | 2       | 40               | 12             | 5990.27         | 71883.26         | no                    |
| 300                | 24        | 2500       | 4       | 80               | 10             | 8816.54         | 88165.44         | no                    |
| 350                | 26        | 2500       | 4       | 80               | 9              | 8982.94         | 80846.49         | no                    |
| 400                | 28        | 2500       | 4       | 80               | 8              | 9149.34         | 73194.75         | no                    |
| 450                | 30        | 2500       | 4       | 80               | 7              | 9315.74         | 65210.20         | no                    |


### Result: The minimum flight cost is $65210.20 ; with 450 passenger capacity ; 4 engines configuration
 - The design of 100-200 passenger capacity is not suitable because it exceed the flight limit for 12 flight per week maximum.
 - The overall result shows that use a four-engine configuration for capacities over 300 can maximize the number of passengers per flight, minimize the number of flights and balancing costs.
 - In the environmental aspect, the four-engine configuration might produce more carbon emissions and green house gas. Though the cost of four-engine is slightly lower than twin-engine.

![Scenario 1 cost based on passenger capacity ](https://github.com/user-attachments/assets/29622e57-1527-43fa-9ad3-6ef5c77e6d90)

# Additional Task 1
<img src="https://github.com/user-attachments/assets/9086f4ed-517e-4268-a327-07ff9d656b17" alt="![螢幕擷取畫面 2024-11-12 181654]" width="500" height="350">

### Introduction
Set up a checkpoint in each cost-intensive area, which must be passed through before reaching the checkpoint
### Checkpoint setup
~~~python
# checkpoint 1
c1x = 40 
c1y = 20
# checkpoint 2
c2x = 2
c2y = 2
~~~
![image](Images\A2cp.png)

### Modified code
The path planning function was called multiple times with different coordinates, and the results were stored in different arrays to be plotted separately
~~~python
rx1, ry1 = a_star.planning(sx, sy, c1x, c1y)
# Plan path from checkpoint 1 to checkpoint 2
rx2, ry2 = a_star.planning(c1x, c1y, c2x, c2y)
# Plan path from checkpoint 2 to goal
rx3, ry3 = a_star.planning(c2x, c2y, gx, gy)
...
...
plt.plot(rx1, ry1, "-r") # show the route 
plt.pause(0.001) # pause 0.001 seconds
plt.plot(rx2, ry2, "-r")
plt.pause(0.001)
plt.plot(rx3, ry3, "-r")
plt.pause(0.001)
plt.show() # show the plot
~~~
# Additional Task 2
### Introduction
Edit the program such that obstacles, cost-intensive area and start/end points are generated randomly
##### Requirements
- Obstacles should be randomly generated with a reasonable density
- Obstacles should not generate near the start and end points
- Remove the cost-intensive area
- Fuel-intensive area should be 40x40 in area
- The fuel-intensive area should not cover the plotting of the obstacles
### Modified code
The code snippet shown below generates the 40x40 fuel-intensive area in a random position:
~~~python
fc_x, fc_y = [], []
    randx = random.randint(-9, 20)
    randy = random.randint(-9,20)
    for i in range(randx, randx + 40):
        for j in range(randy, randy + 40):
            fc_x.append(i)
            fc_y.append(j)
~~~
The code snippet shown below generates obstacles randomly
~~~python
for i in range(int(obstacle_density * 60 * 60)):
  ox_temp = random.randint(-9, 59)
  oy_temp = random.randint(-9, 59)
  if math.sqrt((ox_temp - sx)**2 + (oy_temp - sy)**2) < obstacle_clearance or math.sqrt((ox_temp - gx)**2 + (oy_temp - gy)**2) < obstacle_clearance:
      continue

  ox.append(ox_temp)
  oy.append(oy_temp)
~~~
It takes in two constants, obstacle_density and obstacle_clearance, which determine the obstacle density and area around the start/end points which should not generate obstacles, respectively. Random integers corresponding to the x and y value of the randomly generated obstacle undergoes a check to make sure they aren't within a certain proximity of the start and end points, before appending them to the arrays for the obstacle coordinates.

# Additional Task 3
## Theories between A*, Dijkstra and Breadth-First Search
#### A*
A* is an informed search algorithm that uses a function 𝑓(𝑛)=𝑔(𝑛)+ℎ(𝑛)f(n)=g(n)+h(n), where 𝑔(𝑛)g(n) is the actual cost from the start, and ℎ(𝑛)h(n) is the heuristic estimate to the goal. It’s efficient when the heuristic is accurate, focusing the search towards the goal.

<img src="https://github.com/user-attachments/assets/1b887f6a-ac14-4e64-b527-c3e152c481a4" alt="Image Description" width="400"/>

#### Dijkstra
Dijkstra's algorithm find the shortest path by explore the node with the smallest known distance from the source which is similar to A*, except that A* makes use of heuristics to find the shortest parth. Dijkstra is a greedy algorithm that works on weighted graphs with non-negative edge weights, guaranteeing the shortest path by minimizing the total path cost from the source to each node.

<img src="https://github.com/user-attachments/assets/a05f99fe-df4b-492a-b1b7-444afd47269d" alt="Image Description" width="400"/>

#### Breadth-First Search
Breadth-first search explores all neighboring nodes at the present depth before moving on to the nodes of the next depth level.  It uses a queue to explore nodes in order of their distance from the source which making it ideal for unweighted graphs. As a result, it guarantees the shortest path in terms of the number of edges.

<img src="https://github.com/user-attachments/assets/3f859c58-9e2e-4356-9078-8ce42771a0db" alt="Image Description" width="400"/>


## Performance between A*, Dijkstra and Breadth-First Search
#### A*
A* performs very well when an admissible and consistent heuristic is available, guiding the search efficiently towards the goal and reducing exploration.
For large graphs with a bad heuristic, A* can be slower and explore more nodes than Dijkstra’s.
#### Dijkstra
Dijkstra's is guaranteed to find the shortest path in a graph with non-negative edge weights, but it doesn't have a heuristic to guide it, meaning it may explore more nodes than necessary, especially in large graphs.
Compared to A*, Dijkstra's tends to explore more nodes in graphs with a clear goal since it doesn’t have a heuristic to focus the search.
#### Breadth-First Search
BFS is optimal for unweighted graphs, where the shortest path is defined by the minimum number of edges, but it is inefficient in weighted graphs.
BFS can explore a large number of irrelevant nodes, especially in large graphs where the goal is far from the source, making it slower than A* or Dijkstra’s in many cases.

## Limitation and strength between A*, Dijkstra and Breadth-First Search

### A*
### Limitations:

Heuristic-Dependent: The performance of A* depends heavily on the heuristic. A poor heuristic can lead to worse performance than Dijkstra’s or unnecessary exploration.

Memory-Intensive: A* stores all potential paths and their costs in memory which can become problematic in very large graphs or maps.

Complexity: Implementing A* is more complex than BFS or Dijkstra’s due to the need for a heuristic function and careful management of the priority queue.

### Strengths:

Efficient with a Good Heuristic: A* performs extremely well if the heuristic is a good estimate of the actual cost, focusing the search toward the goal and reducing exploration.

Optimal Path: A* always finds the shortest path if the heuristic is admissible and consistent.

Goal-Oriented: A* is goal-directed which mean it works particularly well in large search spaces because it prioritizes nodes that are closer to the target based on the heuristic.

### Dijkstra

### Limitations:

Explores Many Nodes: Dijkstra’s explores all nodes based on their distance from the source, even if they are far from the goal. This can make it slower in large graphs where the goal is located far from the source.

Not Goal-Oriented: Dijkstra’s algorithm is not goal directed , it does not prioritize nodes that are closer to the goal which leading to unnecessary exploration.

Memory Usage: Like A*, Dijkstra’s needs to store all distances and maintain a large priority queue, which can consume significant memory in large maps.

### Strengths:

Always Finds the Shortest Path: In weighted pathfinding, Dijkstra’s is guaranteed to find the optimal path, regardless of the goal’s position.

No Heuristic Needed: It works well without a heuristic and is easier to apply in general weighted graphs where no obvious heuristic exists.

Handles All Non-Negative Weights: Dijkstra’s works for all graphs with non-negative edge weights which making it versatile for various pathfinding problems.

### Breadth-First Search

### Limitations:

Inefficient for Weighted Graphs: BFS treats all edges equally so it cannot handle different edge weights. It is not suitable for weighted pathfinding.

Blind Search: BFS explores all nodes evenly without considering the goal’s location which leading to slow performance in large graphs or maps where the goal is far from the source.

Not Scalable: In large graphs, BFS can explore a vast number of irrelevant nodes before reaching the goal, making it inefficient compared to A* or Dijkstra’s in large pathfinding problems.

### Strengths:

Simple and Effective for Unweighted Graphs: BFS is ideal for pathfinding in unweighted grids or graphs where all edges have the same cost.

Guarantees Shortest Path: In unweighted graphs, BFS guarantees the shortest path in terms of the number of steps or edges.

Easy to Implement: BFS is straightforward to code and doesn’t require a heuristic or complex data structures like a priority queue.

# Summary

| **Algorithm**         | **Theory**                                                                                                                                      | **Strengths**                                                        | **Limitations**                                                  | **Performance**                                                  |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| **A\***               | - Uses **𝑓(𝑛) = 𝑔(𝑛) + ℎ(𝑛)**, where **𝑔(𝑛)** is the cost from start, and **ℎ(𝑛)** is a heuristic estimate to the goal. <br> - Informed and goal-directed. | - Efficient with good heuristic <br> - Goal-oriented <br> - Finds optimal path | - Heuristic-dependent <br> - Memory-intensive <br> - Complex     | - Fast with good heuristic <br> - Slower with poor heuristic     |
| **Dijkstra**          | - Greedy algorithm exploring nodes with the smallest known distance from the source. <br> - Works on graphs with **non-negative** edge weights.  | - Always finds shortest path <br> - No heuristic needed <br> - Handles non-negative weights | - Explores irrelevant nodes <br> - Not goal-oriented <br> - Memory usage | - Explores many nodes <br> - Slower than A\* with good heuristic |
| **Breadth-First Search** | - Explores all nodes at the current depth before moving to the next level. <br> - Ideal for **unweighted** graphs and uses a queue.            | - Simple and easy to implement <br> - Guarantees shortest path in unweighted graphs | - Inefficient for weighted graphs <br> - Blind search <br> - Not scalable | - Optimal in unweighted graphs <br> - Slow in large graphs       |

# Reflections

Leung Tsz Hei 24082857d

In this group project, I have learnt a lot of programming knowledge. I remember when I first received this assignment, I felt devastated because i have no previous knowledge on the A* algorithm. Fortunately, I had a great group of people who helped me understand the task. One of my groupmate have much more experience in coding and he taught me the meaning of the code patiently. For the work distribution, I was mainly responsible for the work on Task 3 and readme report. At the beginning, I had no idea how to edit the markdown format such as adding the heading, subheading, link and photo. After that, I watched lots of online tutorials which helped me familiarize with the typing style. I started to understand the meaning behind each markdown code. Now, I think I master the basic use of the markdown format report.

