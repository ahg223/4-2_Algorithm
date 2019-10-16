//
//  main.c
//  BCD_C
//
//  Created by Hyung Geun Ahn on 16/10/2018.
//  Copyright © 2018 None. All rights reserved.
//
#include <stdio.h>
#include <stdlib.h>    // For dynamic allocation

void BCD(char b){
    int a=b-'0';
    int tmp[4]={0,0,0,0};
    
    if(a-8>=0){
        tmp[0]=1;
        a-=8;
    }
    if(a-4>=0){
        tmp[1]=1;
        a-=4;
    }
    if(a-2>=0){
        tmp[2]=1;
        a-=2;
    }
    if(a-1>=0){
        tmp[3]=1;
        a-=1;
    }
    for(int i=0;i<4;i++)
    printf("%d", tmp[i]);
    
    printf(" ");
}


int main()
{
    int length;
    printf("숫자의 길이는? ");
    scanf("%d", &length);
    
    char* s1=(char*)malloc(sizeof(char)*length);
    memset(s1,0,sizeof(char)*length);
    
    printf("BCD로 출력할 십진법 수를 입력하시오 ");
    scanf("%s", s1);
    for(int i=0;i<length;i++){
        if(s1[i]!=NULL && s1[i]>47 && s1[i]<58) BCD(s1[i]);
        else {
            printf("Error");
            break;
        }
    }
    
    return 0;
}
