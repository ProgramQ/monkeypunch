import score
import fist # that sounds nasty

# were going to have to have to loops, one for the gameplay,
# and one for the shop. If you set up the skeleton for the shop
# I'll do everything else!

shopLoop = False

while shopLoop:
	# fill screen with blue and all shop items
	# once we have the layout the actually code shouldn't
	# be to hard, mainly just changing variables, WITH STYLE!
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()	