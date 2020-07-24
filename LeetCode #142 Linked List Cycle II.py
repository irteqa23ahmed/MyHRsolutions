'''
Problem
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space?

Solution in description
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
