Title: Dynamic linking and the RUNPATH
Date: 2015-9-21 13:18
Category: programming

If you want to have binaries and libraries portable across linux systems, or
even portable across locations on your filesystem, you need to know a bit about
dynamic linking.

First read `man ld.so`, this will tell you about where libraries are looked up
when they are being searched for during application startup. This should also
tell you something about why using RPATH is a bad idea (it's because it
overrides all else with a fixed location - useless).

Next you will want to see what is currently in the RUNPATH of an elf *thing* (I
might call this RPATH in future, with the understanding that I mean alias
RPATH=RUNPATH). There are atleast two ways of achieving this with standard
tools. They are

    objdump -p <binary>

and

    readelf -d <binary>

It's usually a good idea to pipe the output through

    egrep 'R(UN)?PATH'

which catches the *legacy* case of RPATH usage as well.

Finally, you are likely to want to modify it (I know I frequently am). Again,
there are two tools that can do the job: `chrpath` and `patchelf`. They are
very similar and can also quickly print the content of RUNPATH. Below are their
usage strings.
chrpath:

    Usage: chrpath [-v|-d|-c|-r <path>] <program> [<program> ...]

       -v|--version                Display program version number
       -d|--delete                 Delete current rpath/runpath setting
       -c|--convert                Convert rpath to runpath
       -r <path>|--replace <path>  Replace current rpath/runpath setting
                                   with the path given
       -l|--list                   List the current rpath/runpath (default)
       -k|--keepgoing              Continue as much as possible after an error.
       -h|--help                   Show this usage information.

patchelf:

    syntax: patchelf
      [--set-interpreter FILENAME]
      [--print-interpreter]
      [--set-rpath RPATH]
      [--shrink-rpath]
      [--print-rpath]
      [--force-rpath]
      [--remove-needed LIBRARY]
      [--debug]
      [--version]
      FILENAME

`patchelf` was developed by the [nixos][nix] people, who depend on it to make
their whole idea of a package manager work.

[nix]: //nixos.org/nix
