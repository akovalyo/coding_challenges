# Min Cost Climbing Stairs

You are given an integer array cost where _cost[i]_ is the cost of **i**th step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

**Examples:**

```
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
```

**Constraints:**

```
2 <= cost.length <= 1000
0 <= cost[i] <= 999
```

# Solution

### Python

1.

```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
    minCosts = [0 for _ in range(len(cost) + 1)]
    for i in range(2, len(cost) + 1):
        oneStep = cost[i-1] + minCosts[i-1]
        twoSteps = cost[i-2] + minCosts[i-2]
        minCosts[i] = min(oneStep, twoSteps)
    return minCosts[-1]

```

2.

```python
def minCostClimbingStairs(self, cost: List[int]) -> int:
    @lru_cache
    def minCosts(i):
        if i <= 1:
            return 0
        oneStep = cost[i-1] + minCosts(i-1)
        twoSteps = cost[i-2] + minCosts(i-2)
        return min(oneStep, twoSteps)
    return minCosts(len(cost))

```

### C

```c
int minCostClimbingStairs(int* cost, int costSize){
    int *minCosts;
    int oneStep = 0;
    int twoSteps = 0;
    int res = 0;

    minCosts = (int *)malloc(sizeof(int) * (costSize + 1));
    minCosts[0] = minCosts[1] = 0;
    for(int i=2; i <= costSize; i++){
        oneStep = cost[i-1] + minCosts[i-1];
        twoSteps = cost[i-2] + minCosts[i-2];
        minCosts[i] = oneStep <= twoSteps ? oneStep : twoSteps;
    }
    res = minCosts[costSize];
    free(minCosts);
    return(res);
}
```
