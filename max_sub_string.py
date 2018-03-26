# *-* coding:utf-8 *-*

class Solution(object):
'''
找出最长子字符串的长度
例如 输入 abcabcde 则输出 5 >>>>abcde
	输入aaa   则输出1 >>>>>a

思路：
	定义一个dict  用于存储字母最后一次出现的下标
	用start来记录子串的起始值的下标   如果发现有一样的了  start 

'''
	def found_string(self, s):
		result = {}
		start = maxlength = 0
		for i in range(len(s)-1):
			if s[i] in result:
				start = result[s[i]] +1 
			else:
				maxlength = max(maxlength, i-start+1)
			result[s[i]] = i 
		return maxlength 