# shellcode
My shellcodes and some scripts i made to make the process easier

# How to use

git clone all the stuffs first then cd inside it

 * Create symlinks for getbytes.py and shellcode.sh

```bash
sudo ln -s getbytes.py /usr/local/bin/getbytes
sudo ln -s shellcode.sh /usr/local/bin/shellcode
```

* Now, to create a shellcode, first write the assembly code for it or use one of my codes and then assemble it (for example execve.asm):

```bash
nasm -f elf32 execve.asm
ld -m elf_i386 -o execve execve.o
```

 * To get the shellcode from this assembled binary

```bash
shellcode execve 2
```

[ shellcode takes 2 arguments. The first argument is the assembled binary and the second is the number of lines (usually greater than 2). Try increasing the lines until you get a series of \x\x\x\x... which indicates the end of the shellcode]

 ## Whats the use of getbytes.py

 I made it to make thins a bit easier for me. For example, i want to push "hello!!!" into the ESP register for a write syscall. I dont want to write the hex for it in little endian format manaually, so to generate it, i made this shitty script. Some examples:

 ```bash
getbytes "welcomee"
getbytes "hello\!\!\!"
```
[Some special characters like '!' needs to be escaped as \! like in 2nd example]
