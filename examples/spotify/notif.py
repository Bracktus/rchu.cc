#!/usr/bin/env python3

#API reference for when you need it 👍
#https://lazka.github.io/pgi-docs/index.html

import gi

gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib, GdkPixbuf

gi.require_version('Notify', '0.7')
from gi.repository import Notify

import requests

player = Playerctl.Player()
manager = Playerctl.PlayerManager()
Notify.init("Now Playing")

def on_metadata(player, metadata, manager):
	if lastTrackID != metadata["mpris:trackid"]:
		#Only trigger on new song
		notify(player)

def notify(player):
	#Getting info (and pic if it exists) and displaying the notification
	global lastTrackID 
	metadata = player.props.metadata
	
	if 'xesam:artist' in metadata.keys() and 'xesam:title' in metadata.keys():
		artist = metadata['xesam:artist'][0]
		title = metadata['xesam:title']
		message = Notify.Notification.new(artist, title)
		message.set_timeout(3500)

	if 'mpris:artUrl' in metadata.keys():
		imageDir = "/home/bracktus/.local/share/icons/cover.jpeg"
		if lastTrackID != metadata["mpris:trackid"]:
			#Don't download image if it's the same picture
			imageUrl = metadata['mpris:artUrl']
			image = requests.get(imageUrl).content
			with open(imageDir, "wb") as writer:
				writer.write(image)
		
		cover = GdkPixbuf.Pixbuf.new_from_file(imageDir)
		message.set_image_from_pixbuf(cover)
	
	lastTrackID = metadata["mpris:trackid"]
	message.show()

def init_player(name):
	#Connecting up the signals and the functions when a player appears
    if name.name in ['ncspot', 'spotifyd']:
        player = Playerctl.Player.new_from_name(name)
        player.connect('metadata', on_metadata, manager)
        manager.manage_player(player)

def on_name_appeared(manager, name):
    init_player(name)

lastTrackID = None
manager.connect('name-appeared', on_name_appeared)

for name in manager.props.player_names:
    init_player(name)

# wait for events
main = GLib.MainLoop()
main.run()