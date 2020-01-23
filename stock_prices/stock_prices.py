#!/usr/bin/python

import argparse

test1 = [10, 7, 5, 8, 11, 9]

def find_max_profit(prices):
  max_prof = float('-inf')
  #Subtract each number on the right. 
  for i in range(0, len(prices) -1):
      index = i
      for j in range(index + 1, len(prices) -1):
        profit = prices[j] - prices[index]
        if profit > max_prof:
            max_prof = profit
  print(max_prof)
  return max_prof
    
print(len(test1))
find_max_profit(test1)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))