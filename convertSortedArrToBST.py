class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrToBST(self, nums):
        total_nums = len(nums)
        if not total_nums:
            return None
        mid_node = total_nums//2
        return TreeNode(
            nums[mid_node], 
            self.sortedArrToBST(nums[:mid_node+1]),  
            self.sortedArrToBST(nums[mid_node:])
        )