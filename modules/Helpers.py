from functools import partial
from itertools import chain
from os.path import expanduser, join

flatten = chain.from_iterable

flatMap = lambda x, y: flatten(map(x, y))

joinHomeTo = partial(join, expanduser("~"))
