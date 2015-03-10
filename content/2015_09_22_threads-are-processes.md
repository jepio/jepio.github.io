Title: Threads are processes
Date: 2015-9-22 13:12
Category: programming

The standard thread implementation on linux is `pthreads` and processes can
easily be created by issuing a `fork` function call. While I was studying
processes recently and reading the man pages for `clone` I found two important
pieces of information:

* threads are commonly implemented using `clone`.
* the fork function calls the `clone` syscall.

The conclusion from these is that on linux **threads == processes**. So threads
are in reality *processes* with a shared address space and processes are really
*processes* with COW[^1] pages. You can find confirmation in many answers on
stackoverflow [such as this one][so-answer].

To me this is amazing, and kudos to the kernel devs for deciding that the two
can be implemented in the same way and for optimizing this one path to where
we are now.

[so-answer]:    http://stackoverflow.com/questions/807506/threads-vs-processes-in-linux
[^1]:           **C**opy **O**n **W**rite which makes spawning cheap to do.
