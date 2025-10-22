def rotate_right(head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        stack = list(head)
        n=len(head)
        ans = [0] * (k)
        for i in range(k):
            value = stack.pop()
            ans[k-i-1] = value

        for i in range(len(stack)):
            ans.append(stack[i])

        return ans
def rotate_right2(head, k):
     return head[-k:] + head[:-k]

b = [1,2,3,4,5]
print(rotate_right(b,2))
print(rotate_right2(b,2))
