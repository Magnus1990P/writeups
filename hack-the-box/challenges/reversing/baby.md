Baby RE
====
**FLAG:** HTB{B4BY_R3V_TH4TS_EZ}

**PTS:**  10

### Details
Show us your basic skills! (P.S. There are 4 ways to solve this, are you willing to try them all?) 

### Steps
1. Open executable in Ghidra
2. Find references to string objects, given that it asks for input.  Which grants a starting point
3. Look at the string "Insert key:", jump to main function where it is used. Below this point is a CMP statement.
4. The CMP has previously done a LEA on two strings, where the first is the passphrase
5. Execute the program and insert the key `abcde122313`
6. Grab the flag, which is outputed `HTB{B4BY_R3V_TH4TS_EZ}`