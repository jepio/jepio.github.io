Title: Embedding a gist in post
Date: 2015-03-10 18:29
Category: test

I want to share a python trick with you, that I have found to be very useful.
And since I want to also find out how to embed gists, I decided to use this post
as a testing ground.

[gist:id=e3ef019ee6e48672d81a,file=grouper.py]

This is the easiest (only?) way to group items from an iterator.

Now if I were to use pygments for this snippet, it would look like this:

    :::python
    import itertools as it

    def grouper(iterable, n, fillvalue=None):
        iters = (iter(iterable),) * n
        return it.izip_longest(n, fillvalue=fillvalue, *iters)

Which one looks better?
