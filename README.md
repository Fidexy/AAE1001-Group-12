　<p align="center">

  <h3 align="center">PolyU AAE1001 GitHub Project Group12 </h3>
  
# Members name

**Leader:** 


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

* [Introduction](#Introduction)
* [Task 1](#task-1)
* [Task 2](#task-2)
* [Task 3](#task-3)
* [Reflections](#Reflections)
* [Contacts](#contacts)


## Introduction


## Task 1
### Scenario 1

3000ppl, time limit: 1 week, max: 12/week, time cost: medium, fuel: \$0.76/kg

A321: 3000/200=15 flights \> 12, rejected

A330: 3000/300=10 flights

A350: 3000/350=9 flights

Trip Cost:

A330: $$( 0 . 7 6 84 8 3 . 2 2 5 + 2 1 8 3 . 2 2 5 + 2 0 0 0 ) 10 = \$ 9 0 6 0 8 . 0 9$$

A350: $$( 0 . 7 6 90 8 3 . 2 2 5 + 2 7 8 3 . 2 2 5 + 2 5 0 0 ) 9 = \$ 9 3 9 5 6 . 9 8 5$$

$$test$$

***

So, A330 would be chosen.

***

Scenario 2

1250ppl, time limit: 1 month, max:5/week, time cost: high, fuel:\$0.88/kg

A321: 1250/200=7 flights

A330: 1250/300=5 flights

A350: 1250/350=4 flights

Cost:

A321: $$( 0 . 8 8 54 8 3 . 2 2 5 + 2 0 8 3 . 2 2 5 + 1 8 0 0 ) 7 = \$ 5 1 9 3 5 . 4 6 4$$

A330: $$( 0 . 8 8 84 8 3 . 2 2 5 + 2 7 8 3 . 2 2 5 + 2 0 0 0 ) 5 = \$ 5 1 9 9 5 . 3 3 5$$

A350: $$( 0 . 8 8 90 8 3 . 2 2 5 + 3 4 8 3 . 2 2 5 + 2 5 0 0 ) 4 = \$ 4 7 6 8 4 . 2 8$$

***

So, A350 would be chosen.

***

Scenario 3

2500ppl, time limit: 1week, max: 25/week, time cost: low, fuel: \$0.95/kg

A321: 2500/200=13 flights

A330: 2500/300=9 flights

A350: 2500/350=8 flights

A321: $$( 0 . 9 5 54 8 3 . 2 2 5 + 1 0 8 3 . 2 2 5 + 1 8 0 0 ) 1 3 = \$ 8 9 7 2 2 . 0 0 2 5$$

A330: $$( 0 . 9 5 84 8 3 . 2 2 5 + 1 5 8 3 . 2 2 5 + 2 0 0 0 ) 9 = \$ 8 9 0 0 7 . 5 7$$

A350: $$( 0 . 9 5 90 8 3 . 2 2 5 + 2 0 8 3 . 2 2 5 + 2 5 0 0 ) 8 = \$ 9 0 2 4 1 . 9$$

So, A321 would be chosen.



# Task 3
#### Introduction
In this task, the new aircraft will be designed to achieve minimum cost for [scenario 1](#Scenario-1) in task 1. Different type of aircarft design will be compared through the table and the explanation will be mentioned below. Currently, the airline sometimes use different aircraft for the same route of flight in order to maximize the profit. 

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
- The global average jet fuel price last week fell 0.5% compared to the week before to $89.11/bbl. -> $0.655/kg
  
#### General Calculation Method
  <h3 align="center"> Trip Cost=CT×Best Cruise Time+Total Fuel Cost+CC </h3>

## Our calculation
| **Passenger Capacity** | **Time cost**| **Fixed cost** | **Engines** | **Fuel consumption** | **Flights needed** | **Cost per flight** | **Scenario 1 cost** | **Exceeds Flight Limit** |
| ------------------ | --------- | ---------- | ------- | ---------------- | -------------- | --------------- | --------------- | --------------------- |
| 100                | 16        | 2000       | 2       | 40               | 30             | 5860.48         | 165331.2        | *yes*                   |
| 150                | 18        | 2000       | 2       | 40               | 20             | 6026.88         | 113548.8        | *yes*                   |
| 200                | 20        | 2000       | 2       | 40               | 15             | 6193.28         | 87657.6         | *yes*                   |
| 250                | 22        | 2000       | 2       | 40               | 12             | 6359.68         | 72122.88        | no                    |
| 300                | 24        | 2500       | 4       | 80               | 10             | 9555.36         | 88564.8         | no                    |
| 350                | 26        | 2500       | 4       | 80               | 9              | 9721.76         | 81205.92        | no                    |
| 400                | 28        | 2500       | 4       | 80               | 8              | 9888.16         | 73514.24        | no                    |
| 450                | 30        | 2500       | 4       | 80               | 7              | 10054.56        | 65489.76        | no                    |

###Result: The minimum flight cost is $65489.76 ;with 450 passenger capacity; 4 engines configuration
- The design of 100-200 passenger capacity is not suitable because it exceed the flight limit for 12 flight per week maximum.
- The overall result shows that use a four-engine configuration for capacities over 300 can maximize the number of passengers per flight, minimize the number of flights and balancing costs.

