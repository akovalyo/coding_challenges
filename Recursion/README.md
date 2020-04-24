# Recursion

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


 ***

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

 ***

### Exercise 3

Write a function **is_member(my_list, elem)** that returns **True** if **elem** is a member of my_list and **False** otherwise. For example, **is_member([’c’,’a’,’t’],’a’)** should return **True**. Do not use any of Python's built-in list methods or an operator like in.

<details>
	<summary>Solution</summary>

    def  is_member(my_list,elem):

        if not my_list:
            return False
        if elem == my_list[0]:
            return True
        else:
            return is_member(my_list[1:], elem)

</details>

### Exercise 4

Write the function **remove_duplicates(list1)**, using recursion, which eliminates duplicates in a sorted list. **list1** is a list sorted in ascending order. Function should return new sorted list with the same elements as the input, but without any duplicate elements.

<details>
	<summary>Solution</summary>

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

### Exercise 5

Write the function **merge_sort(list1)**, using recursion. **list1** is an unsorted list. Function should return a new sorted list that contains all of the elements in **list1** sorted in ascending order. Not allowed to use *set*, *sorted* or *sort*.

<details>
	<summary>Solution</summary>

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

### Exercise 6

Write a function **is_member(my_list,elem)** that returns **True** if **elem** is a member of **my_list** and **False** otherwise. For example, **is_member([’c’,’a’,’t’],’a’)** should return **True**. Do not use any of Python's built-in list methods or an operator like *in*.

<details>
	<summary>Solution</summary>

    def is_member(my_list,elem):
        if not my_list:
            return False
        else:
            if my_list[0] == elem:
                return True
            else:
                return is_member(my_list[1:], elem)

</details>