//
//  main.c
//  AllergyC
//
//  Created by Hyung Geun Ahn on 2018. 10. 7..
//  Copyright © 2018년 None. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *Menu[122][13]={0,};

void MenuInit(void){
    char *buffer;
    int size;
    int count;
    int i=0,j=0,r=-1;
    
    char *buff[1200]={0,};
    char *token=NULL;
    char str1[]=",\n";
    
    FILE *fp = fopen("데이터_셋완성_.csv", "rb");
    
    fseek(fp, 0, SEEK_END);
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
            Menu[i][j++]=buff[r++];
        }while(668>r && strcmp(buff[r],"\r"));
        i++;
    }while(668>r);
    fclose(fp);
    free(buffer);
}

int main()
{
    int allergy[14]={0,};
    int day=0;
    int i=0,j=0,t=0,flag=0;
    
    MenuInit();
    
    printf("다음 중 해당하는 알러지가 있다면 정수를 입력하세요\n 1. 난류 \n 2. 우유 \n 3. 메밀 \n 4. 땅콩 \n 5. 대두 \n 6. 밀 \n 7. 고등어 \n 8. 게 \n 9. 새우 \n 10. 돼지고기 \n 11. 복숭아 \n 12. 토마토 \n 13. 아황산염 \n 종료를 원하시면 0을 입력해주세요.\n");
    do{
        scanf("%d",&j);
        if (j==0) break;
        else if (j>0 && 14>j) allergy[i++]=j;
        else printf("잘못된 입력입니다 \n");
    }while(1);
    
    printf("몇 일의 식단이 궁금하신가요?: ");
    scanf("%d",&day);
    printf("%d 일의 알러지 맞춤 식단\n",day);
    Menu[0][0]="1";
    
    i=0;j=0;
    while (1){
        if (day == atoi(Menu[i][0])){
            for(j=2;13>j;j++){
                if(Menu[i][j]){
                    for(t=0;allergy[t]!=0;t++){
                        if (allergy[t]==atoi(Menu[i][j])) flag++;
                    }
                }
            }
            if (flag==0) {
                printf("%s \n",Menu[i][1]);
            }
            flag=0;
        }
        if (i>117) break;
        i++;
    }
    
    return 0;
}
