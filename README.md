# Webscraping with Python (O'Reilly)
---
## Notes

### urllib

Standard Python Lib for handling webrequests, cookies, metadata [\(docs\)](https://docs.python.org/3/library/urllib.html)


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
Use containers and specify required libraries within a virtual env to avoid global installation

Note that the methods for creating virtenvs differs between Python2 and Python3.

Py3 now natively supports virtual environments via the built-in `venv` command, whereas Py2 uses `virtualenv` that requires a separate install via `apt install virtualenv`.

**For Python 2**

```Python
$ virtualenv ./newVirtEnv # create virtenv
$ cd newVirtEnv/
$ source bin/activate # required to enable virtenv
```

(optional download `virtualenvwrapper` provides utility functions if required)

**For Python 3**


```Python
$ python3 -m venv ./newVirtEnv # create virtenv
$ cd newVirtEnv/
$ ./bin/activate # required to enable virtenv
```

** To Deactivate virtenv**

`$ deactivate`

** Managing Dependencies **

The virtenv will be created without dependencies.
To package a pre-existing project, the virtenv can be created on top of the existing folder but the dependencies will have to be specified and reinstalled into the virtenv.


```
# while in the dev environment with the required dependencies
$ pip freeze > ./virtenv/requirements.txt
$ cd ./virtenv
$ pip install -r requirements.txt
```

