# PyLogcat
**PyLogcat**  is an application log system similar to Android Logcat for Python.

PyLogcat currently supports the following log levels.

- **Error** : Critical messages which can cause application malfunction   
- **Warning** : Priority messages which indicate the potential problem in application
- **Information** : Proirity messages which help users tracing application execution
- **Verbose** : Debug messages which help developers debugging application under development 

## How To
### Install package
```shell
pip install pylogcat
```
### Import modules
```python
from pylogcat import Log, Level
```

**Log** module privodes main functions for application log.

**Level** enumerates supported log levels as **v**, **i**, **w**, and **e** for verbose, informatin, warning, and error messages.

### Setup log level
Log level is set as **v**erbose which means all messages will be shown. Users can set log level as **e**rror, **w**arning, **i**nformation, or **v**erbose as required. For example, users can set log level as information by adding the following line of code
```python
Log.level = Level.i
```

### Create log message

#### Verbose log message
Log messages will be shown only if log level is set as **v**.
```python
Log.v(tag, message)
```
#### Information log message
Log messages will be shown only if log level is set as **v** or **i**.
```python
Log.i(tag, message)
```
#### Warning log message
Log messages will be shown only if log level is set as **v**, **i**, or **w**.
```python
Log.w(tag, message)
```
#### Error log message
Log messages will be shown no matter what log level is set.
```python
Log.e(tag, message)
```

## Limitations
**PyLogcat** can only print log messages on console now.