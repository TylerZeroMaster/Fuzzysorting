# Fuzzysorting
 Some kind of sorting algorithm I made in 2017. It works by finding the "slope" of an array, and then using slope-intercept form to determine the approximate location where a number belongs. 
 It adds these approximations to contiguous lists of numbers with a similar approximate index.
 After each number’s position has been approximated, each list is bubble sorted and joined together to make one fully sorted list.

 ## Comparison

 #### Fuzzy sort
 ![Fuzzy sort is faster than the other two](./visual/fuzzy_sort.gif) 
 #### Bubble sort
 ![Bubble sort is the slowest](./visual/bubble_sort.gif)
 #### Insertion sort
 ![Insertion sort is the second slowest](./visual/ins_sort.gif)


