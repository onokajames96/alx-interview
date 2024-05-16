#!/usr/bin/python3
""" Prime Game."""


def sieve(max_num):
    """
    Generate a list of prime numbers up to max_num using
    the Sieve of Eratosthenes.
    """
    is_prime = [True] * (max_num + 1)
    is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
    p = 2
    while (p * p <= max_num):
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def count_primes_up_to(n, is_prime):
    """Count the number of prime numbers from 1 up to n."""
    count = 0
    for i in range(1, n + 1):
        if is_prime[i]:
            count += 1
    return count


def isWinner(x, nums):
    """Determine the winner of the Prime Game."""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    is_prime = sieve(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_up_to(n, is_prime)
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
