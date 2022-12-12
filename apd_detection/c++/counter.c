#include <stdio.h>
#include <sys\timeb.h> 

int main()     
{ 
    struct timeb start, end;
    int diff;
    int i = 0;
    ftime(&start);

    // while(i++ < 999) {
    //     /* do something which takes some time */
    //     printf(".");    
    // }

    ftime(&end);
    diff = (int) (1000.0 * (end.time - start.time)
        + (end.millitm - start.millitm));

    while (1) {
        ftime(&start);
        printf("ms: %s", start.time);
    }
    return 0;
}