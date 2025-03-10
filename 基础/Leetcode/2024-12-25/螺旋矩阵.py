# -*- coding: utf-8 -*-
# @Time    : 25 12月 2024 8:05 下午
# @Author  : codervibe
# @File    : 螺旋矩阵.py
# @Project : pythonBasics
"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1

        while left <= right and top <= bottom:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # Traverse from right to left along the bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        ans = [matrix[0][0]]
        matrix[0][0] = '0'
        a = [0, 0]
        b = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        c = [0, 0]
        flag = 0
        while 1:
            c[0] = a[0] + b[k][0]
            c[1] = a[1] + b[k][1]
            count = 0
            while c[0] < 0 or c[0] >= m or c[1] < 0 or c[1] >= n or matrix[c[0]][c[1]] == '0':
                k = (k + 1) % 4
                c[0] = a[0] + b[k][0]
                c[1] = a[1] + b[k][1]
                count += 1
                if count == 2:
                    flag = 1
                    break
            if flag == 1:
                break
            a[0] = c[0]
            a[1] = c[1]
            ans.append(matrix[a[0]][a[1]])
            matrix[a[0]][a[1]] = '0'
        return ans


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
