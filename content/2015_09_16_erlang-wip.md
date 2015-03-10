Title: Erlang-wip
Date: 2015-9-16 15:09
Category: misc
Status: draft

Joe Armstrong, one of the creators of erlang, often has smart things to say.
From what I have observed by following his _blog_ (not sure I would call it
that) and reading his occasional post on the erlang mailing list, he's a very
down-to-earth guy. Today I saw his post in which someone was asking which data
type is more efficient in erlang: tuple or map. He countered by questioning
the rationale behind worrying about efficiency in this case and cited a quote
from Bell labs which I whole heartedly agree with.

    An incorrect program can be made arbitrarily fast.

I have caught myself doing this more than I'd like to admit. Optimising a
program before you're sure of the results is a bad habit that has spread all
over the place and we must stop it. I want to remember to stop myself from
doing it.
