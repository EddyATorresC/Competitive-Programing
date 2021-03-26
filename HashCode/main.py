import numpy as np
import random 
class Street:
    def __init__(self,B,E,street_name, L):
        self.B = B
        self.E = E
        self.street_name = street_name
        self.L = L

class Vehicle: 
    def __init__(self,P,streets):
        self.P = P
        self.streets = streets
def rand_bin_matrix(K, N):
    arr = np.zeros((N,N))
    arr[0,:K]  = 1
    np.random.shuffle(arr)
    return arr

def rand_matrix(K, N):
    arr = np.zeros((N,N))
    arr[:K,:K]  = random.randint(1,6)
    np.random.shuffle(arr)
    return arr

def score(adjency, total_time, streets_to_cover):
    n,m = adjency.shape
    to_turn_on = rand_bin_matrix(random.randint(1,n),int(n))
    print(int(to_turn_on[0,0]))
    seconds = rand_matrix(random.randint(1,n),int(n))

    f = open("output.txt", "w")
    f.write(str(random.randint(1,n)) + '\n')

    for i, row in enumerate(to_turn_on):
        for j, val in enumerate(row):
            if int(to_turn_on[i,j]) == 1:
                f.write(str(i) + '\n')
                for k, _val in enumerate(row):
                    if(int(to_turn_on[i,k]) == 1):
                        for street in streets_to_cover:
                            if street.B == i and street.E == k:
                                f.write(street.street_name + ' ' + str(str(int(seconds[i,k])))  + '\n')
    
    f.close()

file1 = open('b.txt', 'r')
Lines = file1.readlines()
 
count = 1
# Strips the newline character
D=1
I=2
S=2
V=1
F=1

streets = []
vehicles = []


for line in Lines:
    if count == 1:
      splited = line.replace("\n", "").split()
      D=int(splited[0])
      I=int(splited[1])
      S=int(splited[2])
      V=int(splited[3])
      F=int(splited[4])  

      adjency = np.zeros((I,I))
    elif count <= S + 1 and count > 1:
        splited = line.replace("\n", "").split()
        streets.append(Street(int(splited[0]),int(splited[1]),splited[2],int(splited[3])))

        adjency[int(splited[0]),int(splited[1])] = 1
    else:
        splited = line.replace("\n", "").split()
        path = []
        i = 1
        while i < len(splited):
            flag = True
            j = 0

            while j<len(streets) and flag:
                if streets[i].street_name == splited[i]:
                    path.append(streets[i])
                    flag = False
                j+=1

            i += 1

        vehicles.append(Vehicle(int(splited[0]), path))

    count += 1

for s in streets:
    print(s.street_name)
    print(str(s.B) + "," + str(s.E))

for v in vehicles:
    print(v.P)
    for st in v.streets:
        print(st) 

print(adjency)

score(adjency,6,streets)