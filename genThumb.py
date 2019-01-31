#!/usr/bin/env python
#coding:utf8
import os
import sys
import subprocess

def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exists(src):
		return "", "파일이 존재하지 않습니다."
	if not os.path.isfile(src):
		return "", "파일형태가 아닙니다."
	if not os.path.exists("/usr/bin/convert"):
		return "","ImageMagick이 설치되지 않았습니다."

	d, f = os.path.split(src)
	notuse, ext = os.path.splitext(f)
	dst = d="/"+f.replace(ext, ".jpg")
	size = "360x240"
	cmds = ["convert", src, "-thumbnail", size,
			"-background", "black", "-gravity", "center",
			"-extent", size, dst]
	p = subprocess.Popen(cmds,
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE)
	return p.communicate()

if __name__ == "__main__":
	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
	stdOut, stdErr = genThumb(src)
	if stdErr:
		sys.stderr.write(stdErr)
	sys.stdout.write(stdOut)


# ========== practice2 ==========
#import os
#
#def genThumb(src):
#	"""
#	경로를 입력받으면 썸네일을 만든다.
#	"""
#	# src = source
#	# d = directory
#	# f = filename
#	# ext = 확장자
#	# dst = destination 목적지
#
#	if not  os.path.exists("/usr/bin/convert"):
#		return "ImageMagick이 설치되지 않았습니다."
#
#	d, f = os.path.split(src)
#	notuse, ext = os.path.splitext(f)
#	dst = d="/"+f.replace(ext, ".jpg")
#	cmd = "convert {src} -thumbnail {size} -background black -gravity center -extent {size} {dst}".format(
#		src=src,
#		dst=dst,
#		size="360x240")
#	print cmd
#	#os.system(cmd)
#
#if __name__ == "__main__":
#	src = "/project/circle/in/aces_exr/A003C025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
#	genThumb(src)


# ========== practice1 ==========
#def genThumb(src):
#	"""
#	경로를 입력받으면 썸네일을 만든다.
#	"""
#	size = "360x240"
#	ext = ".jpg"
#	cmd = "convert %s -thumbnail %s -background black -gravity center -extent %s %s" % (target, size, size, result.replace(srcExt,ds)
#
#
#p = "/project/circle/in"
#
#for i in os.listdir(p):
#	for j in os.listdir(p +"/"+i):
#		for k in os.listdir(p+"/"+i+"/"+j):
#			target = "/".join([p, i, j, k])
#			result = "/".join([p, i, j, k.replace(".dpx", ".jpg").replace(".exr", ".jpg")])
#			cmd = "convert %s -thumbnail 360x240 -background black -gravity center -extent 360x240 %s" % (target, result)
#			print target
#			rint result
#			print cmd
#			os.system(cmd)
