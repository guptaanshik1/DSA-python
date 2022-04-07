class Solution:
    def __knight(self, board, row, col, numKnights):
        if numKnights == 0:
            self.__display(board)
            print()
            return 1

        count = 0
        if row == len(board) - 1 and col == len(board):
            return count
        
        # check if all the columns of the row are done
        if col == len(board):
            self.__knight(board, row + 1, 0, numKnights)# then move to the next row
            return count

        if self.__isSafe(board, row, col):# if knight is safe to place
            board[row][col] = True# set True for that
            count += self.__knight(board, row, col + 1, numKnights - 1)# check in next column and decrease number of knights
            board[row][col] = False

        self.__knight(board, row, col + 1, numKnights)

        return count

    def __isValid(self, board, row, col):# just for the bound check
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
        return self.__knight(board, 0, 0, n)

sol = Solution()

print(sol.solveNKnights(4))