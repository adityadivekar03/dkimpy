# dkimpy
Library for ARC mail authentication(Under development for GNU Mailman)

Authenticated Received Chain (ARC) permits an organization which is

creating or handling email to indicate their involvement with the

handling process by adding a cryptographically signed header (or

headers) in a manner analagous to that of DomainKeys Identified Mail

(DKIM).  Assertion of responsibility is validated through a

cryptographic signature and by querying the Signer's domain directly

to retrieve the appropriate public key. Changes in the message which

may break DKIM, may be tracked through the ARC set of headers.

This project involves the use of the pre-existing dkimpy 0.5.6 library to 

generate the ARC Headers since the underlying signing algorithm remains 

similar to a large extent in ARC and DKIM. 

Specifically, it involves modification of the dkimpy0.5.6 python 

library available from PyPi, and hosted at launchpad - 

https://launchpad.net/dkimpy/




