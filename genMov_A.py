#!/usr/bin/env python
#coding:utf8
import os

#1. 폴더를 탐색한다.
#의문. 폴더 탐색 시, exr과 jpg가 함께 있는 경우
#		이를 구분해야하는가. 한다면 어떻게 해야할까.
#정확히는 exr파일만을 뽑아 정렬하는 기능의 함수를 만들어보자.

def searchExr():
	result = []
	for root, dirs, files in os.walk(rootPath, topdown=True):
		if root == rootPath:
			continue
		for f in files
			basename, e = os.path.splitext(f)
			if e != ext
				continue
			results.append(f)
			
	

#2. proxy 파일을 저장할 폴더를 지정한다. 없으면 만든다.
def checkProxy(proxyPath):
	if not os.path.exists(proxyPath):
		try:
			os.makedirs(proxyPath)
		except:
			return "폴더를 만들 수 없습니다."
	return None

#3. exr을 jpg로 만든다.
#convert사용시 shot에서 파일 이름과 확장자를 구분해야할 것 같다.




#4. jpg를 mov로 만든다.
#def genMov(srcJpg)



#5. jpg를 삭제한다.




#6. 마무리
if __name__ == "__main__":
	root = "/project/circle/in/aces_exr"
	proxyPath = "/tmp/project/circle/in/aces_exr"
	checkProxy(proxyPath)


