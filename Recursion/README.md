# Recursion

Solve all problems with recursion

### Exercise 1

Write a function **num_sum(num)** that computes the arithmetic sum 0 + 1 + 2... + (num-1) + num0+1+2...+(num−1)+num. For example **num_sum(3)** should return **6**. 

<details>
	<summary>Solution C</summary>
    
    int num_sum(int num)
    {
        if (num == 0)
            return (0);
        else
            return (num + num_sum(num - 1));
    }
 
 </details>

<details>
	<summary>Solution Python</summary>
    
    def  num_sum(num):

        if num == 0:
            return 0
        else:
            return num + num_sum(num - 1)
 
 </details>

___

 ### Exercise 2

 Write a function **num_of_threes(num)** that returns the number of times the digit **3** appears in the decimal representation of the non-negative integer **num**. For example **num_of_threes(34534)** should return **2**

<details>
	<summary>Solution C</summary>

    int num_of_threes(int num)
    {
        int digit, rest;

        if (num == 0)
            return (0);
        else
        {
            digit = num % 10;
            rest = num_of_threes(num / 10);
            if (digit == 3)
                return (rest + 1);
            return (rest);
        }
    }

</details>

 <details>
	<summary>Solution Python</summary>
	
    def  num_of_threes(num):

        if num == 0:
            return 0
        else:
            digit = num % 10
            rest = num_of_threes(num // 10)
            if digit == 3:
                return rest + 1
            else:
                return rest
	    
 </details>

___

### Exercise 3

Write a function that reverses a string using recursion. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

<details>
	<summary>Solution C</summary>
    
    void reverseString(char* s, int sSize) 
    {
        char tmp;
        
        if (sSize <= 0)
            return ;
        tmp = s[0];
        s[0] = s[sSize - 1];
        s[sSize - 1] = tmp;
        reverseString(s + 1, sSize - 2);
    }
</details>

___

### Exercise 4

Write a function **is_member(my_list, elem)** that returns **True** if **elem** is a member of my_list and **False** otherwise. For example, **is_member([’c’,’a’,’t’],’a’)** should return **True**. Do not use any of Python's built-in list methods or an operator like in.

<details>
	<summary>Solution Python</summary>

    def  is_member(my_list,elem):

        if not my_list:
            return False
        if elem == my_list[0]:
            return True
        else:
            return is_member(my_list[1:], elem)

</details>

___

### Exercise 5

Write the function **remove_duplicates(list1)**, using recursion, which eliminates duplicates in a sorted list. **list1** is a list sorted in ascending order. Function should return new sorted list with the same elements as the input, but without any duplicate elements.

<details>
	<summary>Solution Python</summary>

    def remove_duplicates(list1):

        ind = 0
        while ind < len(list1) and  (ind + 1) < len(list1):
            if list1[ind] == list1[ind+1]:
                left = list1[:ind]
                right = list1[ind+1:]
                return left + remove_duplicates(right)
            ind += 1
        return list1

</details>

___

### Exercise 6

Write the function **merge_sort(list1)**, using recursion. **list1** is an unsorted list. Function should return a new sorted list that contains all of the elements in **list1** sorted in ascending order. Not allowed to use *set*, *sorted* or *sort*.

<details>
	<summary>Solution Python</summary>

    def merge(list1, list2):
    
        sorted_list = []
        while list1 and list2:
            if list1[0] < list2[0]:
                sorted_list.append(list1.pop(0))
            else:
                sorted_list.append(list2.pop(0))
        if not list1:
            sorted_list += list2
        elif not list2:
            sorted_list += list1
        return sorted_list
                
    def merge_sort(list1):
    
        if len(list1) < 2:
            return list1
        else:
            middle = len(list1) // 2
            return merge(merge_sort(list1[:middle]), 
                        merge_sort(list1[middle:]))

</details>

___

### Exercise 7

Write a function **remove_x(my_string)** that takes the string **my_string** and deletes all occurrences of the character **’x’** from this string. For example, **remove_x("catxxdogx")** should return **"catdog"**. You should not use Python's built-in string methods.

<details>
	<summary>Solution 1 Python</summary>

    def remove_x(my_string):
        if my_string == "":
            return ""
        for i in range(len(my_string)):
            if my_string[i] == "x":
                left = my_string[:i]
                return left + remove_x(my_string[i+1:])
        return my_string

</details>

<details>
	<summary>Solution 2 Python</summary>

    def remove_x(my_string):
        if my_string == "":
            return ""
        else:
            first_character = my_string[0]
            rest_removed = remove_x(my_string[1 :])
            if first_character == 'x':
                return rest_removed
            else:
                return first_character + rest_removed

</details>

___

### Exercise 8

Write a function **insert_x(my_string)** that takes the string **my_string** and adds the character **’x’** between each pair of consecutive characters in the string. For example, **insert_x("catdog")** should return **"cxaxtxdxoxg"**.

<details>
	<summary>Solution Python</summary>

    def insert_x(my_string):
        if len(my_string) <= 1:
            return my_string
        first = my_string[0] 
        rest = insert_x(my_string[1:])
        return first + "x" + rest

</details>

___

### Exercise 9

Write a function **list_reverse(my_list)** that takes a list and returns a new list whose elements appear in reversed order. For example, **list_reverse([2,3,1])** should return **[1,3,2]**. Do not use the *reverse()* method for lists.

<details>
	<summary>Solution Python</summary>

    def list_reverse(my_list):
        if my_list == []:
            return []
        else:
            first = my_list[0]
            rest = list_reverse(my_list[1:])
            return rest + [first]
</details>

___

### Exercise 10

Write a function **gcd(num1,num2)** that takes two non-negative integers and computes the greatest common divisor of **num1** and **num2**. To simplify the problem, you may assume that the greatest common divisor of zero and any non-negative integer is the integer itself. For an extra challenge, your programs should only use subtraction. Hint: If you get stuck, try searching for "Euclid's Algorithm".

___

### Exercise 11

Write a function **slice(my_list,first,last)** that takes as input a list **my_list** and two non-negative integer indices **first** and **last** satisfying *0 ≤ first ≤ last ≤ n* where *n* is the length of **my_list**. **slice** should return the corresponding Python list slice **my_list[first:last]**. For example, **slice(['a', 'b', 'c', 'd', 'e'], 2, 4])** should return **[’c’,’d’]**.Important: Your solution should not use Python's built-in slice operator **:** anywhere in its implementation. Instead use the method **pop** to remove one element from the input list during each recursive call. (You may mutate the input list to simplify your solution.)

