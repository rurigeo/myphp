import urlparse

URLscheme = "http"

URLlocation = "www.python.org"

URLpath = "lib/module-urlparse.html"

modList = ("urllib", "urllib2", \

"httplib", "cgilib")

#����ַ���������

print "��Google����pythonʱ��ַ����URL�Ľ������"

parsedTuple = urlparse.urlparse("http://www.google.com/search?hl=en&q=python&btnG=Google+Search")

print parsedTuple

#�������������URL

print "\������python�ĵ�ҳ���URL"

unparsedURL = urlparse.urlunparse( \

(URLscheme, URLlocation, URLpath, '', '', ''))

print "\t" + unparsedURL

#��·�������ļ����һ���µ�URL

print "\n����ƴ�ӷ�ʽ��Ӹ���python�ĵ�ҳ���URL"

for mod in modList:

    newURL = urlparse.urljoin(unparsedURL, "module-%s.html" % (mod))

    print "\t" + newURL

    #ͨ��Ϊ·�����һ����·�������һ���µ�URL

    print "\nͨ��ƴ����·��������Python�ĵ�ҳ���URL"

    newURL = urlparse.urljoin(unparsedURL,"module-urllib2/request-objects.html")

    print "\t" + newURL
