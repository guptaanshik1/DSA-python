class Solution:
    def __knight(self, board, row):
        if row == len(board):
            self.__display(board)
            print()
            return 1

        count = 0
        for col in range(len(board)):
            if self.__isSafe(board, row, col):
                board[row][col] = True
                count += self.__knight(board, row + 1)
                board[row][col] = False
        return count

    def __isValid(self, board, row, col):
        if row >= 0 and row < len(board) and col >= 0 and col < len(board):
            return True
        
        return False

    def __isSafe(self, board, row, col):
        if self.__isValid(board, row - 2, col - 1):
            if board[row - 2][col - 1]:
                return False

        if self.__isValid(board, row - 1, col - 2):
            if board[row - 1][col - 2]:
                return False

        if self.__isValid(board, row - 2, col + 1):
            if board[row - 2][col + 1]:
                return False

        if self.__isValid(board, row - 1, col + 2):
            if board[row - 1][col + 2]:
                return False

        return True

    def __display(self, board):
        for row in board:
            for el in row:
                if el:
                    print("K", end=" ")
                else:
                    print(".", end=" ")
            print()

    def solveNKnights(self, n):
        board = [[None for j in range(n)] for i in range(n)]
        return self.__knight(board, 0)

sol = Solution()

print(sol.solveNKnights(4))