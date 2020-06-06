# Random Pick with Weight

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

```

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

```
**Examples:**

```
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]

Output: [null,0]


Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]

Output: [null,0,1,1,1,0]
```

# Solution

```python

import random

class Solution:

    def __init__(self, w: List[int]):
        self.arr = []
        summ = 0
        for num in w:
            summ += num
            self.arr.append(summ)
        
    def pickIndex(self) -> int:
        ran = random.randint(1, self.arr[-1])
        a = 0
        b = len(self.arr)
        while a < b:
            mid = a + (b - a) // 2
            if ran > self.arr[mid]:
                a = mid + 1
            else:
                b = mid
        return a if a <= ran else b

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

```