___

### Exercise 12

There is a series, **S**, where the next term is the sum of pervious three terms. Given the first three terms of the series, **a**, **b**, and **c** respectively, you have to output the **n**-th term of the series using recursion.

**Input Format:**

The first line contains a single integer, **n**.

The next line contains 3 space-separated integers, **a**, **b**, and **c**.

**Constraints:**

1 <= n <= 20

1 <= a, b, c <= 100


**Output Format**

Print the n-th term of the series, **S(n)**.

**Example:**

```
Input:
5
1 2 3

Output:
11
```

<details>
	<summary>Solution C</summary>

    #include <stdio.h>

    int find_nth_term(int n, int a, int b, int c) 
    {
        if (n == 4)
            return (a + b + c);
        return (find_nth_term(n-1, b, c, (a + b + c)));
    }

    int main() 
    {
        int n, a, b, c;
    
        scanf("%d %d %d %d", &n, &a, &b, &c);
        int ans = find_nth_term(n, a, b, c);
    
        printf("%d", ans); 
        return 0;
    }
</details>

___

### Exercise 12

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

<details>
	<summary>Solution Python</summary>
    
    def getRow(rowIndex):
        if rowIndex == 0:
            return [1]
        last = getRow(rowIndex - 1)
        return [1]+[last[i] + last[i + 1] for i in range(len(last) - 1)]+[1]
 
 </details>