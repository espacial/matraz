import re

def main():
	image = matraz_svg('MIT', False, False, '10.1234/hola')
	f = open('matraz.svg', 'w')
	f.write(image)
	f.close()

def matraz_svg (license=None, contact=False, documentation=False, doi=None, size='150mm'):
	blocks = []
	with open('svg.cfg', 'r') as f:
		cfg = f.read()
		blocks = re.split (r'<!-- .* -->', cfg)

	image = blocks[0] 
	current_box = 1

	if (license != None):
		image += blocks[current_box] 
		image += 'LICENSE (' + license + ')'
		image += blocks[current_box+1] + blocks[current_box+2]
		current_box = current_box + 3

	if (contact != False):
		image += blocks[current_box] 
		image += "CONTACT INFO"
		image += blocks[current_box+1] + blocks[current_box+2]
		current_box = current_box + 3

	if (documentation != False):
		image += blocks[current_box]
		image += "DOCUMENTATION" 
		image += blocks[current_box+1] + blocks[current_box+2]
		current_box = current_box + 3

	if (doi != None): 
		image += blocks[current_box]
		image += "DOI" 
		image += blocks[current_box+1] + blocks[current_box+2]
		current_box = current_box + 3

	image += blocks[-2] 
	image += blocks[-1]

	return image

if __name__ == "__main__":
    main()

