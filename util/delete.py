try:
    import requests
    from printy import printy,inputy
    import sys
except:
    print("Requirements Error ,Please install requirements from requirements.txt")
    sys.exit()
def deletepoc(url):
    try:
        x = requests.delete(url)
        if x.status_code==200:
            printy("Deleted :"+ url,'n')
        else:
            printy("[*]Error deleting"+url,'r>')
    except:
        printy("[*]Check Internet Connection"+url,'r>')
