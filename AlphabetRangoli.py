import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    for x in range(size):
        line = "-".join(alphabet[x:size])
        lines.append((line[::-1] + line[1:]).center(4*(n-1)+1, "-"))
    print("\n".join(lines[:0:-1] + lines))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)