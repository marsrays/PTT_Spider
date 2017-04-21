# PTT_Spider
A Python code for web crawler of "www.ptt.cc"

# Develop Environment
Before use this code, you need Python 3 develop environment

PS. python version can not higher than 3.4, because this project used BeautifulSoup, and it is stick in Python 3.4 ^^

Use command get "requests" module
```
pip install requests --upgrade

```

# Running
Use command for run
```
python 八卦板爬蟲.py

```

# Package
Install "cx_Freeze" module
```
python -m pip install cx_Freeze --upgrade

```
If  you enconter install error, you can try command upgrade your pip version
```
python -m pip install --upgrade pip
```
Use command for package this project in .exe file
```
python setup.py build

```