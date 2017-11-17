# https://leetcode.com/problems/find-duplicate-file-in-system/description/

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        if not paths: return []
        dup_files = dict()
        for path in paths:
            directory = path.split(' ')[0]
            
            filesAndContents = path.split(' ')[1:]
            for fileAndContent in filesAndContents:
                fileAndContentSplit = fileAndContent.split('(')
                filename = fileAndContentSplit[0]
                content = fileAndContentSplit[1][:len(fileAndContentSplit[1]) - 1]
                
                if content not in dup_files:
                    dup_files[content] = set()
                dup_files[content].add(directory + '/' + filename)
                
        result = []
        for content in dup_files:
            if len(dup_files[content]) > 1:
                result.append(list(dup_files[content]))
        return result                    
