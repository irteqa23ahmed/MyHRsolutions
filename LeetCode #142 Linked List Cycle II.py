'''
Problem
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?
Solution
Use two pointer with different speed, say runner and walker, and make runner be twice faster than walker. 
If there is no cycle in this linked list, runner will finally run through entire list without meet walker.
If there exists a cycle, they will meet each other at a node, say x, and x represents the x-th node in this list. 
Let’s assume the position of cycle start is at y-th node and the length of cycle is m.
About runner, it has already run 2x nodes, which is equal to y + m + (x — y) (length to cycle start + length of cycle + nodes to meet walker). 
So we have 2x = y + m + (x — y), and it can conduct to x = m.
About walker, it needs to walk more m — (x — y) = m — x + y nodes to reach cycle start. As we know in 1 that x is equal to m, 
walker needs to walk more y nodes to reach the node of cycle start.
By 1 and 2, we can put another pointer, say seeker, with the same speed as walker at the head.
Because seeker also needs y move nodes to reach the node of cycle start, the node that seeker and walker meet each other will be what we are looking for.
'''

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        found = False
        temp1,temp2 = head, head
        while temp1!=None and temp2!=None:
            
            temp1 = temp1.next
            temp2 = temp2.next
            
            if temp2 == None:
                return 
            else:
                temp2 = temp2.next
            if temp1 == temp2:
                found = True
                break
            
        if found == True:
            seeker = head
            while seeker!=temp1:
                seeker = seeker.next
                temp1 = temp1.next
            return seeker
        return
