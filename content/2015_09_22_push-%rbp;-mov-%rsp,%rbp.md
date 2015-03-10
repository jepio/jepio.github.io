Title: push %rbp; mov %rsp,%rbp
Date: 2015-9-22 8:57
Category: programming

There. Do I have your attention? With this post my intention is to finally
figure out what this pair of instructions actually mean. I mean, they show up
everywhere. To do this I'd like to deal with a simple C example.

    :::c
    int main(void)
    {
        for (int i = 0; i < 5; ++i);
    }

First let's compile it

    gcc -g -O0 test.c -c

and then let's disassemble

    objdump -S test.o

The output is the assembly interleaved with the source code.

    test.o:     file format elf64-x86-64

    Disassembly of section .text:

    0000000000000000 <main>:
    int main(void)
    {
       0:	55                   	push   %rbp
       1:	48 89 e5             	mov    %rsp,%rbp
        for (int i = 0; i < 5; ++i);
       4:	c7 45 fc 00 00 00 00 	movl   $0x0,-0x4(%rbp)
       b:	eb 04                	jmp    11 <main+0x11>
       d:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)
      11:	83 7d fc 04          	cmpl   $0x4,-0x4(%rbp)
      15:	7e f6                	jle    d <main+0xd>
      17:	b8 00 00 00 00       	mov    $0x0,%eax
    }
      1c:	5d                   	pop    %rbp
      1d:	c3                   	retq

An interesting thing to note, and what made me write this post was the idea:

> a loop is 5 instructions

and indeed it is:

1. assignment
2. unconditional jump to comparison
3. increment
4. comparison
5. conditional jump out of loop

When I was figuring this out in my head it looked slightly different:

1. assignment
2. comparison
3. conditional jump out of loop
4. increment
5. unconditional jump to comparison

but reordering does not change the logic.
