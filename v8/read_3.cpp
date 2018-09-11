#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

main() {

  double rek, dek;
  int n = 1;

  double d = 0.7893/12.;
  double r = 2.0476/12.;
  
  FILE *myfile = fopen("p-e-new.txt", "r");
  FILE *newfile = fopen("p-e-next.txt", "w");

  while(1) {
    if (fscanf(myfile, "%lf,%lf", &rek, &dek) == EOF)
      break;

    fprintf(newfile, "%lf,%f,%d\n", 15 * rek - n * r, dek + n * d, n);
    n += 1;
  
  }
  
  fclose(myfile);
  fclose(newfile);

  return 0;
}
