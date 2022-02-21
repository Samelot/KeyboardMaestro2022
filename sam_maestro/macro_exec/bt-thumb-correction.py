#!/usr/bin/python3

import sys
import os
import subprocess
import argparse
import glob
import math
import re
import shutil
import codecs

import json
from collections import OrderedDict
import io

home = os.path.dirname(os.path.realpath(__file__))

height = 180
columns = 100
rows = 1
video_data_array = []
yt_video_out = '/tmp/video.mp4'

def move_file(file):
	destination = os.path.expanduser("~/_dev/blendertube.github.io/images/post-content")
	shutil.move(file, destination)

def clean_up_tmp():
	os.remove(yt_video_out)

def get_yt_video_url(file):
	# print(os.path.dirname(file))
	# print(os.path.expanduser("~/_dev/blendertube.github.io/_posts"))
	if os.path.dirname(file) != os.path.expanduser("~/_dev/blendertube.github.io/_posts"):
		return False

	with codecs.open(file, 'r', 'utf-8') as search:
		for line in search:
			try:
				if re.search('video_url:', line):
					video_url = line.rstrip()
				if re.search('video_id:', line):
					video_id = line.rstrip()
			except:
				break
		video_url = video_url.split('video_url:')[1].lstrip()
		video_id = video_id.split('video_id:')[1].lstrip()
	return [video_url, video_id]

# SAM: update
def download_video(url):
	cmd = ['youtube-dl', '-f', '22', '-o', yt_video_out, str(url)]
	
	# download the video
	subprocess.call(cmd)

# SAM: What does this do??
def extract_thumb(file, start):
	print(start)
	file_prefix = '/tmp/'+file+'-thumb'
	file = '/tmp/'+file+'-thumb%02d.jpg'
	count_frames_cmd = """ffmpeg -nostats -i /tmp/video.mp4 -vcodec copy -f rawvideo -y /dev/null 2>&1 | grep frame | awk '{split($0,a,"fps")}END{print a[1]}' | sed 's/.*= *//'"""
	ps = subprocess.Popen(count_frames_cmd, shell=True, stdout=subprocess.PIPE)
	frames = ps.communicate()[0].decode('utf-8').strip()
	nth_frame = math.floor(int(frames) / 100)
	# SAM: use double quotes for these fuckers?	
	extract_frames_cmd = ['ffmpeg', '-loglevel', 'panic', '-y', '-i', '/tmp/video.mp4', '-ss', '0:00:49', '-q:v', '1', '-vf', 'select=not(mod(n\,10))', '-vsync', 'vfr', '-vframes', '20', file]
	subprocess.call(extract_frames_cmd)
	# move_file(file)
	for i in range(1, 21):
		out_file_formatted = str(file_prefix)+"{0:0=2d}.jpg".format(i)
		if os.path.isfile(out_file_formatted):
			move_file(out_file_formatted)
		else:
			print("Failure!")

def check_arg(args=None):	
# https://www.bogotobogo.com/python/python_argparse.php
# Command line options
	parser = argparse.ArgumentParser(description='download video')
	parser.add_argument('-u', '--url',
						help='video url',
						required='True')
	parser.add_argument('-s', '--start',
						help='starting time',
						required='True')	

	results = parser.parse_args(args)
	return (results.url, results.start)

if __name__ == '__main__':
	u, s = check_arg(sys.argv[1:])

	video_data_array = get_yt_video_url(u)
	# exit()

	if video_data_array == False:
		print("finder selection error!")
	else:
		download_video(video_data_array[0]) # pass in url
		extract_thumb(video_data_array[1], s) # pass in id
		clean_up_tmp()