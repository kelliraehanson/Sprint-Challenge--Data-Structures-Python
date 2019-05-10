Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
Answer: When I run this the test runs in 0.000s! (Not an eternity). So I would say because of the fact that the append method contains one if statement the runtime complexity for this would be 0(n). Which would be
considered to be "Fair" and Linear Time on the Big-O Complexity Chart.

2. What is the space complexity of your ring buffer's `append` function?
Answer: Space Complexity of an algorithm is total space taken by the algorithm. I would say that the space complexity of the append function would be 0(n) because it has two variable. Which is reserved memory locations to store values.

3. What is the runtime complexity of your ring buffer's `get` method?

4. What is the space complexity of your ring buffer's `get` method?

5. What is the runtime complexity of the provided code in `names.py`?

6. What is the space complexity of the provided code in `names.py`?

7. What is the runtime complexity of your optimized code in `names.py`?

8. What is the space complexity of your optimized code in `names.py`?


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