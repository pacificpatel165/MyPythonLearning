# Decoding from str to bytes : success and error handling

octets = b'Montr\xe9al'

print(octets.decode('cp1252'))

print(octets.decode('iso8859_7'))

print(octets.decode('koi8_r'))

#print(octets.decode('utf_8')) # The 'utf_8' codec detects that octets is not valid UTF-8, and raises Unicode DecodeError

print(octets.decode('utf_8', errors='replace')) # Using 'replace' error handling, the \xe9 is replaced by “�” (code point U +FFFD), the official Unicode REPLACEMENT CHARACTER intended to represent unknown characters.