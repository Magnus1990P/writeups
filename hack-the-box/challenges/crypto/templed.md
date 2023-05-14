Templed
====
**FLAG:** HTB{M0Nks_kN3w!}

**PTS:**  10

### Details
I found the following message in a temple, I had the sensation that they were hiding something. Could you help me discover what it was?


### Steps
1. Find the Cipher / COde Alphabet used, by googling common ancient ciphers / code alphabets
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


![Encoded message](https://gitlab.hackitguys.com/ctf/hackthebox/-/raw/master/challenges/data/6358819bec076521dffa026da9636c5a.png)
