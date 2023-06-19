# RTL CTF 2021

## Crypto
- Welcome
  - **cipher:**		UlRMe0g0VkVfRlVOX1BMNFkxTkchfQ==
    - Base64:		RTL{H4VE_FUN_PL4Y1NG!}
    - **Flag:**		`RTL{H4VE_FUN_PL4Y1NG!}`
- Triangle
    - **cipher:**		0x133f29027034094a33253126395b3704
    - **Partial flag:**	0x52544c7b  
        key:		0x133f2902 ^ 0x52544c7b = 0x416b6579 = "Akey"  
        Flag(hex):		0x52544c7b315f6c33724e545f7830527d  
    - **Flag(ascii):** `RTL{1_l3rNT_x0R}`
- Wait, what!
    - **cipher:** 	"NBY{9x175777156k5608n3x889n5nx9215n2}"
    - **Partial key:**	"RTL"
    - **Key:**		"WIN"
    - Vigenere:	"RTL{9b175777156c5608a3b889f5ab9215f2}"
    - **Flag:**		`RTL{9b175777156c5608a3b889f5ab9215f2}`
- Ciphers Galore!
    - **cipher:** 		"NBY{9x175777156k5608n3x889n5nx9215n2}"
    - rot-47(cipher): 	"IKC{j1dgc3_tIpgk0_ty@113ex3_3y?}"
    - Caesar cipher(+17):  	"RTL{s1mpl3_cRypt0_ch@113ng3_3h?}"
    - **Flag:** 			`RTL{s1mpl3_cRypt0_ch@113ng3_3h?}`