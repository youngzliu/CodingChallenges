

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    word = ""
    current = root
    for num in s:
        if (num == "0"):
            current = current.left
            if(current.data != "\0"):
                word += current.data
                current = root
        else:
            current = current.right
            if(current.data != "\0"):
                word += current.data
                current = root
    print(word)
        


