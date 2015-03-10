Title: Vmstat rocks
Date: 2015-9-15 17:22
Category: misc

Something I find myself doing constantly is monitoring the performance of my
machines. CPU usage, VM (virtual memory) usage and the likes.

The goto-application for this purpose is top. Top is great, and can be used on
linux as well as BSD's, which I have been experimenting with recently, but is a
bit too noisy most of the time. The default color settings of red + yellow make
some items too dark and others too bright so I prefer the uncoloured output.
This still has the downside that you see numbers/text all over the place and it
makes it unlikely that you're going to catch a sudden change like high CPU usage
or an application filling all your ram. You may not care about that but I do.

While I mentioned portability of top as an advantage, there is a catch to it:
the *tops* in BSD and linux differ. The BSD one is based on the classic unix top
while the linux one is a reworked implementation. They aren't vastly different
but it does take some getting used to. Granted, it is possible to get the
classic top on linux but it's not available everywhere.

An alternative to top has always been `htop`. I myself have been a long time fan
of it over the classic top, and initially it was the only thing I used until I
started being concerned about portability. It has a very good color scheme by
default that shows mostly the same information as top but the colors allow it to
be interpreted with greater ease. But of the major BSDs I care about, OpenBSD
doesn't have it and it feels a bit *bolted on* in places where it is present
(FreeBSD/NetBSD, and also OS X). So I consider it to be a Linux only feature.

Another tools that I used constantly, is free paired with watch. Free gives a
nice overview of what is happening with your memory, how it is being used for
caching, how much is free and whether you are intensively using swap. Watch is
what makes free an interactie tool showing you changes. All you have to do is
open a terminal and run:

    watch -n 1 free -m

and you can monitor it, without using too much space (fits perfectly within a
small tmux pane). Both tools are part of the procps(-ng) package on linux.

Now the last tool which I only most recently grew to appreciate is `vmstat`.
Present on virtually all unices (I think) it shows all the vital system
information in tabular form. Perfect! It gives an overview of:

  * processes
  * memory
  * swap
  * disk I/O
  * interrupts and context switches
  * CPU split

so in one word: everything. I use it with a repeat delay of 5 and in units of
megabyte:

    vmstat -S M 5

and due to it's simplicity I think it will be my goto monitoring tool all my OSs
for a while.
