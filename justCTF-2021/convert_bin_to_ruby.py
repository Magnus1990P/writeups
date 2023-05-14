out = open("ruby_pdf.txt","w")
for c in HEX.replace("\n","").replace("  "," ").strip().split(" "):
    out.write( chr( int(c,16) ) )
out.close()