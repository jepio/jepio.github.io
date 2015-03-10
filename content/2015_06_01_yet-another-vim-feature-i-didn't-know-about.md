Title: Yet another vim feature I didn't know about
Date: 2015-6-1 1:27
Category: misc

As I was editting a python script this morning, I acidentally entered `K` in
normal mode. Vim quickly hid and revelead a shell which contained two lines:

> no Python documentation found for 'd'
>
>
> Press ENTER or type command to continue

*What is this sorcery*, I thought to myself. I quickly googled but couldn't
quite find an answer. Then I remembered vim's built-in help system and it
revealed the following:

>  K
>
> Run a program to lookup the keyword under the cursor.

Cool, ain't it? It uses the program specified by the variable `keywordprg`, the
default is `man -s` but for python files it changes to `pydoc`. That's something
worth remembering.
