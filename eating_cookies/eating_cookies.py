#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  #Add all the n -1 combinations with 1 in front
  #Add all the n-2 combinations with a 2 in front
  #Add all hte n-3 combinations with a 3 in front
  if cache is None or type(cache) == list:
    cache = {0: 1, 1: 1, 2: 2}
  if n < 0:
    return 0
  elif n not in cache:
    cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')