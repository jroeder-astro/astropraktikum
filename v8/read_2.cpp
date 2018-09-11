#include<iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

main() {

  double dm, yr, h, m, s, de, am, as, tm1, tm2, el, eb;
  char date[11];

  FILE *myfile = fopen("solar.txt", "r");
  FILE *newfile = fopen("solar-new.txt", "w");

  while(1) {
    if (fscanf(myfile, "%s    %lf  %lf   %lf    %lf    %lf    %lf    %lf    %lf   %lf   %lf", 
               date, &tm1, &tm2, &h, &m, &s, &de, &am, &as, &el, &eb) == EOF)
      break;
    printf("%s    %lf  %lf   %lf    %lf    %lf    %lf    %lf    %lf   %lf   %lf\n", 
               date, tm1, tm2, h, m, s, de, am, as, el, eb); 


//    fprintf(newfile, "%lf,%lf\n", h+m/60+s/3600, de+am/60+as/3600);
 

//    printf("%lf,%lf\n", h+m/60+s/3600, de+am/60+as/3600);
  }
  
  fclose(myfile);
  fclose(newfile);

  return 0;
}
