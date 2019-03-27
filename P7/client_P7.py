import requests
import sys
from seq_P7 import Seq

server = "http://rest.ensembl.org/"
ext = "sequence/id/ENSG00000165879?"
PORT = 80

header = {"Content-Type": "application/json", "Accept": "application/json"}

r = requests.get(server + ext, headers=header)

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

sequence = Seq(decoded['seq'])

bases = "A", "C", "T", "G"
percentage_bases = {}
num_of_bases = {}
ttl_length = sequence.len()

# -- doing count and percentage operations
for base in bases:
    percentage_bases.update({base: sequence.percentage(base)})
    num_of_bases.update({base: sequence.count(base)})


# -- calculating the maximum

def element(x):
    return x[1]


maximum_percentage = max(percentage_bases.items(), key=element)

# -- print results
print("Number of bases in FRAT1 gene is {}\n".format(ttl_length))
print("FRAT1 gene is {} T bases in length\n".format(num_of_bases["T"]))
print("The most popular base is {} and his percentage is {}%\n".format(maximum_percentage[0], maximum_percentage[1]))
print("The percentages of all the different bases are{}\n".format(percentage_bases))