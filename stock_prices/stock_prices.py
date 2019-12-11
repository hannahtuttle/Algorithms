#!/usr/bin/python

# You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 
# 
# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.
# 
# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

  # understand: trying to write down what i understand about this problem before i plan it out....
    # it seams like the list is one stock through out the day. Like the example the max gain would be if you bought the stck when it cost 270 and let it rise to 3800 that would be the max that you could earn from that list in one day.
    #  seams like you need your function to check what the value of the first amount (as a negative since that is what you are spending) plus each following value in the list like this:
    #       -1050 + 270 = -780      # would be a loss
    #       -1050 + 1540 = 490      # would be a gain
    #       -1050 + 3800 = 2750      # would be a gain , and it is greater that the previous amount that could be gained.
    #  and then do that for the second number in the list to the second to last number in the list and then return the highest difference from all the math problems.

  # plan: not sure if this is how i am supposed to plan or not.
    # write a loop that make the fist value a negative and then loops through the second array a second time start at the second value and test the difference between the. 
    # have a place to storethe largest amount gained
    # check to see if the stored amount gained is less that the current amount gained, if it is replace the amoount gained with the current amount.

  # code

import argparse

def find_max_profit(prices):
  largest_gain = 0 
  start_sub = 1
  saved_val = []
  for i in range(0, len(prices) - 1):
    for j in range(start_sub, len(prices)):
      current_difference = -prices[i] + prices[j]
      print(f'current difference for the value at index {i}', current_difference)
      saved_val.append(current_difference)
      if largest_gain < current_difference:
        largest_gain = current_difference
      else:
        pass
    start_sub +=1
    print(saved_val)
    if largest_gain == 0:
      largest_gain = saved_val[0]
      for i in range(0, len(saved_val)):
        if largest_gain < saved_val[i]:
          largest_gain = saved_val[i]
        else:
          pass
    else:
      pass
  return largest_gain

sample = [100, 90, 80, 50, 20, 10]
print(find_max_profit(sample))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))