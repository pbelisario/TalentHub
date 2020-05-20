    
# [War Games](https://en.talenthub.jp/coding_test/show/56)
Ichiro got a collection of N toy tanks for his birthday. He called his friend Hideki to come play with him. They made a battlefield – a wooden board consisting of squares in N rows and N columns.
Each tank can be moved to one of the four neighbouring squares in a single move. A tank can shoot at any square in the same row or column. The tank is said to be guarding the row and column it is in.
Additionally, no two tanks can be in the same square at the same time.
After the boys had been playing for many hours, Ichiro’s mom repeatedly yelled for them to come down for lunch, and the boys decided to rearrange the tanks so that each tank guards a different row and column (meaning also that each row and column contains only one tank).
However, they want to do this using the minimum number of moves.
Write a program that finds the minimum number of moves required to rearrange the tanks so that each row and each column contains a single tank.

## INPUT

- The first line of input contains the integer N (5 ≤ N ≤ 500).
- Each of the following N lines contains two integers R and C (1 ≤ R, C ≤ N), the row and column of a single tank at the moment of mom's call. No two tanks are on the same square.
- Rows and columns are marked 1 through N, top-down and left-to-right.
## OUTPUT

- Output the minimum number of moves.

### Sample Input
5
2 3
3 2
3 3
3 4
4 3
### Sample Output
8