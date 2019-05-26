# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
for _ in range(num):
    a = int(input())
    set1 = set(list(map(int, input().split())))
    b = int(input())
    set2 = set(list(map(int, input().split())))
    print(set1.issubset(set2))
