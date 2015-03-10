Title: playing with cp
Date: 2015-10-19 12:15
Category: misc

BTRFS breathes new air into the old `cp` command. Suddenly it can be used to
create instantaneous copy-on-write (CoW) snapshots of single files via `cp
--reflink`.

When you want to convert a folder to a subvolume, you are best of with the
following commands:

    # mv folder folder_old
    # btrfs su create ./folder
    # cp -a --reflink ./folder_old/. folder

If you want to disable data CoW (as with `nodatacow` mount option [but which
isn't that useful because it applies to the whole btrfs volume]) on single
files you need apply the xattr +C to it, and defrag, or simply `cp` it (if it's
a folder best to use `cp -a folder/. dest`).

    $ chattr +C file
    $ btrfs fi defrag file # or
    $ cp --reflink=never file file.new && mv file.new file

And there you have it: cp is suddenly much more useful.
