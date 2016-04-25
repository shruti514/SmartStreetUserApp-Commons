from parse_rest.connection import register
from parse_rest.datatypes import Object
import glob
from subprocess import Popen, PIPE
from time import sleep
import datetime


class UserInteraction(Object):
	pass



def main():
	flag=0
	path_to_music="/home/pi/Music/"
	default_music="Toss_the_Feathers.mp3"
	music_to_play=default_music
	last_updated=datetime.datetime.min
	register('pQCx3CjwJTZgOfoWjrkdAGdKqAxBoXJoSVbltkeB', 'iITWf0dW7MbLy3hv5LwgoQaiIEluK5lfh4apdgDr')
	while True:
		sleep(10)
		print "Fetching data...."
		interactions = UserInteraction.Query.all().order_by('-updatedAt').limit(1)
		latest_interaction = interactions[0]
		print latest_interaction.LightSelection, latest_interaction.MusicSelection, latest_interaction.Type, latest_interaction.updatedAt
				
		if(flag == 0):
			print "Creating a player"
			player = Popen(["omxplayer","-o", "local",path_to_music+music_to_play],stdin=PIPE,stdout=PIPE,stderr=PIPE)
			flag=1
		if(latest_interaction.updatedAt!=last_updated):
			print "Recieved new interaction details"
			last_updated = latest_interaction.updatedAt
			if(latest_interaction.Type=='Music'):
				polling_status = player.poll()
				music_to_play = default_music
				if(latest_interaction.MusicSelection == 'Symphony-1'):
					music_to_play = "Happy_Birthday.mp3"
				if(latest_interaction.MusicSelection == 'Symphony-2'):
					music_to_play = "bittersweet_symphony.mp3"
				if(latest_interaction.MusicSelection == 'Symphony-3'):
					music_to_play = "Jingle_bells.mp3"
				if(latest_interaction.MusicSelection == 'Symphony-4'):
					music_to_play = "Game_Of_Thrones.mp3"
				print "**************Updating music***********"
				if(flag == 1 and polling_status!=0):
					print "Stopping music player"
					player.stdin.write("q")
					flag=0
	
				if(flag ==0):
					print "Starting music player "
					player = Popen(["omxplayer","-o", "local",path_to_music+music_to_play],stdin=PIPE,stdout=PIPE,stderr=PIPE)
					flag=1
	
	
if __name__ == "__main__":
    main()
