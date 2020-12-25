#coding:utf8



#def primes(starting: int = 2):
def primes(starting=2):
    """Yield the primes in order.
    
    Args:
        starting: sets the minimum number to consider.
    
    Note: `starting` can be used to get all prime numbers
    _larger_ than some number. By default it doesn't skip
    any candidate primes.
    """
    candidate_prime = starting
    while True:
        candidate_factor = 2
        is_prime = True
        # We'll try all the numbers between 2 and
        # candidate_prime / 2. If any of them divide
        # our candidate_prime, then it's not a prime!
        while candidate_factor <= candidate_prime // 2:
            if candidate_prime % candidate_factor == 0:
                is_prime = False
                break
            candidate_factor += 1
        if is_prime:
            yield candidate_prime
        candidate_prime += 1
      

#素数生成器
      
i=0        
for p in primes():
    print(p)
    i += 1
    if i >= 10:
        break


        
        