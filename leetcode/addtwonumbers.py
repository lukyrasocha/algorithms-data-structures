#https://leetcode.com/problems/add-two-numbers/
# Author: Lukas Rasocha

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
     
        if l1.val + l2.val < 10:
            first = ListNode(val=l1.val+l2.val,next=None)
            temp = 0
        else:
            first = ListNode(val = int(str(l1.val+l2.val)[1]))
            temp = 1
            
        z = first
        
        while l1 != None or l2 != None or temp != 0:
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            
            if l1 == None and l2 != None:
                #x = l1.val + l2.val + temp
                x = l2.val + temp
            elif l2 == None and l1 != None:
                x = l1.val + temp
                
            elif l1 != None and l2 != None:
                x = l1.val + l2.val + temp
                
            else:
                if temp == 1:
                    first.next = ListNode(val = 1)
                return z
            
            if x < 10:
                node = ListNode(val=x)
                temp = 0
                
            else:
                node = ListNode(val = int(str(x)[1]))
                temp = 1
            
            first.next = node
            first = node
            
        return z
