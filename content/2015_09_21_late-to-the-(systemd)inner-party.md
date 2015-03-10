Title: Late to the (SystemD)inner party
Date: 2015-9-21 10:28
Category: misc

I may be coming late to the SystemD bashing party, but I'd just like to say
that I disagree with all of the opponents of this init system. It makes sense
to have all of the basic components in one place (journal, basic networking),
it does speed up booting and as far as I know has a solid code base.

Feeling your *unix philosophy* has been violated? How has _it_ benefited you
in this case before? The init system is not something that you run in your
shell where piping, composition and all this nice stuff makes sense. It runs
before you have a chance to mess with the system and for all you should care it
should not get in the way.

Systemd makes administering systems easier, my knowledge is more portable
thanks to it and the wide adoption. This also means that there probably are
more people who like it (or don't give a fuck) than those that criticize it. So
deal with it.
