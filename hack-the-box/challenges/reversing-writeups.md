Baby RE
====
**FLAG:** HTB{B4BY_R3V_TH4TS_EZ}

Details
---
Show us your basic skills! (P.S. There are 4 ways to solve this, are you willing to try them all?) 

Steps
---
1. Open executable in Ghidra
2. Find references to string objects, given that it asks for input.  Which grants a starting point
3. Look at the string "Insert key:", jump to main function where it is used. Below this point is a CMP statement.
4. The CMP has previously done a LEA on two strings, where the first is the passphrase
5. Execute the program and insert the key `abcde122313`
6. Grab the flag, which is outputed `HTB{B4BY_R3V_TH4TS_EZ}`


<br><br>
Find The Easy Pass
====
**FLAG:** HTB{fortran!}

Details
---
Find the password (say PASS) and enter the flag in the form HTB{PASS} 

Steps
---
1. Executed the software, and found the "Wrong password!" string, which I found the location of and then first use of.
2. Going backwards in the code from this point I found the line for successful password and looked around this point for compares.
3. The password is split across multiple 96b data section, and there are two main separations in the data, because the second `r` is the same as the first.
4. The location of the first byte in each section is progressively assessed against the users input.
4. If the password entered is ok, the string "Good Job. Congratulations" is printed in a message box.

### Code
Code snippet from Ghidra.
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined __register FUN_0045407f(int param_1)
             int               EAX:4          param_1
        00454082 33 c0           XOR        param_1,param_1
        00454084 55              PUSH       EBP
        
		00454090 8d45 f8         LEA        param_1,[EBP + -0x8]
        00454093 ba88 4145 00    MOV        EDX=>DAT_00454188,DAT_00454188                   = 66h    f
        0045409d 8d45 f4         LEA        param_1,[EBP + -0xc]
        004540a0 ba94 41 45 00   MOV        EDX=>DAT_00454194,DAT_00454194                   = 6Fh    o
        004540aa 8d45 f0         LEA        param_1,[EBP + -0x10]
        004540ad baa0 41 45 00   MOV        EDX=>DAT_004541a0,DAT_004541a0                   = 72h    r
        004540b7 8d45 ec         LEA        param_1,[EBP + -0x14]
        004540ba baac 4145 00    MOV        EDX=>DAT_004541ac,DAT_004541ac                   = 74h    t
        
                             LAB_004540c4                                    XREF[1]:     00454055(j)  
        004540c4 8d45 e8         LEA        param_1,[EBP + -0x18]
        004540c7 baa0 4145 00    MOV        EDX=>DAT_004541a0,DAT_004541a0                   = 72h    r
        004540d1 8d45 e4         LEA        param_1,[EBP + -0x1c]
        004540d4 bab8 4145 00    MOV        EDX=>DAT_004541b8,DAT_004541b8                   = 61h    a
        004540de 8d45 e0         LEA        param_1,[EBP + -0x20]
        004540e1 bac4 4145 00    MOV        EDX=>DAT_004541c4,DAT_004541c4                   = 6Eh    n
        004540eb 8d45 dc         LEA        param_1,[EBP + -0x24]
        004540ee bad0 4145 00    MOV        EDX=>DAT_004541d0,DAT_004541d0                   = 21h    !
        
		004540f8 ff 75 f8        PUSH       dword ptr [EBP + -0x8]
        004540fb ff 75 f4        PUSH       dword ptr [EBP + -0xc]
        004540fe ff 75 f0        PUSH       dword ptr [EBP + -0x10]
        00454101 ff 75 ec        PUSH       dword ptr [EBP + -0x14]=>DAT_00454171            = E9h
        00454104 ff 75 e8        PUSH       dword ptr [EBP + -0x18]
        00454107 ff 75 e4        PUSH       dword ptr [EBP + -0x1c]
        0045410a ff 75 e0        PUSH       dword ptr [EBP + -0x20]
        0045410d ff 75 dc        PUSH       dword ptr [EBP + -0x24]
        00454110 8d 45 fc        LEA        param_1,[EBP + -0x4]
        00454113 ba08 0000 00    MOV        EDX,0x8
        
		0045411d 8d55 d8         LEA        EDX,[EBP + -0x28]
        00454120 8b83 f802 0000  MOV        param_1,dword ptr [EBX + 0x2f8]
                 
        0045412b 8b45 d8         MOV        param_1=>DAT_00454171,dword ptr [EBP + -0x28]    = E9h
        0045412e 8b55 fc         MOV        EDX,dword ptr [EBP + -0x4]
        00454131 e8f2 04fb ff    CALL       FUN_00404628                                     uint * FUN_00404628(uint * param
                 
        00454136 750c            JNZ        LAB_00454144
        00454138 b8dc 4145 00    MOV        param_1=>s_Good_Job._Congratulations_004541dc,   = "Good Job. Congratulations"
        
                             LAB_00454144                                    XREF[1]:     00454136(j)  
        00454144 b800 4245 00    MOV        param_1=>s_Wrong_Password!_00454200,s_Wrong_Pa   = "Wrong Password!"
        00454149 e8e2 38fd ff    CALL       FUN_00427a30                                     undefined FUN_00427a30(undefined
```



<br><br>


Impossible Password
====
**FLAG:** HTB{40b949f92b86b18}

Details
---
Are you able to cheat me and get the flag? 

Steps
---
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