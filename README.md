# DAA-assignment

Presentation of MAXIMUM SUM SUBARRAY.

ASSIGNMENT QUESTION : 

Implement the solution for Maximum Sum Array by populating the array of size 14 with non-zero [positive/negative] random numbers.
Comment on sum, if first element is positive/negative and last element is positive/negative


Approach: Following steps are performed in order to find Maximum Crossing Sum Subarray: 

Step 1: Find mid location of the array  [mid=(low+high)/2] 

Step 2: Perform sum for the left component and find out the value of MAX SUM and LEFT MOST POINT of the array . 

Step 3: Perform sum for the right half array and find out the value of MAX SUM and LEFT MOST POINT of the array.

Solved Example: a= [ 5, -3, 9, 12, -8, 7, 11, -9, 1, -2, 4, 6] (From classwork)
mid=(low+high)/2=(1+12)/2=13/2=6.5=6 
Maximum sum from left side is 22 and from right side is 11
Maximum sum at crossing is 33 hence maximun sum array is 33 starting from index - 0 and end index - 7 
Crossing subarray of maximum sum is: b= {5, -3, 9, 12, -8, 7, 11} Maximum sum is: 33


Test Case 1: first element positive & last element positive 
a=[65,20,91,-56,28,83,74,-40,24,73,59,28,-30,35] 

First and last elements are positive,
Sum of MAXIMUM SUM ARRAY:  454


Test Case 2: Both first & last negative 
a=[-65,20,91,-56,28,83,74,-40,24,73,59,28,-30,-35] 


First and last elements are negative,
Sum of MAXIMUM SUM ARRAY:  384

Test Case 3: first element positive & last element negative 
a=[65,20,91,-56,28,83,74,-40,24,73,59,28,-30,-35] 

First element is positive and last element is negative,
Sum of MAXIMUM SUM ARRAY:  449

Test Case 4: first element negative & last element positive 
a=[-65,20,91,-56,28,83,74,-40,24,73,59,28,-30,35] 

First element is negative and last element is positive,
Sum of MAXIMUM SUM ARRAY:  389
![image](https://user-images.githubusercontent.com/102512172/191579950-bfcf4500-679d-4a6d-8b82-1acef482613f.png)

OBSERVATION: 
Sum obtained in the case-01 where first and last element is positive is the largest. 
Second largest is case-03 where first element is positive and last element is negative. 
The lowest sum is in the case-02 where both elements are negative. 

CONCLUSION: 
Therefore we can conclude that the sum of maximum subArray will be largest when both element are positive and least when both are negative.
