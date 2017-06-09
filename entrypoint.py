#!/usr/bin/env python
import argparse
from subprocess import call
from os.path import basename
import re
import glob

parser = argparse.ArgumentParser(description='Create HEVC streaming package')
parser.add_argument('sourcefiles', metavar='SRC', nargs='+', help='source media files')

parser.add_argument('--workdir', help='specify a working directory, default is /mnt/')
args = parser.parse_args()

workdir = '/mnt'
if args.workdir:
  workdir = args.workdir

sources = []
sources.extend(args.sourcefiles)

hevcfiles = []
doTranscode = False

if len(sources) < 2:
  # Only one source file specified, assume we also need to transcode
  doTranscode = True

#if not hevc:
#  doTranscode = True

if doTranscode:
  bitrates = ['500k', '800k', '1500k']
  for srcfile in sources:
    for bitrate in bitrates:
      outfile = basename(srcfile).split('.')[0]
      video = ['-c:v', 'libx265', '-preset', 'medium', '-crf', '28', '-b:v', bitrate, '-g', '75', '-keyint_min', '75']
      audio = ['-c:a', 'libfdk_aac', '-b:a', '128k']
      cmdline = []
      cmdline.extend(['ffmpeg', '-i', '%s/%s' % (workdir, srcfile)])
      cmdline.extend(video)
      cmdline.extend(audio)
      outfilepath = '%s/%s-hevc-%s.mp4' % (workdir, outfile, bitrate)
      cmdline.extend([outfilepath])
      call(cmdline)
      hevcfiles.append(outfilepath)
else:
  hevcfiles.extend(sources)  
