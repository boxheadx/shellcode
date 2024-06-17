global _start

_start:

	xor eax, eax
	xor ebx, ebx
	xor ecx, ecx
	xor edx, edx

	mov al, 0xb
	push 0x4e68732f
	push 0x6e69622f
	mov bl, byte [esp+0x7]
	xor bl, bl
	mov byte [esp+0x7], bl
	mov ebx, esp
	int 0x80

	mov al, 0x1
	xor ebx, ebx
	int 0x80


