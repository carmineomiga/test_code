#!/usr/bin/env python
#coding:utf8
import os

#1. 폴더를 탐색한다.
#의문. 폴더 탐색 시, exr과 jpg가 함께 있는 경우
#		이를 구분해야하는가. 한다면 어떻게 해야할까.
def searchItem(root):
	seqs = []
	for subdir in os.listdir(root):
		shot = []
		for f in os.listdir(root+"/"+subdir):
			shot.append("/".join([root,subdir,f]))
		shot.sort()
		seqs.append(shot)
		seqs.sort()
	return seqs

#2.(완성)proxy 파일을 저장할 폴더를 지정한다. 없으면 만든다.
if not os.path.exists("/tmp/project/circle/in"):
	os.makedirs("/tmp/project/circle/in")

#3. exr을 jpg로 만든다.
#convert사용시 shot에서 파일 이름과 확장자를 구분해야할 것 같다.
def genJpg(src, dst):
	src = 
	cmd = "convert %s.exr %s.jpg" % (src, dst)
#	return proxyJpg
	print cmd

#4. jpg를 mov로 만든다.
#def genMov(srcJpg)



#5. jpg를 삭제한다.


#6. 마무리
if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	searchItem(root)
	len(searchItem(root))


	genJpg(src, dst) 
	

#1. proxy 파일을 저장할 폴더를 지정한다. 없으면 만들기
#2. 폴더를 탐색한다. "/project/circle/in/"
#3. exr로 jpg를 만든다.
#4. jpg로 mov를 만든다.
#5. jpg를 삭제한다.
