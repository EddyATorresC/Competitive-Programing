test = int(input())

#For each test 
for n_test in range(0,test):
    n = int(input())
    
    visited = [0]*(n)
 
    count = 0
    idx = -1
 
    for i in range(0,n):
        
        num = 0
        v = input().split(' ')
 
        for idj in range(1, len(v)):
            current_prince = int(v[idj]) -1
 
            if (visited[current_prince] == 0):
                visited[current_prince] = 1
                break
        else:
            idx = i
    
    if idx == -1:
        print('OPTIMAL\n')
    else:
        print('IMPROVE\n')
        u = visited.index(0)
        print(str(idx + 1) + " " + str(u + 1) + "\n")
 
