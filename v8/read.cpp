#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

main() {

  double dm, yr, h, m, s, de, am, as;

  FILE *myfile = fopen("pluto-ephemeride.txt", "r");
  FILE *newfile = fopen("p-e-new.txt", "w");

  while(1) {
    if (fscanf(myfile, "%lf    %lf    %lf    %lf    %lf    %lf    %lf    %lf", 
               &dm, &yr, &h, &m, &s, &de, &am, &as) == EOF)
      break;

//    printf("%lf    %lf    %lf    %lf    %lf    %lf    %lf    %lf\n", 
//               dm, yr, h, m, s, de, am, as);
    fprintf(newfile, "%lf,%lf\n", h+m/60+s/3600, de+am/60+as/3600);
 

//    fprintf(newfile, "%lf,%lf\n", h+m/60+s/3600, de+am/60+as/3600);
  }
  
  fclose(myfile);
  fclose(newfile);

  return 0;
}
