<h1 align="center"><font color="orange">FireOver</font></h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.2-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/jayateertha043/FireOver/blob/master/LICENCE.txt" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
  <a href="https://twitter.com/jayateerthaG" target="_blank">
    <img alt="Twitter: jayateerthaG" src="https://img.shields.io/twitter/follow/jayateerthaG.svg?style=social" />
  </a>
</p>

>This tool is used to takeover Insecure Firebase Databases and automaticaly generate POC to report them,This tool can also delete or redo the POC's done by this tool(remove the data inserted into the database by this tool).

## REQUIREMENTS AND INSTALLATION
>Note:This tool requires Python 3.5 and above <br />
>pip install -r requirements.txt


## USAGE:
<img alt="USAGE" src="https://github.com/jayateertha043/FireOver/blob/master/usage.PNG" height="500px" width="100%"><br />
>Change the Config inside utils/config.py folder before use <br />

```python FireOver.py -u https://FirebaseDatabaseName.firebaseio.com```

```python FireOver.py --url https://FirebaseDatabaseName.firebaseio.com ```
<br /><br />
```python FireOver.py -l list.txt -o poc.txt```

```python FireOver.py --list list.txt --output poc.txt```
<br /><br />

```python FireOver.py -d poc.txt```

```python FireOver.py --delete poc.txt```

## DEMO:

<img alt="DEMO" src="https://github.com/jayateertha043/FireOver/blob/master/demo.PNG" height="500px" width="100%"><br />

<br />

## To Do:
*Add MultiThreading


*Add Getting list of URLS using search engine dorks and store them into list.txt for further takeovers<br />
## Author

👤 **Jayateertha G**

* Twitter: [@jayateerthaG](https://twitter.com/jayateerthaG)
* Github: [@jayateertha043](https://github.com/jayateertha043)

## Show your support
<a href="https://www.buymeacoffee.com/en3EoKG7j" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="50px" width="150px" ></a><br />
Give a ⭐️ if this project helped you!


## 📝 License

Copyright © 2020 [Jayateertha Guruprasad](https://github.com/jayateerthaa043).<br />
This project is [MIT](https://github.com/jayateertha043/FireOver/blob/master/LICENCE.txt) licensed.

