from string import maketrans
outtab = "cdefghijklmnopqrstuvwxyzab" 
intab = "abcdefghijklmnopqrstuvwxyz"
trantab = maketrans(intab, outtab)

#str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj." 

#print str.translate(trantab);

strurl = "http://www.pythonchallenge.com/pc/def/map.html"
print strurl.translate(trantab);