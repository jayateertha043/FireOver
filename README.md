<h1 align="center">FireOver</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.2-blue.svg?cacheSeconds=2592000" />
  <a href="https://github.com/jayateertha043/FireOver/blob/master/LICENCE.txt" target="_blank">
    <img alt="License: MITT" src="https://img.shields.io/badge/License-MITT-yellow.svg" />
  </a>
  <a href="https://twitter.com/jayateerthaG" target="_blank">
    <img alt="Twitter: jayateerthaG" src="https://img.shields.io/twitter/follow/jayateerthaG.svg?style=social" />
  </a>
</p>

> This tool is used to takeover Insecure Firebase Databases and automaticaly generate POC to report them,This tool can also delete the POC's done(to remove the datas inserted into the database by this tool).

## REQUIREMENTS AND INSTALLATION

pip install -r requirements.txt


## USAGE:
<img alt="USAGE" src="https://github.com/jayateertha043/FireOver/blob/master/usage.PNG"><br />
python FireOver.py -u https://FirebaseDatabaseName.firebaseio.com
python FireOver.py --url https://FirebaseDatabaseName.firebaseio.com

python FireOver.py -l list.txt -o poc.txt
python FireOver.py --list list.txt -o poc.txt

python FireOver.py -d poc.txt
python FireOver.py --delete poc.txt

## Author

👤 **Jayaateertha G**

* Twitter: [@jayateerthaG](https://twitter.com/jayateerthaG)
* Github: [@jayateerthaa043](https://github.com/jayateerthaa043)

## Show your support
<a href="https://www.buymeacoffee.com/en3EoKG7j" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" style="height: 50px !important;width: 100px !important;" ></a><br />
Give a ⭐️ if this project helped you!


## 📝 License

Copyright © 2020 [Jayaateertha Guruprasad](https://github.com/jayateerthaa043).<br />
This project is [MIT](https://github.com/jayateertha043/FireOver/blob/master/LICENCE.txt) licensed.

