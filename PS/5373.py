import sys
import copy
input = sys.stdin.readline
sys.setrecursionlimit(10000)
Cube={"U":[["w","w","w"],["w","w","w"],["w","w","w"]],
      "D":[["y","y","y"],["y","y","y"],["y","y","y"]],
      "F":[["r","r","r"],["r","r","r"],["r","r","r"]],
      "B":[["o","o","o"],["o","o","o"],["o","o","o"]],
      "L":[["g","g","g"],["g","g","g"],["g","g","g"]],
      "R":[["b","b","b"],["b","b","b"],["b","b","b"]]}
U=[[Cube["F"][0][0],Cube["F"][0][1],Cube["F"][0][2]], [Cube["R"][0][0],Cube["R"][0][1],Cube["R"][0][2]],
   [Cube["B"][0][0],Cube["B"][0][1],Cube["B"][0][2]], [Cube["L"][0][0],Cube["L"][0][1],Cube["L"][0][2]]]
D=[[Cube["F"][2][0],Cube["F"][2][1],Cube["F"][2][2]], [Cube["R"][2][0],Cube["R"][2][1],Cube["R"][2][2]],
   [Cube["B"][2][0],Cube["B"][2][1],Cube["B"][2][2]], [Cube["L"][2][0],Cube["L"][2][1],Cube["L"][2][2]]]
F=[[Cube["U"][2][0],Cube["U"][2][1],Cube["U"][2][2]], [Cube["R"][0][0],Cube["R"][0][1],Cube["R"][0][2]],
   [Cube["D"][2][0],Cube["D"][2][1],Cube["D"][2][2]], [Cube["L"][0][2],Cube["L"][1][2],Cube["L"][2][2]]] 
B=[[Cube["U"][0][0],Cube["U"][0][1],Cube["U"][0][2]], [Cube["R"][0][2],Cube["R"][0][1],Cube["R"][0][2]],
   [Cube["D"][2][0],Cube["D"][2][1],Cube["D"][2][2]], [Cube["L"][0][2],Cube["L"][1][2],Cube["L"][2][2]]] 

def rotate(cube,cmd):
    if cmd[1]=="+":
    else:
        

T=int(input())
for _ in range(T):
    cube=copy.deepcopy(Cube)
    N=int(input())
    cmds=list(input().split())
    for cmd in cmds:
        rotate(cube,cmd)
