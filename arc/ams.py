import re
import sys

import dkim

def arc_message_sign(message,selector,domain,privkeyfile,identity,):
	
	canonicalize_policy_ams=(b'relaxed',b'relaxed')
	include_headers_ams = (b'message-id',b'date',b'from',b'from',b'to',b'subject',b'subject')
	
	#sign the message
	sig = dkim.sign(message,selector,domain,open(privatekeyfile, "rb").read(),identity = identity
						canonicalize_policy_ams,include_headers_ams)
	
	#convert the sign into an ams	
	ams_sig = convert(sig)
	return ams_sig
