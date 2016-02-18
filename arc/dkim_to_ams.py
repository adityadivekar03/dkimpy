import re
import sys

import dkim

def convert(sig):
	#convert "DKIM-Signature" to "ARC-Message-Signature"
	sub_start = "DKIM-"
	sub_end = "Signature"
	sig = re.sub(r'{}.*?{}'.format(re.escape(sub_start1),re.escape(sub_end1)),'ARC-Message-Signature',sig)

	#remove the 'c' tag
	sub_start = " c="
	sub_end = ";"
	sig = re.sub(r'{}.*?{}'.format(re.escape(sub_start1),re.escape(sub_end1)),'',sig)
	
	#remove the 'i' tag
	sub_start = " i="
	sub_end = ";"
	sig = re.sub(r'{}.*?{}'.format(re.escape(sub_start1),re.escape(sub_end1)),'',sig)
	
	#convert the 'v' tag to the new 'i' tag. Will take the value 1, unless the message has been ARC signed before
	sub_start = " v="
	sub_end = ";"
	sig = re.sub(r'{}.*?{}'.format(re.escape(sub_start2),re.escape(sub_end2)),' i=1;',sig)
	
	return sig