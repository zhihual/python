#include "stdio.h"

void crash()
{
   char* p = NULL;

   *p = 2;
}


void main()
{
  char a;
  printf("this is crash test elf\n");

  a = getchar();

  printf("get %c\n", a);

  crash();
}

