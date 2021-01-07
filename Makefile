tar:
	pyinstaller agit.py --onefile
	rm -rf release
	rm -rf release
	mkdir release
	cp dist/agit release
	cp README.md release
	tar zcvf release.tar.gz release
