s1 = []
s2 = []

def enqueue(x):
    s1.push(x)

def dequeue(x):

    if len(s2) == 0:
        if len(s1) == 0:
            print("end")
        else:
            while(len(s1)> 0):
                temp = s1.pop()
                s2.push(temp)
    
    return s2.pop()

