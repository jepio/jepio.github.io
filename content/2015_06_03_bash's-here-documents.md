Title: Bash's here documents
Date: 2015-6-3 11:11
Category: programming

I'm just about to finish reading the fantastic essay by Neal Stephanson entitled
"*In the Beginning was the Command Line*" and I stumbled upon this quote:

> Unix is hard to learn. The process of learning it is one of multiple small
> epiphanies. Typically you are just on the verge of inventing some necessary
> tool or utility when you realize that someone else has already invented it, and
> built it in, and this explains some odd file or directory or command that you
> have noticed but never really understood before.

In the essay it appears not far from a reference to this very old dilbert
comics:
![unix hacker]({filename}/images/unix-hacker.png)

Now I thought it's worth mentioning these two things because of what I'm
about to write about next. My biggest complaint against
[gnuplot](//www.gnuplot.info) has always been that it is missing bash-like
features - access to utilities for basic data processing, simple looping. This
makes it hard to work with for anything but the simplest plotting scripts.
Instead I always reached for python's matplotlib library, which I love to hate,
whenever I had to perform a more demanding task.

I was aware of the possibility of somehow calling gnuplot from inside bash, but
this never appealed to me. It seemed to be a *forced*, not elegant, solution to
the problem at hand. But it wasn't until today that it finally dawned on me that
this is actually **the** right solution and I decided to write about it.

The bash syntax I am referring to is called `Here Documents`. Inside a script
you double redirect (kind of like append) to stdin the word `EOF`. Everything
entered after this point will be entered into the application you are calling,
until it hits the word `EOF`, the exact same one that you specified. You can use
bash variables inside the *document* and everything will be expanded properly.
It works with everything: python, gnuplot, you name it. I have often felt the
need to call out from bash to python because python's syntax is so much simpler.
Now I have a way:

    :::bash
    #!/bin/sh

    python3 << EOF
    print("$*")
    EOF

Calling this script is equivalent to doing `echo`, but probably does not cover
many corner cases.

Still, I now feel comfortable with using this feature the next time I need to
work with gnuplot. And like Neal wrote, it took an epiphany for me to realise
that gnuplot does not need to have bash built into it to be useful, it is enough
that it can handle arbitrary textual input from the outside.

