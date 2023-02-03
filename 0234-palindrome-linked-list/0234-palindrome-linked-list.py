class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1=[]
        while head:
            list1.append(head.val)
            head=head.next
        list2=[]
        for i in range(len(list1)-1,-1,-1):
            list2.append(list1[i])
        for i in range(len(list1)):
            if  list1[i] != list2[i]:
                return False
        return True