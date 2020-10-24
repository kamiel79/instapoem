from PIL import Image, ImageDraw, ImageFont
import sys
import shutil
import glob
import os.path
import random
from igsettings import *

class Poem:

	def do_poem(self):
		# Based on the work of Muthukrisnan
		# https://muthu.co/instagram-quotes-generator-using-python-pil/

		#if poem and image in args, load them, else get the latest poem and a random image
		if (len(sys.argv) == 3):
			poem_file = sys.argv[1]
			file = open (DEFAULT_POEMS_DIR + poem_file, "r")
			title = file.readline()
			imagename = sys.argv[2]
			print("Using image " + imagename + " for poem " + poem_file)
			img = Image.open(IMAGE_PATH + imagename)
		else:
			list_of_files = glob.glob(DEFAULT_POEMS_DIR + '/*.txt')
			poem_file = max(list_of_files, key=os.path.getctime)
			file = open (poem_file, "r")
			title = file.readline()	#title is first line
			print("Title: " + title)
			#get image from flickr or if not available from default folder
			from flickr import get_flickr_img
			if (get_flickr_img(title, THE_FLICKR_IMAGE)):
				img = Image.open(THE_FLICKR_IMAGE)
				imagename = THE_FLICKR_IMAGE
			else:
				imagename = random.choice(os.listdir(DEFAULT_BKG_DIR))
				img = Image.open(DEFAULT_BKG_DIR + imagename)
			print ("Using " + imagename + " for " + title)

		#read the file and make sure something is there
		poem = file.read()
		if (poem==""):
			return False

		#choose the fonts
		fntname = get_font()
		fnt = ImageFont.truetype(FONTS_PATH + fntname, FONT_SIZE)
		fnt_title = ImageFont.truetype(FONTS_PATH + fntname, TITLE_SIZE)
		fnt_credits = ImageFont.truetype(FONTS_PATH + "segoeuil", SMALL_SIZE)
		print ("Font: " + fntname)

		#Resize the image
		img = img.resize((x1,y1))
		img = img.convert("RGBA")

		br = calculate_brightness(img)
		print ("Brightness: ", format(br, '.2f'))

		#add overlay to make it darker
		img = darken(img, 0.50)

		d = ImageDraw.Draw(img)	

		final_poem = add_line_breaks(poem, fnt)

		print (title + '\n' + final_poem)
		dimtit = d.textsize(title, font=fnt_title)
		dimcred = d.textsize(credits, font=fnt_credits)

		#Render the text in the center of the box
		dim = d.textsize(final_poem, font=fnt)
		x2 = dim[0]
		y2 = dim[1]

		#Adapt title font size if title is too large
		if dimtit[0] > x1 * 0.9:
			factor = dimtit[0]/x1
			fnt_title = ImageFont.truetype(FONTS_PATH + fntname, int (TITLE_SIZE * factor))
			dimtit = d.textsize(title, font=fnt_title)
			
		#Adapt font size if poem is too large
		max_poem_height = int(y1 * MAX_POEM_PROPORTION)
		if y2 > max_poem_height:
		  factor = max_poem_height/y2
		  fnt = ImageFont.truetype(FONTS_PATH + fntname, int (FONT_SIZE * factor))
		  print("Font size: ", int(FONT_SIZE * factor))
		  #recalculate text block size
		  dim = d.textsize(final_poem, font=fnt)
		  x2 = dim[0]
		  y2 = dim[1]

		#Print an extra shade block
		print ("Size of poem block: (", max(x2,dimtit[0]), ", ", y2 + dimtit[1], ")")
		br = calculate_brightness(img)
		print ("Brightness: ", format(br, '.2f'))
		if (br > 0.30):
			print("Shading...")
			img = shade_block(img,int(max(x2,dimtit[0])*1.1), int((y2 + FONT_SIZE*3 + dimtit[1])*1.1), int(255 * 0.20))
			
		d = ImageDraw.Draw(img)

		#Determine center of image
		qx = (x1/2 - x2/2)
		qy = (y1/2-y2/2)
		titlex = (x1/2 - dimtit[0]/2)
		titley = qy-FONT_SIZE*3
		creditsx = (x1/2 - dimcred[0]/2)

		#draw title
		d.text ((titlex,titley), title, align="center", font=fnt_title, fill=TEXT_COLOR)

		#draw poem
		d.text((qx,qy), final_poem, align="center", spacing=10, font=fnt, fill=TEXT_COLOR)

		#Footer overlay
		overlay = Image.new('RGBA', img.size, TINT_COLOR+(0,))
		draw = ImageDraw.Draw(overlay)  # Create a context for drawing things on it.
		draw.rectangle(((0, 572), (612, 612)), fill=TINT_COLOR+(OPACITY,))
		img = Image.alpha_composite(img, overlay)

		#Print credits
		d = ImageDraw.Draw(img)
		d.text ((creditsx,582), credits, align="center", font=fnt_credits, fill=(255,255,255))

		#Save the image
		img.convert("RGB")
		stripped_name = poem_file.rsplit("\\",1)[-1]
		saved_filename = IMAGE_PATH + stripped_name[:-4] + '.png'
		img.save(saved_filename)
		print("Saved image as: " + saved_filename)
		#show image
		img.show()

		#move poem to done
		file.close()
		archive(DEFAULT_POEMS_DIR + poem_file)

def main():
	my_poem = Poem()
	my_poem.do_poem()

if __name__ == "__main__":
	main()
	