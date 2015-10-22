Title: printing symbol table
Date: 2015-10-21 20:15
Category: programming

Ever so often I want to do two things:

1. read the table of symbols exported from a shared library/executable
2. read the _soname_ of a library along with shared library dependencies

Here's how to do both with 3 tools: `nm`, `readelf`, `objdump`. For the sake of
brevity I will be working on a DSO[^1] called `libtest.so`.

[^1]: Dynamic Shared Object

## Reading symbol table

    :::bash
    nm -CD libtest.so
    readelf -sD libtest.so  # no demangling!
    objdump -CT libtest.so

## Dynamic section

    :::bash
    readelf -d libtest.so
    objdump -p libtest.so

`ldd` also works on shared libraries.

