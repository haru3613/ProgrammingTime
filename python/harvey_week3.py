class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums = sorted(nums)
        return nums.index(target)
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        
        self.get_none(l1)
    
    def get_none(self, lt):
        if lt != None:
            print(lt)
            self.get_none(lt.next)
        else:
            return lt