# Webscraping with Python (O'Reilly)

## Notes

### urllib`

Standard Python Lib for handling webrequests, cookies, metadata (\(docs\))[https://docs.python.org/3/library/urllib.html]


(the *Requests* package is recommended for higher level HTTP interaction)

Contains several modules:
* urllib.request
 * open/read URLs
* urllib.error
 * handle request exceptions
* urllib.parse
 * parsing URLs
* urllib.robotparser
 * parsing *robots.txt*


urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)


### Virtual Environments
Contain required libraries within a virtual env to avoid global installation:

```python
$ virtualenv newVirtEnv // c
$ cd newVirtEnv/
$ source bin/activate # required to make virtenv live
```
