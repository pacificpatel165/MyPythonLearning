# Build a list of Unicode codepoints from a string, take two.

symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)
