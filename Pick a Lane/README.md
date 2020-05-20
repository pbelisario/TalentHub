# [Pick a Lane](https://en.talenthub.jp/coding_test/show/142)
Tom has some friends visiting him in TK City, so he takes them on a sightseeing tour. The are 1000 sites to see on the tour, numbered from 0 -> 999, and various options for scenic transportation to choose from: double-decker bus, motorbike taxi, horse-drawn carriage, river ferry, limousine, tuk-tuk, dog sled, stand-up paddleboard, roller skates, rickshaw, tandem bicycle, etc.

The group decides on sites to begin (S) and end (F) their tour. They might make some stops in between, but they want to keep the cost as low as possible so they have money leftover for a nice dinner.

The distance and cost of a ride on each mode of transportation is calculated as follows:
Starting at site Y, a ride on i will take you to site (A[i] * Y + B[i]) and costs C[i].

What is the cheapest way for the group to travel from S -> F?

### Input

-    S F
-    K modes of transportation
-    A[i] B[i] C[i] for each mode of transportation

### Output

-   The cost of traveling from S to F. If it is not possible, print “-1”.

### Limit

-   1<=K <= 50
-   1<=A[i], B[i], C[i] <= 1000

### Sample Input
2 10
3
2 2 5
1 4 4
1 2 3

### Sample Output
8


### Explanation

- Tom could use method 2 twice in a row: first from site 2 to 6, costing 4, and then from 6 to 10, costing 4 again. The total cost is 8.