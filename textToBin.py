
with open("text.txt") as file_in:
    with open("bin.txt", 'w') as file_out:
        for line in file_in.readlines():
            for char in line:
                bits = bin(ord(char))[2:]
                while len(bits) < 8:
                    bits = '0'+bits
                print(bits)
                file_out.write(bits)
