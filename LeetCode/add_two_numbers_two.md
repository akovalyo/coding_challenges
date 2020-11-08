# 445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

**Definition for singly-linked list**

```python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

**Example:**

```
Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
```

***

# Solution

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getDigit(lst):
            digit = 0
            while lst:
                digit = digit * 10 + lst.val
                lst = lst.next
            return (digit)
            
        summ = getDigit(l1) + getDigit(l2)
        l3 = ListNode(0) if summ == 0 else None
        while summ:
            value = summ % 10
            l3 = ListNode(value, l3)
            summ = summ // 10
        return l3
```