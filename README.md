# slackbot
A chat bot for [Slack](https://slack.com) inspired by [this article](https://code.tutsplus.com/articles/building-a-slack-bot-using-python--cms-29668) and [tutsplus/PythonSlackBot](https://github.com/tutsplus/PythonSlackBot).


## Requirements
- **[python](https://www.python.org/downloads/)**, specifically version 2.7
- **[pip](https://pip.pypa.io/en/stable/installing/)**, the Python package manager
for installing packages we need.
- **[virtualenv](https://virtualenv.pypa.io/en/latest/installation/)**, to manage
a virtual environment.
- **[python-slackclient](http://python-slackclient.readthedocs.io/en/latest/)**, a
Slack client for Python.
- **[pandas](https://pandas.pydata.org/getpandas.html)**, a library providing
high-performance, easy-to-use data structures and data analysis tools for Python.


## Setup Environment
After virtual environment is activated, export app's secrets like this:

```bash
export CLIENT_ID='xxx.xxx'
export CLIENT_SECRET='xxx'
export VERIFICATION_TOKEN='xxx'
export SLACK_BOT_TOKEN='xoxb-xxx-xxx'
```


## Run the Bot
With virtual environment turned on and app's secrets exported to the environment, go ahead and start your app:

```bash
$ python slackbot.py
```
