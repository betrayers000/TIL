import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    a, b, c, d, = map(int, input().split())
    bin_ = "00"*a + "01"*b + "10"*c + "11"*d
    print(bin_)
