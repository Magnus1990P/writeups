Impossible Password
====
**FLAG:** HTB{40b949f92b86b18}

**PTS:**  30


### Details
 Are you able to cheat me and get the flag? 


### Steps
1. Find out what type of file it is. An ELF binary
2. Run the binary and I get prompted for input by an "\* "
3. Open binary in Ghidra and run analysis and decompilation on it.
4. Looking for strings in the code and I find an interesting string; "SuperSeKretKey" and go to the strings location.
5. Explore the code where this variable is referenced, and find a string compare after a "\*" is printed.  Which compares my input against the string in question.
```
004008fa e801fdffff  CALL  printf					//print "* "
004008ff 488b55f8    MOV   RDX=>s_SuperSeKretKey_00400a70,qword ptr	//read input
00400903 488d45e0    LEA   RAX=>local_28,[RBP + -0x20]			//Move text
00400907 4889d6      MOV   RSI=>s_SuperSeKretKey_00400a70,RDX		//move variable
0040090a 4889c7      MOV   RDI,RAX					//Move variable
0040090d e81efdffff  CALL  strcmp					//run strmcp
```
6. Run the program again, and input the string, and I'm prompted form input with "\*\*".
7. Go back to the code, find the second point of user input.  Followed by a function, whose output is compared against my input.
The function generates an random output based on a seed using three variables which looks to be static, but turned out to be based on current timestamp and I couldn't break the logic.
```
  tVar2 = time((time_t *)0x0);				//Grab current time
  DAT_00601074 = DAT_00601074 + 1;			//Static value
  srand(DAT_00601074 + (int)tVar2 * param_1);		//Sed PRNG
  pvVar3 = malloc((long)(param_1 + 1));			//Allocate the string
  if (pvVar3 != (void *)0x0) {				//if the provided param is not 0
    for (local_c=0;local_c < param_1; local_c++) {	//For loop 0-20
      iVar1 = rand();					//Generate random value
      *(char *)((long)local_c + (long)pvVar3) = (char)(iVar1 % 0x5e) + '!';//Convert to char
    }
    *(undefined *)((long)pvVar3 + (long)param_1) = 0;	//
    return pvVar3;					//Return value for comparison
  }
```
8. After 3 hours of trying to recreate this function where the PRNG is seeded by a timestamp value.  I realise it might actually be a random value being generated, then pivot to break the check instead. The "`JNZ`" check, opcode `0x75`, is located at position 0x968 in the binary.  
	1. Open binary in vim
	2. Converting the binary to xxd txt data, ":%!xxd"
	3. Changed the opcode at position 0x968 to "`0x74`" (`JZ`), which reverses the check
	4. Convert the xxd txt data to binray, ":%!xxd -r"
9. Re-run the program and input the correct first parameter and an arbitrary second parameter.
```
kali@kali:~/$ ./impossible_password.bin 
* SuperSeKretKey
[SuperSeKretKey]
** asd
HTB{40b949f92b86b18}
```
10. The check now clears, and jumps to the next stage which is a third function that prints the flag in plain text.
```
void FUN_00400978(byte *param_1) {
  int local_14;
  byte *local_10;

  local_14 = 0;
  local_10 = param_1;
  while ((*local_10 != 9 && (local_14 < 0x14))) {
    putchar((int)(char)(*local_10 ^ 9));
    local_10 = local_10 + 1;
    local_14 = local_14 + 1;
  }
  putchar(10);
  return;
}
```
11. To understand the last function, I rewrote it in C++.  At the same time the first key is loaded into its variable, a set of hex values is added to variables `local_48`...`local_35`. Looking like an array is being filled.
Running the compiled program, generates the following output, which is the flag. 

```
kali@kali:~/$ g++ main.cpp; ./a.out 
HTB{40b949f92b86b18}
```
The code below recreates the array, and a set skip based on the value of a[0] generates the flag as the output sequence.

```
#include <stdlib.h>
#include <iostream>
using namespace std;
int main (){
	u_int a[] = {0x41, 0x5d, 0x4b, 0x72, 0x3d, 0x39, 0x6b, 0x30, 0x3d, 0x30, 0x6f, 0x30, 0x3b, 0x6b, 0x31, 0x3f, 0x6b, 0x38, 0x31, 0x74};

	int l14 = 0;
	u_int *l10 = &a[0];

	while( (*l10 != 9 && (l14<0x14))) {
		cout << ((char)(*l10^9));
		l10 = l10+1;
		l14 = l14+1;
	}
	cout <<  char(10);
	
	exit(0);
}
```
