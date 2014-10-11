
/****************************************************************************

                                                        Valeriy Sosnovskiy
                                                        CS12, Fall14
                                                        10/9/14
                                                        Login:cs12xoq
                                Assignment One

File Name:      hw1.c
Description:    This program tests functions to display output strings and 
                numbers. 
****************************************************************************/
#include <stdio.h>

#define COUNT 8     /* number of hex digits to display */
#define DECIMAL 10  /* to indicate base 10 */
#define HEX 16      /* to indicate base 16 */
#define BUFFSIZE 20   /* to indicate the buffer size*/
#define hexCounter 0  /*counter for the number of hex digits*/
/* array used for ASCII conversion */
const char digits[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int writeline (const char * message, FILE * stream);
void decout (unsigned int number, FILE * stream);
void baseout (int number, int base, FILE * stream);
/*--------------------------------------------------------------------------
Function Name:         List the function name.
Purpose:               Say why the function exists in a sentence or two.
Description:           Describe the underlying algorithm of how the function
                       is implemented in a few sentences.
Input:                 A list of the parameters with brief explanation of each.
Result:                A list of possible outcomes when the function is called.
                       Describe return value.
--------------------------------------------------------------------------*/
void baseout (int number, int base, FILE * stream) {
        /*for iteration purposes*/
        char arrayMain[ BUFFSIZE ];    /*array takes in input ints*/
        char arrayFinal[BUFFSIZE];     /*final array with ASCII #'s*/
        int counter = 0;               /*counter for integer characters*/
        int temp= 0;                   /*is the remainder of the mod*/
        int countTwo = 0;              /*is the counter for array*/
        int i = 0;
        int j = 0;

        /*
         * The while loop to take in the input integer and break it down to 
         * Single integers using %(mod) and /(div) 
         */


        if(number == 0){
           fputc('0', stdout);
        }
                                                           
while(number != 0){
           if(counter < BUFFSIZE){
           temp =  number%base;
           number = number/base;
           arrayMain[counter]=digits[temp];
           counter ++;
           }

           else{

           }
       }

         if(base == HEX){

            for (i = 0; i < COUNT; i++){
                arrayFinal[i]=arrayFinal['0'];


            }
         }


         }

         else{



         }


         while(counter > 0){

         arrayFinal[counter] = arrayMain[countTwo];

         counter--;
         countTwo ++;

}

        for (j=0; j  < countTwo; j++){
          fputc(arrayFinal[j], stdout);
        }


}


/*--------------------------------------------------------------------------
Function Name:         List the function name.
Purpose:               Say why the function exists in a sentence or two.
Description:           Describe the underlying algorithm of how the function
                       is implemented in a few sentences.
Input:                 A list of the parameters with brief explanation of each.
Result:                A list of possible outcomes when the function is called.
                       Describe return value.
--------------------------------------------------------------------------*/
void decout (unsigned int number, FILE * stream) {
     //pass the number input, 10, and stream to baseout
     baseout(number, DECIMAL, stream);
}


/*--------------------------------------------------------------------------
Function Name:         hexout
Purpose:               Prints a number in base 16 to the parameter FILE stream
Description:           Goal is achieved via delegating to the baseout function
Input:                 number:  the number to display
                       stream:  where to display, likely stdout or stderr
Result:                Number in base 16 is displayed.
                       No return value.
--------------------------------------------------------------------------*/
void hexout (unsigned int number, FILE * stream) {

    /* Output "0x" for hexidecimal. */
    writeline ("0x", stream);
    baseout (number, HEX, stream);
}


/*--------------------------------------------------------------------------
Function Name:         List the function name.
Purpose:               Say why the function exists in a sentence or two.
Description:           Describe the underlying algorithm of how the function
                       is implemented in a few sentences.
Input:                 A list of the parameters with brief explanation of each.
Result:                A list of possible outcomes when the function is called.
                       Describe return value.
--------------------------------------------------------------------------*/
void newline (FILE * stream) {
fputc('\n',stdout);
}


/*--------------------------------------------------------------------------
Function Name:         List the function name.
Purpose:               Say why the function exists in a sentence or two.
Description:           Describe the underlying algorithm of how the function
                       is implemented in a few sentences.
Input:                 A list of the parameters with brief explanation of each.
Result:                A list of possible outcomes when the function is called.
                       Describe return value.
--------------------------------------------------------------------------*/
int writeline (const char * message, FILE * stream) {
    int index = 0;

    while(message[index] != '\0'){
        fputc(message[index], stdout);

        index++;
    }
   return(index);
}


int main (int argc, char *const* argv) {
    writeline ("Hello World", stdout);
    fprintf (stderr, "Hola Mundo\n");
    newline(stdout);
    decout (123, stdout);
    newline(stdout);
    decout (0, stdout);
    newline(stdout);
    hexout (0xFEEDDAD, stdout);
    newline(stdout);
    return 0;
}
             