import os

def main():
	s_path = input('Ruta a la serie: ')
	os.chdir(s_path)
	seasons = os.listdir('.')

	for s in seasons:
		print(' - {} - '.format(s))
		os.chdir('./'+s)
		epi = os.listdir()
		txt, sub = [], []
		for e in epi:
			if e.lower().endswith('.txt'):
				txt.append(e)
				epi.remove(e)
			elif e.lower().endswith('.srt'):
				sub.append(e)
				epi.remove(e)
			else:
				pass
		renamer(s, txt)
		renamer(s, epi)
		renamer(s, sub)
		os.chdir('..')

def renamer(s, arr):
	for n,el in enumerate(arr):
		if 'txt' not in el[-3:]:
			os.rename(el, '{}E{:0>2d}.{}'.format(s, n+1, el[-3:]))
		else:
			os.rename(el, '{}-{:0>2d}.{}'.format(s, n+1, el[-3:]))

if __name__ == "__main__":
	main()