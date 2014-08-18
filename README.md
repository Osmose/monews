# MoNews - News Aggregation for Mozilla Stuff

So like I've got some ideas for this but right now it just sort've aggregates a
bunch of feeds together.

Abbreviated setup:

1. Make a virtualenv.
2. `pip install -r requirements.txt`
3. `cp monews/settings/local.py-dist monews/settings.py/local.py`
4. Edit `local.py` to be right for you and your emotions.
5. `./manage.py syncdb`
6. `./manage.py migrate`

And you're done!

## License

Release under the MIT License. See LICENSE for details.
