Add your answers to the questions below.

## Question
1. What is the runtime complexity of your ring buffer's `append` method?

## Answer
Answer: When I run this the test runs in 0.000s! (Not an eternity). So I would say because of the fact that the append method contains one if statement the runtime complexity for this would be 0(n). Which would be
considered to be "Fair" and Linear Time on the Big-O Complexity Chart.

## Question
2. What is the space complexity of your ring buffer's `append` function?

## Answer
Answer: Space Complexity of an algorithm is total space taken by the algorithm. I would say that the space complexity of the append function would be 0(n) and considered to be "Fair" and Linear Time on the Big-O Complexity Chart.

## Question
3. What is the runtime complexity of your ring buffer's `get` method?

## Answer
Answer: When I run this the test runs in 0.000s. Considering this method has a for and if statement I would say the runtime complexity for this would be 0(n). Which would be considered to be "Fair" and Linear Time on the Big-O Complexity Chart.

## Question
4. What is the space complexity of your ring buffer's `get` method?

## Answer
Answer: Space Complexity of an algorithm is total space taken by the algorithm. I would say that the space complexity of the ring buffer's 'get' method would be 0(1). Which would be considered to be "Good" and Constant Time on the Big-O Complexity Chart.

## Question
5. What is the runtime complexity of the provided code in `names.py`?

## Answer
Answer: I ran this code a few times and the runtime complexity was always over 8 seconds 
and a few times was over 12 seconds. Like stated in the readme, it does feel like an eternity.
The provided code had two for loops so I would say the runtime complexity is 0(n^2) which
is considered "Horrible" and Quadratic Time on the Big-O Complexity Chart.

## Question
6. What is the space complexity of the provided code in `names.py`?

## Answer
Answer: Space Complexity of an algorithm is total space taken by the algorithm. I would say that the space complexity of the provided code in names.py would be 0(1). Which would be considered to be "Good" and Constant Time on the Big-O Complexity Chart.

## Question
7. What is the runtime complexity of your optimized code in `names.py`?

## Answer
Answer: I was able to get the run time of the provided code down to 1.7 seconds. Which is 
significantly less than the provided code was. What I did to change this code to be less of a runtime
complexity was I made one for loop with a nested if statement instead of two for loops. I would say 
that this would mean it is 0(n) and considered to be "Fair" and Linear Time on the Big-O Complexity Chart.

## Question
8. What is the space complexity of your optimized code in `names.py`?

## Answer
Answer: Space Complexity of an algorithm is total space taken by the algorithm. I would say that the space complexity of the provided code in names.py would be 0(1). Which would be considered to be "Good" and Constant Time on the Big-O Complexity Chart.


## What is a Ring Buffer?
 
 A Ring Buffer is a buffer with a fixed size, so when is filled up, adding another element must overwrite the first (oldest) one. This kind of data structure is useful for sorting log and history information.

### Table of Common Time Complexities

|          Name        |  Time Complexity  |
|----------------------|-------------------|
|      Constant Time   |         0(1)      |
|   Logarithmic Time   |       0(log n)    |
|     Linear Time      |       0(n)        |
|   Quasilinear Time   |     0(n log n)    |
|    Quadratic Time    |       0(n^2)      |
|   Exponential Time   |       0(2^n)      |
|    Factorial Time    |        0(n!)      |