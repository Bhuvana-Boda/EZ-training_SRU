************************binary search tree**************************
* Binary tree  time complexity is O(n)
* left<root<right
* elements in left binary search tree should be less than the root.
* elements in right should be the greater than the root node.
* time complexity of binary search tree is O(n*logn).
* if we want to find the min element,we need to traverse to the left part.
* whereas we need to traverse right to get the maximum element of the binary search tree.

if i is the parent node Index:
then left=2i+1
ie. right=2i+2 

* if we need to insert element, we need to check the hEIGHT balancing.
* height balancing is a imp concept.
* if bst is height balanced then searching of an element takes O(logn) time onlyy.

eg: 1 2 3 4 5 6
mid element is 3
* left elements of 3 will be lesser elements to rootnode.
* right elements will be the greater elements for rootnode.
then the tree will be height balancing.
--->BREADTH FIRST SEARCH:
*USES QUEUE.
*STARTS with one node and checks other nodes.

-----------------------------------------------------------------------------
:::::>700)seacrh in a binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def _init_(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return 
        if root.val==val:
            return root
        elif root.val>val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
------------------------------------------------------------------------------
:::::>108)convert sorted array into binary search tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(si,li):
            if si<=li:
                mid=(si+li)//2
                root=TreeNode(nums[mid])
                root.left=fun(si,mid-1)
                root.right=fun(mid+1,li)
                return root
        return fun(0,len(nums)-1)
-----------------------------------------------------------------------------
:::::>701)insert into a binary search tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root==None:
            return TreeNode(val)
        if root.val>val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
----------------------------------------------------------------------------
:::::>104)finding the maximum depth of the binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            leftdepth=self.maxDepth(root.left)
            rightdepth=self.maxDepth(root.right)
            return 1+ max(leftdepth,rightdepth)  #1 is for node.
---------------------------------------------------------------------------
:::::>breadth first search

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if not edges:
            return True
        d={i: [] for i in range(n)}
        for i,j in edges:
            d[i].append(j)
            d[j].append(i)
        q=[source]
        vis=set()
        while q:
            a=q.pop(0)
            for i in d[a]:
                if i==destination:
                    return True
                if i not in vis:
                    q.append(i)
                    vis.add(i)
        return False
---------------------------------------------------------------------------
:::::>1791)find the center of the star graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0]==edges[1][0] or edges[0][0]==edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
----------------------------------------------------------------------------
:::::>997)find the town judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count=[0]*(n+1) 
        for a,b in trust:
            count[a]-=1
            count[b]+=1 
        for i in range(1,n+1):
            if count[i]==n-1:
                return i
        return -1











