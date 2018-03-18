# Using memoryview and struct to inspect a GIF image header.

import struct
fmt = '<3s3sHH' # struct format: < little-endian; 3s3s two sequences of 3 bytes; HH two 16-bit integers.
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read()) # Create memoryview from file contents in memory...

header = img[:10] # ...then another memoryview by slicing the first one; no bytes are copied here.
print(bytes(header)) # Convert to bytes for display only; 10 bytes are copied here.
print(struct.unpack(fmt, header)) # Unpack memoryview into tuple of: type, version, width and height.
del header # Delete references to release the memory associated with the memoryview instances
del img