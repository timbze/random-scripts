# My Random Scripts

## suspendInSixtySeconds.py

Does what it says. Create entry in /etc/crontab like:
`45 18   * * *   user   python3 ~/RandomScripts/suspendInSixtySeconds.py`

At 18:45 each day a window pops up with a 60 second count-down, unless you cancel it, it will suspend (sleep) your computer.
