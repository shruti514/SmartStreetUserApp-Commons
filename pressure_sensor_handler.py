#!/usr/bin/env python
"""
This python program will listen for button press event and take a still image from Raspberry Pi camera
and upload it to twitter site https://twitter.com/sjsucohort6.
"""

import tweepy
from datetime import datetime
from time import sleep
from subprocess import call
from gpiozero import Button
from picamera import PiCamera
import sys

__author__ = "<a href='mailto:watsh.rajneesh@sjsu.edu'>Watsh Rajneesh</a>"
__copyright__ = "Copyright (C) 2016, San Jose State University"

def main():
    """
    Main method.

    :return:
    """
    while True:
        try:
            #curtime, photo_name = click_camera_cli()

            api = init_tweepy_api()

            button = Button(17)
            camera = PiCamera()

            curtime = datetime.now()
            now = curtime.strftime('%Y%m%d-%H%M%S')
            photo_name = now + '.jpg'

            # Take a picture upon button press
            camera.start_preview()
            button.wait_for_press()
            photo_path = '/home/pi/' + photo_name
            camera.capture(photo_path)
            camera.stop_preview()

            # Send the tweet with photo
            status = 'Photo auto-tweet from Smart Tree: ' + curtime.strftime('%Y/%m/%d %H:%M:%S')
            api.update_with_media(photo_path, status=status)
            sleep(10)
            # Delete pic after successful upload
            cleanup_pic(photo_path)
        except:
            # Catch all errors and continue looping
            print "Unexpected error:", sys.exc_info()[0]
            cleanup_pic(photo_path)



def cleanup_pic(photo_path):
    """
    Safe cleanup.. all exceptions ignored.

    :param photo_path:
    :return:
    """
    try:
        cmd = 'rm -rf ' + photo_path
        call([cmd], shell=True)  # delete the photo after upload
    except:
        pass


def init_tweepy_api():
    """
    Initialize the tweepy python API for twitter.
    :return:
    """
    # Consumer keys and access tokens, used for OAuth
    consumer_key = 'yg0hyGLWcp5HiNqfZWplc3Mim'
    consumer_secret = 'bihpPTQKdu35Bo1JCtbD6QTl0uA6OstYUDWV938Z7WKl7aXgwQ'
    access_token = '727364855901130752-GZBC5azG8Bdd15SSCCxQu2aAcpNREim'
    access_token_secret = 'zTPYU04gXTAbLxlUTg971Y5r03etRZJOnQXHJEXlvSd01'
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    return api


def click_camera_cli():
    """
    Shoot photo using cli command raspistill

    :return:
    """
    curtime = datetime.now()
    now = curtime.strftime('%Y%m%d-%H%M%S')
    photo_name = now + '.jpg'
    cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name
    call([cmd], shell=True)  # shoot the photo
    return curtime, photo_name


if __name__ == "__main__":
    main()