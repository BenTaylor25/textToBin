
with open("bin.txt") as file_in:
    with open("text.txt", 'w') as file_out:
        for line in file_in.readlines():
            for eightbits in [line[i:i+8] for i in range(0, len(line), 8)]:
                char = chr(int(eightbits, 2))
                print(char, end='')
                file_out.write(char)
