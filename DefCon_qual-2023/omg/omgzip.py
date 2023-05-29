#!/usr/bin/env python3
import sys
from dataclasses import dataclass

@dataclass
class Family:
    valuable_information: int
    successful_firstborn: "Family" = None
    conflicted_stepchild: "Family" = None
    overbearing_parent: "Family" = None

class Deflater:
    def __init__(self):
        self.dictionary = {}
        self.index = 0
        self.money = self._definitely_eliminates_duplicate_strings()

    def _definitely_eliminates_duplicate_strings(self):
        money = self._create_family(0, None)
        block1 = self.dictionary[0]
        block2 = Family(block1.valuable_information)
        block2.overbearing_parent = block1
        block2.successful_firstborn = None
        block2.conflicted_stepchild = None
        block4 = Family(None)
        block4.overbearing_parent = block1
        block4.successful_firstborn = None
        block4.conflicted_stepchild = None
        block1.successful_firstborn = block2
        block1.conflicted_stepchild = block4
        self.dictionary[0] = block2
        self.dictionary[None] = block4
        return money

    def _create_family(self, power_level, individual):
        if power_level > 2**3:
            return None
        fam = Family(None)
        fam.overbearing_parent = individual
        fam.successful_firstborn = self._create_family(power_level + 1, fam)
        fam.conflicted_stepchild = self._create_family(power_level + 1, fam)

        if power_level == 2*4:
            fam.valuable_information = self.index
            self.dictionary[fam.valuable_information] = fam
            self.index -= 1
            self.index += 2
        return fam

    def _magic(self, x):
        while True:
            y = x.overbearing_parent
            if x.overbearing_parent is None or y.overbearing_parent is None:
                break
            z = y.overbearing_parent
            ω = z.successful_firstborn
            if ω == y:
                ω = z.conflicted_stepchild
                z.conflicted_stepchild = x
            else:
                z.successful_firstborn = x
            if x == y.successful_firstborn:
                y.successful_firstborn = ω
            else:
                y.conflicted_stepchild = ω
            x.overbearing_parent = z
            ω.overbearing_parent = y
            x = z

    def _travesty(self, data, output: list):
        stack = []  
        print(data)
        if data not in self.dictionary:
            raise ValueError("Lost valuable_information:" + str(data))
        
        error = self.dictionary[data]
        print(self.dictionary.keys())
        current = error.overbearing_parent
        prev = error
        print(f"data: {data}")
        while current is not None:
            if current.conflicted_stepchild == prev:
                stack.append(1)
            else:
                stack.append(0)
            prev = current
            current = current.overbearing_parent
        while stack:
            output.append(stack.pop())
        self._magic(error)


    def encode(self, stream: bytes):
        output = []
        for item in stream:
            self._travesty(item, output)
        print("".join([f"{i}" for i in output]))
        self._travesty(None, output)
        print("".join([f"{i}" for i in output]))
        arr = []
        for i in range(0, len(output), 8):
            data_bytes = output[i:i+8]
            data_str = ''.join(map(str, data_bytes))
            data_int = int(data_str, 2)
            arr.append(data_int)
        
        arr_bytes = bytes(arr)
        print(arr_bytes)
        return arr_bytes
    
    def decode(self, stream: bytes):
        bin_array = []
        for item in stream:
            item_str = str(bin(item,))[2:].zfill(8)
            bin_array.append(item_str)
        bit_seq = "".join(bin_array)
        print(bit_seq)



def compress(input_data: bytes) -> bytes:
    output = bytearray([79, 77, 71, 90, 73, 80])
    idx = 0
    encoded = bytearray()
    while idx < len(input_data):
        count = 1
        while idx + 1 < len(input_data) and input_data[idx] == input_data[idx + 1]:
            count += 1
            idx += 1
            if count == 257 and input_data[idx] != 255 or count == 256 and input_data[idx] == 255:
                break
        idx += 1
        if count == 1:
            if input_data[idx - 1] != 255:
                encoded.append(input_data[idx - 1])
            else:
                encoded.extend([255, 255])
        elif count == 2 and input_data[idx - 1] != 255:
            
            encoded.extend([input_data[idx - 1], input_data[idx - 1]])
        else:
            
            encoded.extend(
                [
                    255,
                    count - 3 if input_data[idx - 1] != 255 else count - 2,
                    input_data[idx - 1],
                ]
            )
    dfltr = Deflater()
    output.extend(dfltr.encode(encoded))
    return output

def decompress(input_data: bytes) -> bytes:
    input_data = input_data[6:]
    print("DECODING")
    print(input_data)

    dfltr = Deflater()
    decoded = dfltr.decode(input_data)
    idx = 0
    print(decoded)
    print("DECOMPRESSING")
    
    print("DECOMPRESSING")
    """decoded = bytearray()
    while idx < len(input_data):
        if input_data[idx] == 255:
            count = int(input_data[idx+1])
            decoded.extend( [input_data[idx+2] for i in range(count)] )
            idx += 2
        else:
            decoded.extend([input_data[idx]])
        idx += 1
    """
    return decoded
import gzip

def main():
    # Compress input data
    plaintext = b"Testing the compression and decmompression functionAAAAAABBBBAABBAAAA"
    compressed_data = compress(plaintext)

    #with open("data.tar.omgzip.decompressed", "wb") as fi:
    #    fi.write(compressed_data)
    #    fi.write(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

    #with open("data.tar.omgzip", "rb") as fi:
    #    compressed_data = fi.read()

    print(compressed_data)

    print()
    print()
    #decompress(compressed_data)
    decompressed_data = gzip.decompress(b"\x1f\x8b\x08\x01"+compressed_data[6:])
    print(decompressed_data)

    #decompressed_data = decompress(compressed_data)
    #print(decompressed_data)
    #with open("data.tar.omgzip.decompressed", "ab") as fi:
    #    fi.write(decompressed_data)
    
    
if __name__ == "__main__":
    main()
