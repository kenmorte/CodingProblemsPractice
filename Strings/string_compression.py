# https://leetcode.com/problems/string-compression/description/

class Solution(object):
    def compress(self, arr):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        # O(1) space
        if not arr: return 0
        i, j, k, n = 0, 0, 0, len(arr)
        while i < n:
            while j < n and arr[i] == arr[j]: j += 1
            cnt = j-i
            strCnt = str(cnt)
            m = len(strCnt)
            arr[k] = arr[i]
            if cnt > 1:
                arr[k+1:k+1+m] = strCnt
                k = k + m + 1
            else: k += 1
            i = j
        return k
            
        
        # O(n) space
        # if not chars: return 0
        # res = []
        # curr = chars[0]
        # cnt = 1
        # for c in chars[1:]:
        #     if c == curr: cnt += 1
        #     else:
        #         res.append(curr)
        #         if cnt > 1: res += [digit for digit in str(cnt)]
        #         curr = c
        #         cnt = 1
        # res.append(curr)
        # if cnt > 1: res += [c for c in str(cnt)]
        # chars[:len(res)] = res
        # return len(res)
