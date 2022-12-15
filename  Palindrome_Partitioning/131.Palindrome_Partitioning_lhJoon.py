class Solution:
    def partition(self, s):
        if not s:
            return []

        output = []
        self.findPartition(s, output, [])

        return output

    def findPartition(self, s, output, temp):
        if not s:
            output.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                temp.append(s[:i])
                self.findPartition(s[i:], output, temp)
                temp.pop()

    def isPalindrome(self, string):
        return string == string[::-1]