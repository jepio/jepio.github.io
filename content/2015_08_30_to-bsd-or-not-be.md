Title: To BSD or not be
Date: 2015-8-30 3:30
Category: misc

I became interested in BSD's this week. The thought of installing one on my
hardware had been crawling around my head ever since someone told me their
"plan for the weekend is to install an original Unix while my girlfriend is
away".

So I dived in and tried what I believe to be the 3 most popular and root
distributions: NetBSD, FreeBSD, OpenBSD. I cared about 3 things: support for
EFI booting, GPT, and WiFi.

First I had to dig through lots of (what I consider to be) legacy information
about slices, wedges and (BSD) disklabels.

FreeBSD has an EFI boot loader, supports GPT but the iwm module panic the
kernel about 80% of the time.

NetBSD supports GPT, doesn't have an EFI bootloader and WiFi works 90% of the
time. Only sometimes does it decide to show me the middle finger.

OpenBSD doesn't support GPT, nor EFI, and I can't test the WiFi because the
firmware needs to be downloaded after the install. Talk of planning right
there... Someone is working on EFI and GPT upstream which works in a virtual
machine, but I'm having problems installing it onto a real hard drive.

Update:
So FreeBSD is still unusable due to the WiFi-related panics. NetBSD seems to
have decided that after initially working quite correctly with respect to the
WiFi, the wpa-supplicant is incorrect for it. So now on boot it stalls at the
WiFi configuration until I cancel. Since I don't have time to figure these
things out right now, I'll leave it for a better time.

OpenBSD appears to work quite well if you ignore the not-obvious mechanics of
mixing __experimental__ GPT support with classic BSD disklabels. I made 1
OpenBSD partition and within that 4 labels: /, swap, /usr, /var. But when using
`disklabel` it also showed me _some_ of the other partitions that I had on that
hard drive. Some, because I have 16 GPT partitions + the 4 OpenBSD ones and only
16 total are supported by disklabel.

When it comes to booting I can boot FreeBSD using only their bootloader, fully in
EFI mode. NetBSD can be booted as a kernel from EFI grub. The only one that
can't be booted in EFI mode is OpenBSD. Although that is being worked on.

On the bright side, all of the things I was testing are part of *BSD-CURRENT.
This goes especially for the iwm module used by my Intel 7260 chip. It was first
introduced to OpenBSD, then NetBSD copied it and finally it made it's way into
FreeBSD. So hopefully once the rough edges are ironed out things will be up to
this years par some time next year (or in November in the case of OpenBSD). I'll
definitely keep tracking the progress, but for now I'll experiment with FreeBSD
in a VM.
