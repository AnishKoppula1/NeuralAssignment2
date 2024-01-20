inpf = "C:\\Users\\koppu\\OneDrive\\Desktop\\icp2_folder\\input.txt"
with open(inpf,'r') as input_file:
    lines = input_file.readlines()

words_count = []
lin = 1
for line in lines:
    words = line.split()
    words_count.append(len(words))
    print("line " + str(lin) + " : " + str(len(words)))
    lin+=1
cnt = 0
for i in range(len(words_count)):
    cnt += words_count[i]
print("total count : " + str(cnt))
outf = "C:\\Users\\koppu\\OneDrive\\Desktop\\icp2_folder\\output.txt" 
with open(outf, 'w') as output_file:
    for count in words_count:
        output_file.write(f"{count}\n")