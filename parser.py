import os

path = os.getcwd() + '/ChemProt'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for i, f in enumerate(files):
    path2 = f.replace("ChemProt/", "raw/")
    name2 = path2.replace(".tsv", ".txt")
    if not os.path.exists(os.path.dirname(name2)):
        os.makedirs(os.path.dirname(name2))
    
    print (name2 + "\n" )

    file2 = open(name2, "a+")

    k = open(f, "r")
    
    for line in k:
        pubmed_id, text = line.strip().split('	')[:2]
        file2.write(text + "\n")

    file2.close()
