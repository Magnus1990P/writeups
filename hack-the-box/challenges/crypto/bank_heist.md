Bank Heist
====
**FLAG:** HTB{GORETIREMENTFUND!!}

**PTS:** 20 

### Details
You get to the scene of a bank heist and find that you have caught one person. Under further analysis of the persons flip phone you see a message that seems suspicious. Can you figure out what the message to put this guy in jail?


### Steps
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

