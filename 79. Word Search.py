class Solution:
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        if not board or not board[0]: return False

        visited = set()
        self.res = False

        def isvalid(i, j, visited, board):
            return 0 <= i < len(board) and 0 <= j < len(board[0]) and (i, j) not in visited

        def dfs(board, curi, curj, index, word, visited):
            if index == len(word):
                self.res = True
                return
            if word[index] == board[curi][curj]:
                visited.add((curi, curj))


                for diff in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newi = curi + diff[0]
                    newj = curj + diff[1]
                    if isvalid(newi, newj, visited, board):

                        dfs(board, newi, newj, index + 1, word, visited)
                visited.remove((curi, curj))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, 0, word, visited)
        return self.res

sol = Solution()
sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],
"ABCCED")