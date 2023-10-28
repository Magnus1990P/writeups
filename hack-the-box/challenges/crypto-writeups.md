Bank Heist
===
**FLAG:** HTB{GORETIREMENTFUND!!}

Details
---
A beaufort encrypted cipher, where the key must be recovered and the cipher decrypted.

Steps
---
1. The message reads:
```
444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733.
84433 5533999 8666 84433 55566622255 4447777 22335556669.
4666 8666 727774447777.
47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369!!
```
2. It looks like a code for the old telephone numpad conversions, and decodes to  
```
IF YOU ARE READING THE CIPHER, YOU ARE OKAY.
YOUR SHARE OF THE HEIST IS IN YOUR HOUSE.
THE KEY TO THE LOCK IS BELOW.
GO TO PARIS. 
GSV XLWV GL GSV HZU OLXP : TLIVGRIVNVMGUFMW!!
```
3. Looks like a cipher, maybe Caesar or Vigenere, possible keyword is PARIS or FRANCE 
4. No such luck, testing Beaufort
5. It was a Beaufort cipher, with the key `ZZ`, the deciphered plaintext message is
```
THE CODE TO THE SAF LOCK : GORETIREMENTFUND!!
```
6. The flag is `HTB{GORETIREMENTFUND!!}`

<br><br>

The Last Dance
====
**FLAG:** HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}

Details
---
A ChaCha20 encrypted flag and message encrypted with the same keystream.  Since the plaintext message is known, we can get the keystream and use it to decrupt the flag. 


Steps
---
1. Collect the required info
```
iv = bytes.fromhex("c4a66edfe80227b4fa24d431")
encrypted_message = bytes.fromhex("7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990")
encrypted_flag = bytes.fromhex("7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7")
```
2. Recover the keystream using the message and encrypted message
```
ks = [c ^ p for c,p in zip(encrypted_message, message)]
```
3. Decrypt the flag using the recovered keystream
```
flag_plain = [c_flag ^ ks[index] for index, c_flag in enumerate(encrypted_flag)]
```
4. The flag is `HTB{und3r57AnD1n9_57R3aM_C1PH3R5_15_51mPl3_a5_7Ha7}`


<br><br>
Templed
====
**FLAG:** HTB{M0Nks_kN3w!}

Details
---
I found the following message in a temple, I had the sensation that they were hiding something. Could you help me discover what it was?

Steps
---
1. Find the Cipher / Code Alphabet used, by googling common ancient ciphers / code alphabets
2. Looks like the number encoding system found at [The Ciphers of the Monks](http://www.davidaking.org/Ciphers.html)
3. Decode the message as shown in the table below.
4. Grab the Flag.

### Code
The decoded image, below, resulted in the following set of values which represented a series of ASCII values which decodes into the flag.

| ASCII | DEC | Values |
|-------|-----|--------|
| H | 72  | 70 + 2 |
| T | 84  | 80 + 4 |
| B | 66  | 60 + 6 |
| { | 123 | 20 + 3 + 100 |
| M | 77  | 70 + 7 |
| 0 | 48  | 40 + 8 | 
| N | 78  | 70 + 8 |
| k | 107 | 100 + 7 |
| s | 115 | 10 + 100 + 5 |
| _ | 95  | 90 + 5 |
| k | 107 | 100 + 7 |
| N | 78  | 70 + 8 |
| 3 | 51  | 50 + 1 |
| W | 119 | 10 + 9 + 100 |
| ! | 33  | 3 + 30 |
| } | 125 | 20 + 5 + 100 |
