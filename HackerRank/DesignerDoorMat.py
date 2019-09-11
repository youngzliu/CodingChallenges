# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    decoration = ".|."
    dimensions = input().split()
    rows = int(dimensions[0])
    columns = int(dimensions[1])
    for x in range(0, int(rows/2)):
        line = decoration + (decoration * x * 2)
        print(line.center(columns, "-"))
    print("WELCOME".center(columns, "-"))
    for x in range(int(rows/2), 0, -1):
        line = decoration + (decoration * (x-1) * 2)
        print(line.center(columns, "-"))