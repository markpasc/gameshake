# gameshake #

`gameshake` is a command line tool for mirroring a MLKSHK shake to a Tumblr blog. It's a mashup of the [`tumblrout`](https://github.com/markpasc/tumblrout) and [`mlkshk-term`](https://github.com/markpasc/mlkshk-term) tools.

This won't actually be useful to anyone else, but I stuck it on GitHub anyway.


## Installation ##

Install its dependencies from the `requirements.txt` file:

    $ pip install -r requirements.txt

Then you can install it as any other Python program:

    $ python setup.py install

If you don't want to install its dependencies system-wide, try installing it in a [virtual environment](http://www.virtualenv.org/).


## Configuring ##

Use the `tumblrout` and `mlkshk-term` tools' `configure` commands to get some keys, then copy them from the `~/.tumblrout` and `~/.mlkshk` config files into a `~/.gameshake` config file instead. Note the argument names in `gameshake` start with `--tumblr-` or `--mlkshk-` as appropriate.


## Usage ##

See `gameshake --help` for supported commands.
