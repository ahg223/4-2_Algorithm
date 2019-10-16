//
//  main.c
//  You_F_byC
//
//  Created by Hyung Geun Ahn on 01/11/2018.
//  Copyright © 2018 None. All rights reserved.
//
//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )
# define NUM 100.0

char *Grade[101][6]={0,};

void GradeInit(void){
    char *buffer;
    long size;
    long count;
    int i=0,j=0,r=-1;
    
    char *buff[1200]={0,};
    char *token=NULL;
    char str1[]=",\n";
    
    FILE *fp = fopen("Data.csv", "rb");
//    if (fp==NULL) printf("1234");
    fseek(fp, 0L, SEEK_END);
    size = ftell(fp);
    
    buffer = malloc(size + 1);
    memset(buffer, 0, size + 1);
    
    fseek(fp, 0, SEEK_SET);
    count = fread(buffer, size, 1, fp);
    
    token=strtok(buffer,str1);
    
    while(token!=NULL){
        buff[i++]=token;
        token=strtok(NULL,str1);
    }
    
    i=0;
    do{
        j=0;
        r++;
        do{
            Grade[i][j++]=buff[r++];
        }while(606>r && strcmp(buff[r],"\r"));
        i++;
    }while(606>r);
    fclose(fp);
    free(buffer);
}

void selection_sort(char* name[], int list[], int n){
    int i, j, least, temp;
    char* temp2;
    
    for(i=1; i<n-1; i++){
        least = i;
        
        for(j=i+1; j<n; j++){
            if(list[j]<list[least])
                least = j;
        }
        
        if(i != least){
            SWAP(list[i], list[least], temp);
            SWAP(name[i], name[least], temp2);
        }
    }
}


int main()
{
    char* Answer[101]={0,};
    int Score[101]={0,};
    char* SCORE[101]={0,};
    GradeInit();
    
    for(int i=1;101>i;i++){
        while (1){
            Answer[i]=Grade[i][0];
            if(atoi(Grade[i][1])>10) Score[i]+=(14-atoi(Grade[i][1]))*(-5);
            else {Score[i]=-20000; break;}
            
            if(atoi(Grade[i][2])>19) Score[i]+=(22-atoi(Grade[i][2]))*(-5);
            else {Score[i]=-20000; break;}

            if(atoi(Grade[i][3])>59) Score[i]+=atoi(Grade[i][3]);
            else {Score[i]=-20000; break;}

            if(atoi(Grade[i][4])>79) Score[i]+=atoi(Grade[i][4]);
            else {Score[i]=-20000; break;}

            if(atoi(Grade[i][5])>59) Score[i]+=atoi(Grade[i][5]);
            else {Score[i]=-20000; break;}
            break;

        }
    }
   
    for(int i=1;i<101;i++){
        printf("%s ",Answer[i]);
        printf("%d ", Score[i]);
        printf("\n");
        
    }

    selection_sort(Answer,Score,101);
    
    for(int i=1;i<101;i++){
        if (Score[i]==-20000) SCORE[i]="F";
        else if ((NUM)*(0.1)>=i) SCORE[i]="C+";
        else if ((NUM)*(0.5)>=i) SCORE[i]="B+";
        else SCORE[i]="A+";
        
        printf("%s ",Answer[i]);
        printf("%s ", SCORE[i]);
        printf("\n");
        
    }
    return 0;
}
