import Image

img = Image.open("pythonChallenge11.jpg")
new_img_size = tuple([x/2 for x in img.size])
new_odds = new_evens = Image.new(img.mode, new_img_size)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if x % 2 == 0 and y % 2 == 0:
            new_evens.putpixel((x / 2, y / 2), img.getpixel((x, y)))
        elif x % 2 == 1 and y % 2 == 0:
            new_evens.putpixel(((x - 1) / 2, y / 2), img.getpixel((x, y)))
        elif x % 2 == 0 and y % 2 == 1:
            new_odds.putpixel((x / 2, (y - 1) / 2), img.getpixel((x, y)))
        else:
            new_odds.putpixel(((x - 1) / 2, (y - 1) / 2), img.getpixel((x, y)))
    	    
new_evens.save('evens.jpg')
new_odds.save('odds.jpg')
