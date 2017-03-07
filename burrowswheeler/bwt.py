from ukkonen.SuffixTree import SuffixTree
from collections import defaultdict, Counter

class BWT:
	def __init__(self, string, transform=True):
		if transform:
			self.suffixTree = SuffixTree(string)
			self.originalString = string
			self.string = self.suffixTree.burrows_wheeler_transform()
		else:
			self.originalString = self._inverse(string)
			self.string = string
			self.suffixTree = SuffixTree(self.originalString)

		# several preprocessing steps
		self._build_alphabets()
		self._build_count_array()
		self._build_first_occurence_array()

	def _inverse(self, string):
		permutation = sorted((t, i) for i, t in enumerate(string))
		def row(k):
			for _ in string:
				t, k = permutation[k]
				yield t
		
		for i in range(len(string)):
			s = ''.join(row(i))
			if s[-1] == '$':
				return s

	def _build_alphabets(self):
		self.alphabets = set(self.string)

	def _build_count_array(self):
		countDict = Counter()
		self.countArray = defaultdict(list)
		for alphabet in self.alphabets:
			self.countArray[alphabet].append(0)

		for character in self.string:
			countDict[character] += 1
			for alphabet in self.alphabets:
				self.countArray[alphabet].append(countDict[alphabet])

	def _build_first_occurence_array(self):
		countDict = Counter()
		self.firstOccurence = dict()
		for i, character in enumerate(list(sorted(self.string))):
			if countDict[character] == 0:
				self.firstOccurence[character] = i

			countDict[character] += 1

	def search(self, pattern):
		top = 0
		bottom = len(self.string) - 1

		while top <= bottom:
			if pattern:
				pattern, symbol = pattern[:-1], pattern[-1]
				if symbol in self.string[top:bottom+1]:
					top = self.firstOccurence[symbol] + self.countArray[symbol][top]
					bottom = self.firstOccurence[symbol] + self.countArray[symbol][bottom+1] - 1
				else:
					return []
			else:
				suffixArray = self.suffixTree.suffix_array()
				return sorted([suffixArray[i] for i in range(top, bottom+1)])