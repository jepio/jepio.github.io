#!/usr/bin/env python3
from datetime import datetime
from docopt import docopt

TEMPLATE = """
Title: {title}
Date: {tod.year}-{tod.month}-{tod.day} {tod.hour}:{tod.minute:02d}
Category: {category}

"""

__usage__ = "Usage: make_entry.py <title> <category>"

def make_entry(title, category):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    filename = "content/{}_{:0>2}_{:0>2}_{}.md".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title, tod=today, category=category)
    with open(filename, "w") as w:
        w.write(t)
    print("Created file -> ", filename)

if __name__ == '__main__':
    args = docopt(__usage__)
    title, category = args['<title>'], args['<category>']
    make_entry(title, category)

