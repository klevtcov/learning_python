# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        result = []
        result.extend(list1)
        result.extend(list2)
        result = result.sort()
        return result


if __name__ == '__main__':
    list1 = [1,2,4] 
    list2 = [1,3,4]
    solution = Solution()

    print(solution.mergeTwoLists(list1, list2))



# Output: [1,1,2,3,4,4]

def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    result = []
    result.extend(list1)
    result.extend(list2)
    result = result.sort()
    return result


if __name__ == '__main__':
    list1 = [1,2,4] 
    list2 = [1,3,4]
    
    print(mergeTwoLists(list1, list2))