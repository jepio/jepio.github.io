Title: The actual source of the bad battery life rumour surrounding linux
Date: 2015-8-23 19:48
Category: misc

This one is pretty widespread and gets repeated a lot:

> I don't use Linux because the battery life is worse than under Windows

Here's what I have to say about this.

My laptop is a Haswell machine. I say Haswell, because that's not only the
processor generation right there - it's also the chipset, DRAM controller
and GPU. What that means is that everything works together as a *package*
to deliver the lowest power usage possible. And it does that quite well -
most of the time. 

The kernel itself is pretty good with handling battery life. All tweaks
that can be made are built into the kernel and can be modified through
either the proc or sys filesystems. Some of them are activated by default -
like CPU scaling. Others are best left in the hands of a tool that can
change the settings based on whether external power is connected - I used
to be a [Laptop Mode Tools][lmt] guy but lately I have turned to [TLP][tlp]
(since I have a Thinkpad). TLP requires a little less tweaking but both do
the same thing. I have also heard of jupiter and pm-utils but the former is
(from what I heard) dead and the latter I have not investigated.

The ultimate tool that every laptop user should have running almost
constantly is [PowerTop][powertop]. As the name suggests, it's a top-like
program for displaying power drain. Originally written by Intel, it's
probably best suited for use with their hardware but most of the
functionality should work with AMD processors as well. PowerTop has a
tabbed ncurses interface and shows the following information:

* summary screen with power estimate by process along with a 
  wakeup-per-second count - kill high wake-up applications
* package/core/gpu power state view - tells you if your hardware is
  sitting in the lowest power states enough.
* processor frequency breakdown - allows you to notice when your
  hardware is not down-clocking enough.
* per device power usage estimates - the precision is suspicious but if
  a device is draining a lot of power maybe it's best to disconnect it.
* tunables - tune the most common system settings.

The first four have helped me multiple times to name a few. They allow me to
identify when an application is responsible for more power usage than I
would have expected. When a kernel bug stopped my laptop from reaching
package power states lower than PC2, I could find that out and reboot
instead of wasting power. When something strange had set my min and max
processor frequencies to 100%, I had the chance to notice and fix that.
My bluetooth was turning on after being blocked on every resume, and I saw
that through the device stats tab. So if you care at all about power usage,
PowerTop is your friend.

Thanks to this utility I can also give some numbers to back up my claims of
*good* Linux battery life. When my laptop idles with the screen off it uses
around 4 W. When watching a movie I have seen constant power drain of 6.5
W, thanks to **hardware accelerated decoding**. I'll come back to this
later. Normal usage email, web, some text editing keeps me at between 7 and 9 W.
I consider all of these values, especially the movie watching usage, to be
very good.

The only thing that really kills Linux laptops is flash. Or the lack
thereof. Flash is everywhere on the web (still) even though it has had
countless security advisories to prove it should be killed a long time ago.
What's more, the Linux version from Adobe does not get new features and is
only eligible for security updates. This means it does not have hardware
acceleration like the windows version, which leads to **insane** power
usage. And by insane I mean 12-15 W are not unusual. This effectively cuts
my battery life in half. The real killer here is youtube. While google is
moving it away from flash towards HTML5, the HTML5 does not make it any
better. Chrome does not use acceleration on Linux, and Firefox is not ready
for it by default either (even with gstreamer it does not work particularly
well for me). The adobe alternatives - lightspark, gnash - did not show
better results when I tested them.

So for me the conclusion is easy - if you want battery life, don't use
youtube. Or rather, don't use youtube in your browser. I have had much
better results with listening to youtube music through mps-youtube, a
python program for streaming from youtube from the command line. But aside 
from that I am satisfied with my laptop's performance. We have come a long
way and the next objective should be to accelerate HTML5 on the web. Of course
distributions should also pay extra attention to this aspect and enable many 
power saving settings by default.

[lmt]:		http://www.samwel.tk/laptop_mode/
[tlp]:		http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html
[powertop]:	https://01.org/powertop
