T = int(input())
for tc in range(1, T + 1):
    def pascal_triangle(n):
        dp = [[1] * (i + 1) for i in range(n)]

        for i in range(2, n):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp

    # 테스트
    n = int(input())
    triangle = pascal_triangle(n)
    print(f'#{tc}')
    for row in triangle:
        print(*row)
