Find The Easy Pass
====
**FLAG:** HTB{fortran!}

**PTS:**  20


### Details
Find the password (say PASS) and enter the flag in the form HTB{PASS} 

### Steps
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