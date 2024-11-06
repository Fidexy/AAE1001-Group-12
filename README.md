　<p align="center">

  <h3 align="center">PolyU AAE1001 GitHub Project Group 12 </h3>
  
# Members name

**Leader:**
AU bai qiao

**Member 1:** 
LEUNG tsz hei

**Member 2:** 


**Member 3:**


**Member 4:**


**Member 5:**


**Member 6:**


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>

* [Introduction](#introduction)
* [Task 1](#task-1)
* [Task 1 (Bonus)](#task-1-bonus)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Task 4](#task-4)
* [Reflections](#reflections)
* [Contacts](#contacts)


## Introduction
Nowadays, the cost of flight is a very important factor to decide upon profitability and competitive pricing besides operational efficiency for an airline company. Fuel and maintenance are two major key items of expenses in airline operations, which account for the price of tickets and planning of routes. Airlines have to consider their operation costs, range, capacity, and technology when they choose aircraft Moreover, market trends and passenger preferences too lead to deciding upon the type of aircraft selected. Thus, it is clear that, by properly managing the cost of flights and making prudent choices in aircraft, airlines can optimize their operations and maximize profitability in order to meet this demand. In this project, path planning can be used to find the shortest and most obstacle-free path from a start to goal state. We are going to modify and utilize the A* algorithm to facilitate the shortest path which is the lowest flight cost for different scenario.

#### The Programme Path:
<img src="https://github.com/user-attachments/assets/e800c87a-83fb-4ab7-a524-1daaf3ae7748" alt="螢幕擷取畫面 2024-11-06 231752" width="700" height="350">

## Task 1
### Discription
- Here are the three scenario, the total cost are affected by shortest distance, cost intensive area, aircraft fuel and time cost from different aircraft model. The best aircraft model will be chosen through the calculation and programming.

### General Calculation Method
　<p align="center"> <img src="https://github.com/user-attachments/assets/ae80c7c5-0781-4657-a360-592e238de6a4" alt="螢幕擷取畫面 2024-11-06 000040" width="500" height="150">

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

## Task 1 (Bonus) 


# Task 3
#### Introduction
In this task, the new aircraft will be designed to achieve minimum cost for [scenario 1](#Scenario-1) in task 1. Different type of aircarft design will be compared through the table and the explanation will be mentioned below. Currently, the airline sometimes use different aircraft for the same route of flight during peak seaon in order to maximize the profit. 

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
  <h3 align="center"> Trip Cost=CT×Best Cruise Time+Total Fuel Cost+CC </h3>


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


# Reflections
