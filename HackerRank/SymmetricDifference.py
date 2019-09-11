# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
set1 = set(list(map(int, input().split())))
b = int(input())
set2 = set(list(map(int, input().split())))

for x in sorted(set1 ^ set2):
    print(x)
