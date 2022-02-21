# !/usr/bin/python3

import sys
import os
import subprocess
import argparse
import glob
import math
import re
import datetime
import unicodedata
import codecs
import string

import json
from collections import OrderedDict
import io

from os import listdir
from os.path import isfile, join

def check(c):
	# pattern = r'[^\-.#a-z0-9]'
	pattern = r'[^\.#a-z0-9]'
	if re.search(pattern, c):
		return False
	else:
		return c
		
def count_letters(word):
	for i, c in reversed(list(enumerate(word))):
		# print(word[c])
		if check(word[i]):
			# print(i, c)
			return i+1

def normalize_char(c):
	try:
		cname = unicodedata.name(c)
		cname = cname[:cname.index(' WITH')]
		return unicodedata.lookup(cname)
	except (ValueError, KeyError):
		return c

def normalize(s):
	return ''.join(normalize_char(c) for c in s)       

def convert_yt_title(d):
	title = d.replace(' - ', '-')
	title = title.replace(' + ', '+')
	title = title.replace('&', 'and')
	title = title.replace('|', '-')
	title = title.replace(' ', '-')
	title_length = len(title) - 1
	title = ''.join(c for c in title if c.isalnum() or c =='-' or c == '+' or c =='_')
	
	index = count_letters(title)
	title = title[:index] + title[len(title):]

	title = title.lower()
	
	# word = 'hi-i+blender-i:)-:)'
	# index = count_letters(word)
	# print(word[:index] + word[len(word):])

	return title

def convert_yt_date_with_extra_handling(d):
	date = d.split("Premiered ")[1] # handles removal of "Premiered "
	date = d.split("on ")[1] # handles removal of "Streamed live on " and "Published on "
	date = date.replace(',', '')
	month, day, year = date.split(' ')
	yt_months_array = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	# print(day)
	date = datetime.date(int(year),yt_months_array[month],int(day)).strftime('%Y-%m-%d')
	return date

def convert_yt_date(d):
	date = d.replace(',', '')
	month, day, year = date.rsplit(' ', 3)
	yt_months_array = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
	date = datetime.date(int(year),yt_months_array[month],int(day)).strftime('%Y-%m-%d')
	return date

def convert_yt_creator(d):
	# https://stackoverflow.com/questions/8935111/translating-letters-not-in-7bit-ascii-to-ascii-like-%C5%84-to-n-and-%C4%85-to-a
	
	# No long used.. for removing accents in YouTube Creator's names
	# creator = normalize(d)

	creator = d
	return creator

def convert_yt_duration(d):
	int_seconds = int(round(float(d)))
	length = str(datetime.timedelta(seconds=int_seconds))
	return length

'''
Track Height Locking in REAPER
Mar 28, 2018
REAPER Mania
/channel/UCq297H7Ca98HlB5mVFHGSsQ
https://www.youtube.com/watch?v=5P04TvRSwyk
476.801
'''

def convert_yt_uri(d):
	uri = d.split('?v=')
	uri = uri[1].split('&t=')
	uri = 'https://youtu.be/' + uri[0]
	return uri

def handle_video_data(d):
	video_data_array = d.split('\n')

	# use below line to get rid bad characters
	# video_title.decode('utf-8','ignore').encode("utf-8")

	video_title = video_data_array[0]
	video_id = convert_yt_title(video_title)
	video_date = convert_yt_date(video_data_array[1])
	video_creator = convert_yt_creator(video_data_array[2])
	channel_url = video_data_array[3]
	video_url = convert_yt_uri(video_data_array[4])
	video_length = convert_yt_duration(video_data_array[5])
	video_data_array = []
	video_data_array = [video_title, video_id, video_date, video_creator, channel_url, video_url, video_length]
	return video_data_array

def create_new_blog_post(d):
	home = os.path.expanduser("~/_dev/blendertube.github.io/_posts")
	
	new_file = d[2] + "-" + d[1] +  ".md"
	
	blog_post_exists = 0
	blog_posts = [f for f in listdir(home) if isfile(join(home, f)) and f.endswith(".md")]
	for f in blog_posts:
		if f == new_file:
			blog_post_exists = 1

	if blog_post_exists == 0:
		# https://stackoverflow.com/questions/3198765/how-to-write-russian-characters-in-file
		new_blog_post = codecs.open(join(home, new_file), "w", "utf-8")
		new_blog_post.write("---\n")
		new_blog_post.write("layout: blogpost\n")
		new_blog_post.write("category: blog\n")
		new_blog_post.write("video_topic: x\n")
		new_blog_post.write("video_title: " + d[0] + "\n")
		new_blog_post.write("video_id: " + d[1] + "\n")
		new_blog_post.write("video_date: " + d[2] + "\n")
		new_blog_post.write("video_creator: " + d[3] + "\n")
		new_blog_post.write("channel_url: " + d[4] + "\n")
		new_blog_post.write("video_url: " + d[5] + "\n")
		new_blog_post.write("video_length: " + d[6] + "\n")
		new_blog_post.write("language_audio: English\n")
		new_blog_post.write("language_subs: x\n")
		new_blog_post.write("blender_version: 2.78\n")
		new_blog_post.write("tags_software: x\n")
		new_blog_post.write("---\n")
		new_blog_post.close()
		return "creating file... " + join(home, new_file)
	else:
		return "existing file... " + join(home, new_file)

def check_arg(args=None):

# Command line options
# Currently, only the url option is used

	parser = argparse.ArgumentParser(description='download video')
	parser.add_argument('-d', '--data',
						help='video data',
						required='True')

	results = parser.parse_args(args)
	return (results.data)

if __name__ == '__main__':
	data = check_arg(sys.argv[1:])
	new_video_data = handle_video_data(data)
	new_path = create_new_blog_post(new_video_data)
	if new_path:
		print(new_path)
		sys.exit(0)