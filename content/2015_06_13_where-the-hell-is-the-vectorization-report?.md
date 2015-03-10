Title: Where the hell is the vectorization report?
Date: 2015-6-13 14:22
Category: programming

Everyone should care about vectorization. It's relatively easy for the compiler
to do on it's own compared to stuff like auto-parallelisation, and can yield
high performance gains on certain parts of the code. The win can be anything
from 2x to 8x, depending on what data type we're using and what kinds of
instructions our processor supports. The only condition is that we have to write
easy code that shows the compiler everything it needs to know to determine
whether it's safe to vectorize.

Most of the time we talk about vectorization of loops. It so happens that in
both clang and gcc the vectorizer is turned on automatically at `-O3`
optimization flags [^1]. What we're interested in is knowing how well it does.
And I don't mean benchmarking or profiling - we need to know if it has done its
job.  That's what vectorization reports are there for. Clang has a fairly large
set of flags to inform you of what went on behind your back:

    -Rpass=loop-vectorize
    -Rpass-missed=loop-vectorize
    -Rpass-analysis=loop-vectorize

I pretty much use all of them at the same time, everytime. You turn on the first
one and you see nothing, so you turn on the second one and it tells you that
this and that loop failed to be vectorized. Finally you have to turn on that
last one to find out why. There really ought to be a flag that turns all of them
on - something like `-fvectorize-report`.

But that's nothing compared to the trouble that gcc caused me. Like a good
citizen I open up my browser and search for *gcc autovectorization*. With
joy I remark that the first link leads to the GNU project website dealing with
[Auto-vectorization in GCC][auto-vect]. But when I get there, it tells me to use
`-ftree-vectorizer-verbose=N` to turn on a verbose vectorization report. Seems
reasonable, I think to myself, and start experimenting with it. But it doesn't
work in GCC 4.9.2. I get no report of anything, neither failures nor successes.
And on top of that, no warning/error message telling me that the flag doesn't
work. Luckily the internet has other websites and the LHCb twiki website tells
me that this flag is depracated in GCC 4.9. Someone should notify GNU of
that[^2]! The new flags are:

    -fopt-info-vec
    -fopt-info-vec-missed

You learn something new every day.


[^1]: Clang might have vectorization enabled by default, I haven't really looked
    into it.
[^2]: Don't worry, I plan on doing that myself and this post will help remind me
    of that.

[auto-vect]: https://gcc.gnu.org/projects/tree-ssa/vectorization.html
