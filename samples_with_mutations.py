#Andrew Shen
import sys
import re

###To run this program, go to the command line and specify four parameters:
###python samples_with_mutations.py (input file 1) (output file)
###For this program, (input file 1) is the file "mutation_sample_data.txt" and the output file is "output_samples_per_gene.txt".

###Sets the input file to the variable "contents".
input_file = sys.argv[1]
read = open(input_file, "r")
contents = read.read()

###Formats the data file into a list of lists with each gene name as the first item and the number of samples with mutations as the second item.
contents_lines = contents.splitlines()
del contents_lines[0]
contents_tab = []
for item in contents_lines:
	contents_tab.append(item.split("\t"))
samples = {}
for item in contents_tab:
	if item[2] not in samples:
		samples[item[2]] = [item[11:26]]
	else:
		samples[item[2]].append(item[11:26])
count = []
for key in samples:
	if key != "PIK3CA":
		count.append([key, samples[key][0]])
	else:
		for item in samples[key][1]:
			samples[key][0].append(item)
		count.append([key, samples[key][0]])
print count;
for item in count:
	item.append(len([x for x in item[1] if x != "."]))
	del item[1]
printed = ""
for item in count:
	printed += item[0] + "\t" + str(item[1]) + "\n"

###Writes to the output file.
output_file = sys.argv[2]
write = open(output_file, "w")
write.write(printed)
write.close()






