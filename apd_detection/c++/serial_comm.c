#include <Windows.h>
#include <stdio.h>


void main(void){

    printf("Hello!\n");

    DWORD dwCommEvent;
    DWORD dwRead;
    DWORD lpEvtMask;
    char  chRead;
    char  ComPortName[] = "\\\\.\\COM8";  // Name of the Serial port(May Change) to be opened,
    int i=0;

    HANDLE hComm;
    hComm = CreateFile( ComPortName,  
                        GENERIC_READ | GENERIC_WRITE, 
                        0, 
                        0, 
                        OPEN_EXISTING,
                        0,
                        0);
    if (hComm == INVALID_HANDLE_VALUE)
       printf("Error opening port.\n");
   
    //////////////////////////////////////////////////////   
    DCB dcb;

    FillMemory(&dcb, sizeof(dcb), 0);
    if (!GetCommState(hComm, &dcb))     // get current DCB
       printf("Error GetCommState.\n");

    // Update DCB rate.
    dcb.BaudRate = CBR_9600 ;
    dcb.ByteSize = 8;             // Setting ByteSize = 8
    dcb.StopBits = ONESTOPBIT;    // Setting StopBits = 1
    dcb.Parity = NOPARITY;        // Setting Parity = None 
    dcb.DCBlength = sizeof(dcb);
     // Set new state.
    if (!SetCommState(hComm, &dcb))
        printf("Error SetCommState.\n");
        // Error in SetCommState. Possibly a problem with the communications 
         // port handle or a problem with the DCB structure itself.


    /////////////////////////////////////////////////////////////////////
    COMMTIMEOUTS timeouts;

    timeouts.ReadIntervalTimeout = MAXDWORD; 
    timeouts.ReadTotalTimeoutMultiplier = 0;
    timeouts.ReadTotalTimeoutConstant = 0;
    timeouts.WriteTotalTimeoutMultiplier = 0;
    timeouts.WriteTotalTimeoutConstant = 0;

    if (!SetCommTimeouts(hComm, &timeouts))
       printf("Error timeouts.\n");

    if(!PurgeComm(hComm,PURGE_RXCLEAR | PURGE_TXCLEAR | PURGE_RXABORT | PURGE_TXABORT))
        printf("Error PurgeComm.\n");
    ////////////////////////////////////////
    for ( ; ; ) {
        if (!SetCommMask(hComm, 0))
            printf("Error CommMask.\n");
    
        if (!SetCommMask(hComm, EV_RXCHAR))
            printf("Error CommMask.\n");
        
        printf("Waiting for characters.. \n\n");
    
       if (WaitCommEvent(hComm, &dwCommEvent, NULL)) {
           do {
                if (ReadFile(hComm, &chRead, 1, &dwRead, NULL)){
                    if(dwRead!=0)
                        printf("Character Received: %c\n",chRead);
                }
                else{
                    printf("ErrorReadFile.\n");
                    break;
                }
            }while (dwRead);
       }
       else{
            printf("Error WaitCommEvent.\n");
             break;
        }
        printf("=========================\n");
    }
}