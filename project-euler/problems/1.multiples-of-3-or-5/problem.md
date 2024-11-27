# Problem
Multiples of 3 or 5
Problem 1
If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.
Find the sum of all the multiples of $3$ or $5$ below $1000$.

# Info
Factors: [3, 5]
Multiples: [3, 5, 6, 9]
Below: 10
Summation of Multiples: 23

# Thoughts
To find the multiples below 10 for 3 we will have to se how many times 10 can be divided by 3.
```
  times = floor(10 / 3) # 3
```
We can do the same for 5:

```
  times = floor(10 / 5) # 1
```

When adding all values of the multiples from 3 (3, 6, 9) we get 18. This can be calculated either by summation or by the Arithmetic mean:
```
  arithmetic_mean = 18 / 3 = 6
```
If the number of times we can divide n by m is even the mean can also be calculated as half the value of the sum of the lowest (3) and highest product (9):
```
  arithmetic_mean = (3 + 9) / 2 = 6
```

This would for the first case (below 10) give us the formula:
```
  sum_of_multiples = times_3 + arithemtic_mean_3 + times_5 + arithemtic_mean_5 
  sum_of_multiples = floor(10 / 3) * (3 + floor(10 / 3) * 3) +  floor(10 / 5) * 5 + floor(10 / 5) * 5
  sum_of_multiples = 3 * 6 + 1 * 5 = 18 + 5 = 23
```


