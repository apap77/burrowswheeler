from burrowswheeler.bwt import BWT

if __name__ == '__main__':
	bwt = BWT('mississippi', transform=True)
	print(bwt.search('issi'))