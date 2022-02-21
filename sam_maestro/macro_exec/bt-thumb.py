#!/usr/bin/python3

# * * * BT_Thumb * * *

import logging as log
import sys
import os
from subprocess import STDOUT
from subprocess import Popen, PIPE
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

height = 360
columns = 100
rows = 1
video_data_array = []

# global var used in multiple functions
yt_video_out = '/tmp/video.mp4'

def move_file(file):
	destination = os.path.expanduser("~/_dev/blendertube.github.io/images/post-content")
	shutil.copy(file, destination)

def rename_videofile(id):
	destination = '/tmp/' + id + '.mp4'	
	shutil.move(yt_video_out, destination)

# SAM: variable name file --> path ?
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

    download137 = ["yt-dlp", "-f", "137+bestaudio[ext=m4a]", "-o", yt_video_out, str(url)]
    download22 = ["yt-dlp", "-f", "22+bestaudio[ext=m4a]", "-o", yt_video_out, str(url)]

    print("try video format 137...")

    ps137 = subprocess.Popen(download137, stdout=PIPE, stderr=PIPE)
    output, error = ps137.communicate()
    if ps137.returncode == 0:
      print("returncode == 0")
      if "already been downloaded" in output.decode("utf-8"):
        print("file exists")
        return None
      else:
        print("DOWNLOAD FINISHED")
    else:
      print("ERROR")
      if "Requested format is not available" in error.decode("utf-8"):
        print("no available format")

        print("try video format 22...")

        ps22 = subprocess.Popen(download22, stdout=PIPE, stderr=PIPE)
        output, error = ps22.communicate()
        if ps22.returncode == 0:
          print("returncode == 0")
          if "already been downloaded" in output.decode("utf-8"):
            print("file exists")
          else:
            print("DOWNLOAD FINISHED")
        else:
          print("ERROR")
          if "Requested format is not available" in error.decode("utf-8"):
            print("no available format")
          else:
            print("something else")
      else:
        print("something else")

# file --> id
def extract_thumb(file):
	file = '/tmp/'+file+'-thumb.jpg'
	count_frames_cmd = """ffmpeg -nostats -i /tmp/video.mp4 -vcodec copy -f rawvideo -y /dev/null 2>&1 | grep frame | awk '{split($0,a,"fps")}END{print a[1]}' | sed 's/.*= *//'"""
	ps = subprocess.Popen(count_frames_cmd, shell=True, stdout=subprocess.PIPE)
	frames = ps.communicate()[0].decode('utf-8').strip()
	nth_frame = math.floor(int(frames) / 100)
	# print('extract every ' + str(nth_frame) + ' frames')
	print("nth frame: " + str(nth_frame))

	# SAM: use double quotes for these fuckers?
	extract_frames_cmd = ['ffmpeg', '-loglevel', 'panic', '-y', '-i', '/tmp/video.mp4', '-frames', '1', '-q:v', '1', '-vf', 'select=not(mod(n\,'+str(nth_frame)+'))', file]
	subprocess.call(extract_frames_cmd)
	move_file(file)

# select=not(mod(n\,nth_frame)),scale=-1:height,tile=num_columnsxnum_rows
# quotes around -vf's string
# ffmpeg -loglevel panic -y -i /tmp/video.mp4 -frames 1 -q:v 1 -vf 'select=not(mod(n\,12)),scale=-1:180,tile=100x1' /tmp/preview.jpg

def extract_preview(file):
	file = '/tmp/'+file+'-preview.jpg'
	count_frames_cmd = """ffmpeg -nostats -i /tmp/video.mp4 -vcodec copy -f rawvideo -y /dev/null 2>&1 | grep frame | awk '{split($0,a,"fps")}END{print a[1]}' | sed 's/.*= *//'"""
	ps = subprocess.Popen(count_frames_cmd, shell=True, stdout=subprocess.PIPE)
	frames = ps.communicate()[0].decode('utf-8').strip()
	nth_frame = math.floor(int(frames) / 100)
	# print('extract every ' + str(nth_frame) + ' frames')
	extract_frames_cmd = ['ffmpeg', '-loglevel', 'panic', '-y', '-i', '/tmp/video.mp4', '-frames', '1', '-q:v', '1', '-vf', 'select=not(mod(n\,'+str(nth_frame)+')),scale=-1:'+str(height)+',tile='+str(columns)+'x'+str(rows), file]
	subprocess.call(extract_frames_cmd)
	move_file(file)

def check_arg(args=None):

# https://www.bogotobogo.com/python/python_argparse.php
# Command line options

	parser = argparse.ArgumentParser(description='download video')
	parser.add_argument('-u', '--url',
						help='video url',
						required='True')

	results = parser.parse_args(args)
	return (results.url)

if __name__ == '__main__':
	u = check_arg(sys.argv[1:])

	video_data_array = get_yt_video_url(u)
	# exit()

	if video_data_array == False:
		print("finder selection error!")
	else:
		download_video(video_data_array[0]) # pass in url
		extract_preview(video_data_array[1]) # pass in id
		extract_thumb(video_data_array[1]) # pass in id
		rename_videofile(video_data_array[1])