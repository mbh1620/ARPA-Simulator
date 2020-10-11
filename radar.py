from RADAR_plotter import *


your_speed = input("Please input your speed: ")
your_heading = input("Please input your heading: ")

game = Pygame_class(1, 2)
plotter = Plotter(your_heading,your_speed)


#your speed, your heading,
# plot 1(time, range and bearing), plot 2(time, range and bearing), plot 3(time, range and bearing)
'''

calculations:
Your Way of Own = (Speed/60)*plot length(time range between first and last plots)
Way of another = (distance/plot length)*60 (Their true speed)

outputs:

True Course of other boat,
True Speed of other boat,
CPA (Closest point of approach)
TCPA (Time closest point of approach)

'''


pygame.init()

screen = pygame.display.set_mode((1200, 1200))


# game.run_loop

plotter.draw(game)

plots = read_in_plots("plots.csv", game)
vessel1 = Vessel(120, 14, plots)
# plots = read_in_plots("plots2.csv", game)
# vessel2 = Vessel(120, 14, plots)
# plots = read_in_plots("plots3.csv", game)
# vessel3 = Vessel(120, 14, plots)


arpa1 = ARPA(plotter, game)

arpa1.calculate_Way_Of_Own(vessel1)
arpa1.calculate_Way_Of_Another(vessel1)
arpa1.calculate_CPA(vessel1)
arpa1.calculate_TCPA(vessel1)
arpa1.text_to_screen(vessel1)

# arpa1.calculate_Way_Of_Own(vessel2)
# arpa1.calculate_Way_Of_Another(vessel2)
# arpa1.calculate_CPA(vessel2)
# arpa1.calculate_TCPA(vessel2)
# arpa1.text_to_screen(vessel2)

# arpa1.calculate_Way_Of_Own(vessel3)
# arpa1.calculate_Way_Of_Another(vessel3)
# arpa1.calculate_CPA(vessel3)
# arpa1.calculate_TCPA(vessel3)
# arpa1.text_to_screen(vessel3)





while True:
	# a = wind((1100,100),10,(180*(2*math.pi))/360).paint()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = 0 

	
	# Clear Screen
	#game.screen.fill((0,0,0))
	
	pygame.display.update()
pygame.quit()
quit()

