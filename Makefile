
init:
	# https://github.com/ekalinin/github-markdown-toc
	curl https://raw.githubusercontent.com/ekalinin/github-markdown-toc/master/gh-md-toc -o gh-md-toc
	chmod a+x gh-md-toc
	# ag
	echo "you should install `ag`!"

readme:
	./merge.sh

push:
	./merge.sh
	git add README.md
	git commit -m "do update README.md"
	git push origin master
