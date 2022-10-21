try:
	import urllib2
except:
	import urllib.request as urllib2
	

def get_proxy_opener(proxyurl, proxyuser, proxypass, proxyscheme="http"):
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, proxyurl, proxyuser, proxypass)

    proxy_handler = urllib2.ProxyHandler({proxyscheme: proxyurl})
    proxy_auth_handler = urllib2.ProxyBasicAuthHandler(password_mgr)

    return urllib2.build_opener(proxy_handler, proxy_auth_handler)

if __name__ == "__main__":

    proxy = input("url del proxy:") #tu proxy
    user = input("usuario:")  # tu user
    passw = input("password:") # tu pass  
   
    
    url_opener = get_proxy_opener(proxy, user, passw)

    urllib2.install_opener(url_opener)
    url_sanidad = "http://transparencia.gob.es/es_ES/buscar/contenido/cibi/CIBI_DPTO26"
    f = urllib2.urlopen(url_sanidad)
    html = f.read()
    f.close()

    # procesar HTML:
    

     
    #print url_opener.open(url).headers
   
