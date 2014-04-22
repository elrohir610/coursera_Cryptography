from Crypto.Hash import SHA256

my_file = "6 - 1 - Introduction (11 min).mp4"
#my_file = "6 - 2 - Generic birthday attack (16 min).mp4"
file_array = []

with open(my_file, "rb") as f:
	byte = f.read(1024)
	while byte != "":
		file_array.append(byte)
		byte = f.read(1024)
f.close()

index = len(file_array) -1;
last_hash = ""

while index>=0:
	h = SHA256.new()
	byte = file_array[index]

	if last_hash == "":
		h.update(byte)
	else:
		h.update(byte+last_hash)
	last_hash = h.digest()
	index = index -1

print last_hash.encode("hex")
