#!/usr/bin/env python
#coding:utf8

import os
import subprocess
import sys

def searchExt(rootPath, ext):
	"""
	rootPath 경로에서 ext 확장자를 가진 파일경로를 list로 반환한다.
	"""
	results = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if root == rootPath:
			continue
		for f in files:
			basename, e = os.path.splitext(f)
			if e != ext:
				continue
			results.append("/".join([root]+dirs+[f]))
	return results

def genProxy(files):
	"""
	file 리스트를 받아서 /tmp/proxy에
	프록시 이미지를 생성한다.
	"""
	for src in files:
		p, f = os.path.split(src)
		basename, ext = os.path.splitext(f)
		proxyDir = "/tmp/proxy/" + p
		if not os.path.exists(proxyDir):
			os.makedirs(proxyDir)
		dst = proxyDir + "/" + basename + ".jpg"
		cmds = ["convert", src, dst]
		p = subprocess.Popen(cmds, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		if err:
			sys.stderr.write(err)
		sys.stdout.write(out)

if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	items = searchExt(root, ".exr")
	genProxy(items)
