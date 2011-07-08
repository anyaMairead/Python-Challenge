import Image

im = Image.open("oxygen.png")

#use GIMP or similar image manipulation program to figure out where the
#grey bar ends. it ends around 607px on the x-axis. because each grey bar
#is 7px wide, i divided 607 by 7 & rounded up to get the range, then multiply
#i by 7 in order to avoid duplicates.
for i in range(87):
    print chr(im.getpixel((i*7,50))[0]),
    
a = "".join([chr(i) for i in [105, 110, 116, 101, 103, 114, 105, 116, 121]])
print a
