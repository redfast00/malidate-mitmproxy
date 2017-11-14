# Malidate-mitmproxy

A plugin for [mitmproxy](https://mitmproxy.org/) that can execute some of the attacks described in [Cracking the lens: Targeting HTTP's hidden attack surface](http://blog.portswigger.net/2017/07/cracking-lens-targeting-https-hidden.html). This plugin communicates with the [malidate server](https://github.com/redfast00/malidate), an opensource alternative to some parts of the Burpsuite Collaborator server.

## Workflow

Start the proxyserver with
```
mitmdump --tcp '.*' -s "main.py --attack ReplaceHostAttack"
```
then configure your browser to use the proxyserver
```
chromium-browser --proxy-server="localhost:8080 --disable-http2"
```
 and start browsing. When you are done, compare the server results with the client results using:
```
./compare.py
```

## Setup

First, make a virtualenv and install the requirements.

```
virtualenv venv
pip3 install -r requirements.txt
```

Then configure the settings in `configfiles/config.json` and copy over
 `configfiles/secret_config.example.json` to `configfiles/secret_config.json` 
 and edit those settings.

## TODO

- [ ] implement more attacks
- [X] implement a way to choose between attacks
- [ ] improve `compare` script
- [ ] refactor
- [ ] make own custom launcher script 
