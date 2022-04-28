#leetcode 428 序列化和反序列化N叉树
# leetcode 449 序列化反序列化二叉搜索树
# leetcode 105从前序与中序遍历序列构造二叉树
import queue


class treenode():
    def __init__(self,data = 0,leftnode = None,rightnode = None):
        self.data = data
        self.left = leftnode
        self.right = rightnode
    def __str__(self):
        return str(self.data)

#反序列化 e.g leetcode:[1,2,3,4,null,2,4,null,null,4] 华为：[1,2,3,4,#,2,4,#,#,#,#,4,#,#,#]
#层序遍历 [1,2,3,null,null,4,5]
    #         1
    #     2       3
    # #      # 4     5
class Solution:
    #层序遍历的反序列化使用index
    def buile_huawei(self,list,index):
        if index >=len(list):
            return
        if list[index] != '#':
            root = treenode(list[index])
            root.left = self.buile_huawei(list,2*index+1)
            root.right= self.buile_huawei(list,2*index+2)
        else:
            return
        return root
    #前序反序列dfs
    def build_dfs(self,list):
        if not list:
            return
        temp = list.pop(0)
        if temp == 'None':
            return
        root = treenode(int(temp))

        root.left = self.build_dfs(list)
        root.right =self.build_dfs(list)
        return root
    #层序反序列bfs
    def build_bfs(self,list):
        queue = []
        a = treenode(int(list.pop(0)))
        queue.append(a)
        while(queue):
            temp = queue.pop(0)
            if temp== 'None':
                continue
            x = list.pop(0)
            temp.left= treenode(int(x)) if x != '#' else 'None'
            x = list.pop(0)
            temp.right = treenode(int(x)) if x != '#' else 'None'
            queue.append(temp.left)
            queue.append(temp.right)
        return  a
    def zhongxu(self, root):
        pass

    # 层序序列化 = bfs
    def bianli_bfs(self,root):
        route =queue.Queue()
        route.put(root)
        s = []
        while not route.empty():
            temp=route.get()
            if temp and temp!= 'None':
                s+=[str(temp.data)]
                route.put(temp.left)
                route.put(temp.right)
            else:
                s+=['None']
        return ','.join(s)


    #前序序列化dfs
    def bianli_dfs(self,root):
        if root == 'None':
            return
        s = []
        s+=[str(root.data)]+[str(self.bianli_dfs(root.left))]+[str(self.bianli_dfs(root.right))]
        return ','.join(s)
    def findDuplicateSubtrees(self, root):
        if root == None:
            return '#'
        s = ''
        s+=(str(root.val)+','+str(self.findDuplicateSubtrees(root.left))+','+str(self.findDuplicateSubtrees(root.right)))
        return s
#%%
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val =val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)


def serialize(root):
    route = queue.Queue()
    route.put(root)
    s = []
    while not route.empty():
        temp = route.get()
        if temp:
            s += [str(temp.val)]
            route.put(temp.left)
            route.put(temp.right)
        else:
            s += ['n']
    return ' '.join(s)


def deserialize(data):
    tree = data
    # print(tree)
    if tree[0] == 'null':
        return None
    queue = []
    root = TreeNode(int(tree[0]))
    queue.append(root)
    i = 1
    while queue:
        cur = queue.pop(0)
        if cur == None:
            continue
        cur.left = TreeNode(int(tree[i])) if tree[i] != "null" else None
        cur.right = TreeNode(int(tree[i + 1])) if tree[i + 1] != "null" else None
        i += 2
        queue.append(cur.left)
        queue.append(cur.right)
    return root
huaweicode = [1,2,3,4,'null',2,4,'null','null','null','null',4,'null','null','null']
# huaweicode =[1,2,3,4,5,6,7]
# root = deserialize(huaweicode)
# print(root.right.right.left)
# print(root.right.left.left)
# print(serialize(root))
#%%
huaweicode = [1,2,3,4,'#',2,4,'#','#','#','#',4,'#','#','#']
strcode = '1,2,3,None,None,4,None,None,5,None,None'
temp = Solution()
# root = temp.buile_huawei(huaweicode,0)
# strtemp =temp.bianli_dfs(root).split(',')
# print(strtemp)
# # print(temp.build_dfs(strtemp))
# root2 = temp.build_dfs(strtemp)
# print(root2.right.left.left.data)
# print(temp.bianli_bfs(root))
root = temp.build_bfs(huaweicode)
print(temp.bianli_bfs(root))
print(temp.bianli_dfs(root))
