#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

main() {

  double el = 0.0;
  int day = 1;
  
  FILE *myfile = fopen("solar.txt", "r");
  FILE *newfile = fopen("solar-new.txt", "w");

  while(1) {
    if (fscanf(myfile, "%lf", &el) == EOF)
      break;

    fprintf(newfile, "%lf,%d\n", el, day);
    day += 2;
  }
  
  fclose(myfile);
  fclose(newfile);

  return 0;
}
