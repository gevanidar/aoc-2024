# Problem
Largest Prime Factor
Problem 3
The prime factors of $13195$ are $5, 7, 13$ and $29$.
What is the largest prime factor of the number $600851475143$?

# Info
Prime factors are numbers which only return an integer number when divided by itself and 1. 
```
  n / n = 1
  n / 1 = n
  n / m -> d
  where n and m are integers and d is a decimal number
```

# Thoughts
By calculating 'all' prime numbers and sending them into a file we can then reuse this file later if we need larger prime factors. (This probably exists)

We can also se that the first prime number 2 is not a divider since the number is odd.


Are there any smarter ways then just looping through each prime number?
  - Like stepping up and down with similar prime number products
  ```
    2*3*3 ~= 3*3*3
  ```
