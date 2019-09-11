if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort();
    for i in reversed(arr):
        if i != arr[n-1]:
            print(i)
            break