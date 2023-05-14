
#https://docs.fileformat.com/pdf/

blen=1

PDF = []

with open("challenge.pdf", "rb") as f:
    data = f.read()

i=0

i = data[i:].find(b"\x3c\x3c\x0a")
j = data[i:].find(b"\x3e\x3e\x06")

start   = i
end     = i + j + 3

while i != -1 and j != -1:
    print(start, end, data[start+3 : end-3])
    
    elements = {"data":b""}
    subdata = data[start+3 : end-3].strip().split(b"\n")
    
    #for sde in subdata:
    #    k,v = sde.split(" ")
        
    
    print(subdata)
    
    
    
    i = data[end:].find(b"\x3c\x3c\x0a")
    j = data[end:].find(b"\x3e\x3e\x06")
    
    start   = end + i
    end     = end + j + 3





#print(data)


