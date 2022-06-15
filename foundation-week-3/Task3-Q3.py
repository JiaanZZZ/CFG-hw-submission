song="You could never know what it's like \n\
Your blood like winter freezes just like ice \n\
And there's a cold lonely light that shines from you \n\
You'll wind up like the wreck you hide behind that mask you use\n\
 \n\
And did you think this fool could never win?\n\
Well look at me, I'm coming back again\n\
I got a taste of love in a simple way\n\
And if you need to know while I'm still standing, you just fade away\n\
 \n\
Don't you know I'm still standing better than I ever did\n\
Looking like a true survivor, feeling like a little kid\n\
I'm still standing after all this time\n\
Picking up the pieces of my life without you on my mind\n\
 \n\
I'm still standing (Yeah, yeah, yeah)\n\
I'm still standing (Yeah, yeah, yeah)\n"

with open('song.txt', 'r+') as poem_file:
	poem_file.write(song)
	data = poem_file.readlines()
	for line in data:
		if 'still' in line:
			print(line)
