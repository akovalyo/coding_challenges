# Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
 
```
Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 
Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 
```

***

# Solution

### C:

```c
int	bin_count(int nbr)
{
	if (nbr >= 2)
		return (1 + bin_count(nbr / 2));
	return(1);
}

int findComplement(int num)
{
    return (num ^ ((long)pow(2, bin_count(num)) - 1));
}
```

### Python:

```python
class Solution:
    def findComplement(self, num: int) -> int:
        length = len(bin(num)[2:])
        return (num ^ ((2 ** length) - 1))
```

