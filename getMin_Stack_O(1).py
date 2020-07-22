# Use Stack to retrieve Minimum element in O(1) Time

class SpecialStack:
  def __init__(self):
    self.top = -1
    self.stack = []
    self.minVal = float("-inf")

  def push(self, x):
    if self.top == -1:
      self.stack.append(x)
      self.minVal = x
    elif x < self.minVal:
      # For easy retrieval of previous minVal later => new_push_ele = 2*push_ele - curr_min, curr_min = push_ele
      self.stack.append((2*x-self.minVal))
      self.minVal = x
    else:
      self.stack.append(x)
    self.top += 1

  def pop(self):
    if self.top == -1:
      return "Error"
    # if element being removed is lesser than curr minVal then it is the minVal being removed
    elif self.stack[self.top] < self.minVal:
      y = self.minVal
      # Retrieving of previous minVal after popping existing minval => new_min = 2*curr_min - pop_ele
      new_minVal = (2*self.minVal - self.stack[self.top])
      self.minVal = new_minVal
      self.stack.pop(self.top)
    else:
      y = self.stack.pop(self.top)
    self.top -= 1
    return y

stack = SpecialStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)
stack.push(-1)

print(stack.stack)

print(stack.pop())
print(stack.pop())
print('Min Value now = '+str(stack.minVal))


'''
:- Output
[3, 5, 1, 0, -3]
-1
1
Min Value now = 2
'''

'''
Additional Note: How to do it for Max element?
push := if (push_ele > curr_max) then (new_push_ele = 2*push_ele + curr_max)

for eg. [3] <-- 5       min = 3
        since 5 > 3 then 2*5+3 = 13, now
        [3] <-- 13
        [3, 13]         min = 5 

pop := if (pop_ele > curr_max) then (new_max = pop_ele - 2*curr_max)

for eg. [3,13]          min = 5
        since 13 should be popped and 13 > 5, hence 13-2*5 = 3
        [3] --> 13
        [3]              min = 3
'''
