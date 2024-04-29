# 不定长滑动窗口

## 最长上升/下降子数组

n = int(input())
w = list(map(int, input().split()))
res = 0
l, r = 0, 0
while l<n:
    r = l
    while r+1<n and w[r]<w[r+1]:
        r += 1
    res = max(res, r-l+1)
    l = r+1

print(res)

## 最大值/最大长度

def query(nums):
    n = len(nums)
    l, r = 0, 0
    res = 0
    while r<n:
        cur = 0 # 维护变量
        while not check():
            l += 1
        res = max(res, cur)
        r += 1
    return res

def check():
    return

## 最小值/最小长度

def query(nums):
    n = len(nums)
    l, r = 0, 0
    res = float('inf')
    while r<n:
        cur = 0 # 维护变量
        while check():
            res = min(res,cur)
            l += 1
        r += 1
    return res

def check():
    return

## 方案数

def query(nums):
    n = len(nums)
    l, r = 0, 0
    res = 0
    while r<n:
        cur = 0
        while not check():
            r += 1
        res = max(res, cur)
        l += 1
    return res

def check():
    return