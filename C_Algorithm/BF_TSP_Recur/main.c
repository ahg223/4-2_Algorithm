//
//  main.c
//  BF_TSP_Recur
//
//  Created by Hyung Geun Ahn on 2018. 9. 25..
//  Copyright © 2018년 None. All rights reserved.
//
//  갈 수 없는 길은 0으로 표시 (1번 도시에서 1번으로 가는 것은 불가능해 0)
//


#include <stdio.h>
#include <stdbool.h>

#define INT_MAX 2147483647

int MAX;            //도시 수
int TSP[11][11];    //도시 간 거리 저장
int Min = INT_MAX;  //최소값 저장 변수
bool visited[11];   //이미 들렸는지 확인


int min(int x, int y){ // 최소값 반환 함수
    if (x>y) return y;
    else return x;
}

/*
 next : 방문한 도시
 costSum : 현재까지 비용 합
 count : 재귀 횟수 == 방문한 도시 수
*/

void tsp(int next, int total, int Recur){   // 최소 거리 구하는 함수
    if(Recur == MAX) {                      // 모든 노드를 방문 == 도시 수 만큼 재귀
        if(TSP[next][1] != 0)                   // 시작점으로 돌아 갈 수 있는 길이 있으면
        Min = min(Min, total+TSP[next][1]);
        return;
    }
    
    visited[next] = true;                   // 해당 도시에 도착함을 표시
    for(int i=1;i<=MAX;i++){                // 다음 도시 탐색
        if(!visited[i] && TSP[next][i] != 0){   // 다음 도시를 들른 적 없고 길이 있다면
            tsp(i, total+TSP[next][i], Recur+1);// 해당 거리를 total에 더한 뒤 재귀
        }
    }
    visited[next] = false;                  // 재귀가 끝나기 전에 이전 상태로 복귀
}

int main()
{
    scanf("%d", &MAX);
    for(int i=1;i<=MAX;i++)
        for(int j=1;j<=MAX;j++)
            scanf("%d",&TSP[i][j]);
    
    tsp(1,0,1);
    printf("%d\n", Min);
    return 0;
    
}
