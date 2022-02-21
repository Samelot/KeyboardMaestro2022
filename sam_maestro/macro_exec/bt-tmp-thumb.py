#!/usr/bin/python3

# * * * BT_TmpThumb * * *

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
yt_video_out_dir = "/tmp/"

def get_yt_video_url(file):
    if os.path.dirname(file) != os.path.expanduser(
        "~/_dev/blendertube.github.io/_posts"
    ):
        return False

    with codecs.open(file, "r", "utf-8") as search:
        for line in search:
            try:
                if re.search("video_url:", line):
                    video_url = line.rstrip()
                if re.search("video_id:", line):
                    video_id = line.rstrip()
            except:
                break
        video_url = video_url.split("video_url:")[1].lstrip()
        video_id = video_id.split("video_id:")[1].lstrip()
    return [video_url, video_id]

# https://stackoverflow.com/questions/24849998/how-to-catch-exception-output-from-python-subprocess-check-output
# try:
#     result = subprocess.run(download137, shell=True, capture_output=True)
# except subprocess.CalledProcessError as error: 
#     # print(error.decode("utf-8")) 
#     print("shit")      
# except subprocess.CalledProcessError as e:
#     print(e)
#     print("\n\n")
# except Exception as e:
#     print(e.output.decode())
#     print(e)

# try:
#     subprocess.check_output(download137, stderr=STDOUT, shell=True)
# except subprocess.CalledProcessError as error: 
#     print(error) 
#     # log.debug("Command Result: {}".format(error.stdout.decode('utf-8')))
#     print("shit")      
# except subprocess.CalledProcessError as e:
#     print(e)
#     print("\n\n")
# except Exception as e:
#     print(e.output.decode())
#     print(e)

# SAM: write to journal
def download_video(url, id):

    download137 = ["yt-dlp", "-f", "137+bestaudio[ext=m4a]", "-o", yt_video_out_dir+id+".mp4", str(url)]
    download22 = ["yt-dlp", "-f", "22+bestaudio[ext=m4a]", "-o", yt_video_out_dir+id+".mp4", str(url)]

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

# SAM: a lot to figure out here
def extract_thumb(id, start):
    video_file = "/tmp/" + id + ".mp4"
    thumb_file = "/tmp/" + id + "-thumb.jpg"
    count_frames_cmd = """ffmpeg -nostats -i """ + video_file + """ -vcodec copy -f rawvideo -y /dev/null 2>&1 | grep frame | awk '{split($0,a,"fps")}END{print a[1]}' | sed 's/.*= *//'"""
    ps = subprocess.Popen(count_frames_cmd, shell=True, stdout=subprocess.PIPE)
    frames = ps.communicate()[0].decode("utf-8").strip()
    nth_frame = math.floor(int(frames) / 100)
    print("nth frame: " + str(nth_frame))

    # from correction
    # extract_frames_cmd = ['ffmpeg', '-loglevel', 'panic', '-y', '-i', '/tmp/video.mp4', '-ss', '0:00:49', '-q:v', '1', '-vf', 'select=not(mod(n\,10))', '-vsync', 'vfr', '-vframes', '20', file]

    # SAM: use single quotes in python?
    extract_frames_cmd = ["ffmpeg", "-loglevel", "panic", "-y", "-i", video_file, "-ss", start, "-q:v", "1", '-vframes', '1', thumb_file ]
    subprocess.call(extract_frames_cmd)


def check_arg(args=None):

    # https://www.bogotobogo.com/python/python_argparse.php
    # Command line options

    parser = argparse.ArgumentParser(description="download video")
    parser.add_argument('-u', '--url', help='video url', required='True')
    parser.add_argument('-s', '--start', help='starting time', required='True')

    results = parser.parse_args(args)
    return (results.url, results.start)

if __name__ == "__main__":
    # u = check_arg(sys.argv[1:])
    u, s = check_arg(sys.argv[1:])

    video_data_array = get_yt_video_url(u)
    # exit()

    if video_data_array == False:
        print("finder selection error!")
    else:
        download_video(video_data_array[0], video_data_array[1])  # pass in url
        # extract_thumb(video_data_array[1]) # pass in id
        extract_thumb(video_data_array[1], s) # pass in id
