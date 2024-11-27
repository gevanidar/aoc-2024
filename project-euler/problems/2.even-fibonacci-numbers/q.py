
if __name__ == "__main__":
    fib_last = 1
    fib_current = 2
    total = 2
    while True:
        fib_next = fib_last + fib_current
        if fib_next > 4000000:
            break
        if fib_next % 2 == 0:
            total += fib_next
        fib_last = fib_current
        fib_current = fib_next
    print(total)

            
    
