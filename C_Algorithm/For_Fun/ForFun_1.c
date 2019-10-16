//
//  main.c
//  Algorithm_for_Fun_1_C
//
//  Created by Hyung Geun Ahn on 12/11/2018.
//  Copyright © 2018 None. All rights reserved.
//

#include <stdio.h>

int Fun(int Num){
    
    if (Num==1) return 1;
    else if (Num==2) return 2;
    else if (Num==3) return 4;
    else return Fun(Num-1)+Fun(Num-2)+Fun(Num-3);
}

int main(int argc, const char * argv[]) {
    int Num;
    printf("Typing int you want to find: ");
    scanf("%d",&Num);
    
    if (Num<3) printf("Need more int than 3\n");
    else printf("%d \n",Fun(Num));
    
    return 0;
}
