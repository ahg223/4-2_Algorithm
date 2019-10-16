Flag,Crash=0,0
    
def simulation(atoms,Map,locate):
    global Flag
    global Crash
    
    for _ in range(len(atoms)):
        atom=atoms[_]
        if atom[0]==-1: continue
        
        if atom[0]==0: locate[_][0]+=1
        elif atom[0]==1: locate[_][0]-=1
        elif atom[0]==2: locate[_][1]-=1
        else: locate[_][1]+=1

    Locate=[]
    while True:
        for i in range(len(atoms)):
            if 2001>locate[_][0]>-1 and 2001>locate[_][1]>-1:
                temp=locate.pop(0)
                if temp in Locate+locate:
                    locate.
                Locate.append(locate.pop(0))
            else:
                atoms.pop(i)
                locate.pop(i)
                break
    
               
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    locate=[[] for i in range(N)]
    atoms=[]
    for _ in range(N):
        i,j,dir,K=map(int,input().split())
        atoms.append([dir,K])
        locate.append([j,i])
    
    Crash,Flag=0,len(atoms)
    while Flag>1: simulation(atoms,Map,locate)
    
    print("#{} {}".format(test_case,Crash))
    
'''
def moving(atoms,Map,Crash):
    for _ in range(len(atoms)):
        atom=atoms[_]
        Map[atom[0]][atom[1]]-=1
        if atom[2]==0: atom[0]+=1
        elif atom[2]==1: atom[0]-=1
        elif atom[2]==2: atom[1]-=1
        else: atom[1]+=1
        
        if 2001>atom[0]>-1 and 2001>atom[1]>-1: 
            Map[atom[0]][atom[1]]+=1
            if Map[atom[0]][atom[1]]>1:
                atom[0],atom[1],atom[2],atom[3]=-1,-1,-1,-1
                Crash+=atom[3]
                if Map[atom[0]][atom[1]]==2:
                    for i in range(atoms):
                        if atoms[i][0]==atom[0] and atoms[i][1]==atom[1]:
                            atoms[i][0],atoms[i][1],atoms[i][2],atoms[i][3]=-1,-1,-1,-1
                            break
                
                
        else: atom[0],atom[1],atom[2],atom[3]=-1,-1,-1,-1
    
    
def simulation(atoms,Map,Crash):
    #print(atoms)
    moving(atoms,Map,Crash)
    for i in range(len(atoms)-1,-1,-1):
        if atoms[i][0]==-1: atoms.pop(i)
    
    for i in range(2001):
        for j in range(2001):
            if Map[i][j]>1:Map[i][j]=0
               
T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    Map=[[0 for i in range(2001)] for j in range(2001)]
    
    atoms=[]
    for _ in range(N):
        i,j,dir,K=map(int,input().split())
        i+=1000
        j+=1000
        atoms.append([j,i,dir,K])
        Map[j][i]=1
        print(Map[j][i])
    
    Crash=0
    while atoms!=[]:
        simulation(atoms,Map,Crash)
    
    print("#{} {}".format(test_case,Crash))
'''
