#include "misc.h"


void Assert(int assertion, char* error) {
  if(!assertion) {
    printf("Assertion Failed: %s\n",error);
    exit(-1);
  }
}





void * SafeMalloc(size_t size) {
  void * result;

  if ( (result = malloc(size)) ) {
    return(result);
  } else {
    printf("memory overflow: malloc failed in SafeMalloc.");
    printf("  Exiting Program.\n");
    exit(-1);
    return(0);
  }
}



void NullFunction(void * junk) { ; }
