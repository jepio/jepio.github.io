Title: pushing and popping
Date: 2015-10-9 9:24
Category: shell

Today's blog post will be about da pushing and da poppin'. More specifically
the shell kind.

`pushd <dir>` is like `cd <dir>` except that it puts your previous location on
the directory stack before changing directory. 

The directory stack can be inspected with `dirs`. The _top_ is on the left.

It is possible to go back to a previous directory (and pop the current one of
the stack) using `popd`.

This should be useful!
