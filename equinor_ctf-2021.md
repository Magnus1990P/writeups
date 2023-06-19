# Equinor CTF 2021

## Beginner
### Beginner/Encoding or encryption?
Solve with cyberchef, From hex -> From Base64 -> Rot13
```
C0 = "55 6b 4e 48 65 32 6f 7a 58 32 4e 6f 5a 31 39 6d 4d 48 6f 7a 58 7a 4e 68 63 44 42 78 64 6d 46 30 58 7a 46 68 58 32 77 77 61 47 56 66 4d 32 46 77 5a 57 78 6e 64 6a 42 68 66 51 3d 3d"
C1 = "UkNHe2ozX2NoZ19mMHozXzNhcDBxdmF0XzFhX2wwaGVfM2FwZWxndjBhfQ=="
C2 = "RCG{j3_chg_f0z3_3ap0qvat_1a_l0he_3apelgv0a}"
FLAG = "EPT{w3_put_s0m3_3nc0ding_1n_y0ur_3ncryti0n}"
```

### Beginner/Cipher salad with vinaigrette is so tasty
The cryptogram was a Vigenere cipher, but with a long keyword.  Running it through an autocracker, the first part of the keyword is discovered.
"**thisisav**"

With this, the keyword length can be discerned followed by bruteforcing the remainder of the keyword.

Final keyword is, "**thisisaverystrongkey**"


### Beginner/Numbers and letters
Split the document into a list of number,character pairs and grab all numbers which are prime while skipping 1.


## Crypto
### Crypto/Really Solid Algebra
Crack it by factorizing n and decrypt the cryptogram.


## Forensics
### Forensics/sysadmin1
Two part problem.  The partition table is not starting at 0, the partition is bitlocker encrypted with a password list.

1. Find the starting sector and calculate the starting byte of the bitlocker encrypted partition
1. Download dislocker
1. Run through a test for each password in the list to unlock the drive while specifying the offset.
1. When it is unlocked it is "mounted" to an intermediary location
1. Mount the intermediary location to a third location
1. Find the flag.