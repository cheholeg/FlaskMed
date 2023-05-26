#!/usr/bin/env python
# coding: utf-8

# # Proteomics

# # Libraries to Import

# Be sure to activate the "biopython" conda environment.

# In[1]:


# !jupyter-nbextension enable nglview --py --sys-prefix


# In[3]:


from Bio.PDB import *
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.SeqUtils.ProtParam import ProtParamData
import nglview as nv
import ipywidgets

import warnings
warnings.filterwarnings('ignore')


# # Using the PDB (Protein Data Bank) File Format

# In[4]:


parser = PDBParser()


# In[7]:


structure = parser.get_structure("PHA-L", "proteo/1FAT.pdb")


# In[36]:


view = nv.show_biopython(structure)
view


# # Using the CIF (Crystallographic Information File) File Format

# In[9]:


parser = MMCIFParser()


# In[10]:


structure = parser.get_structure("PHA-L", "proteo/1fat.cif")


# In[11]:


view = nv.show_biopython(structure)
view


# In[12]:


structure2 = parser.get_structure("K", "proteo/6ebk.cif")


# In[13]:


view2 = nv.show_biopython(structure2)
view2


# # Diving into the Header Information

# In[14]:


mmcif_dict = MMCIF2Dict.MMCIF2Dict("proteo/1fat.cif")


# In[15]:


# list(mmcif_dict.keys())


# **What’s the overall layout of a Structure object?**
# 
# The Structure object follows the so-called SMCRA (Structure/Model/Chain/Residue/Atom) architecture :
# 
# - A structure consists of models
# - A model consists of chains
# - A chain consists of residues
# - A residue consists of atoms

# **Accessing Residue Sequence**
# 
# The above molecule has 4 major models, which is represented below when resseq (Residue Sequence) resets for each model.

# In[16]:


# Iterate over all residues in a model
# for model in structure:
#     for residue in model.get_residues():
#         print(residue)


# In[17]:


residues = structure.get_residues() # returns a generator object


# In[18]:


# [item for item in residues]


# In[19]:


res_list = Selection.unfold_entities(structure, "R")


# **Polypeptide Builder**
# 
# Peptides are characterized by start codons, a sequence of length N, and a stop codon, hence why 4 models can be comprised of 7 chains. You can see the 4 major chains comprising the above structure as well as 3 linking chains.

# In[20]:


# Using CA-CA
ppb = CaPPBuilder()
counter = 1
for pp in ppb.build_peptides(structure):
    seq = pp.get_sequence()
    print(f"Sequence: {counter}, Length: {len(seq)}")
    print(seq)
    counter += 1
        
# With our different chains, we can run protein analysis methods from ProteinAnalysis and store the results in a dict.
# 
# Protein scale analysis is omitted due to the number of scales that can be examined for. One should run scale analysis ad hoc as detailed below.

# In[21]:


# Define parser and get structure from file
parser = MMCIFParser()
structure = parser.get_structure("PHA-L", "proteo/1fat.cif")

# Define polypeptide builder
ppb = CaPPBuilder()

# Create empty list for chains
all_seqs = []
counter = 1

# For each polypeptide in the structure, run protein analysis methods and store in dict
with open("proteo.csv", "w") as file:
    file.write(f"Sequence, Length, Molecular Weight, GRAVY" + '\n')
    for pp in ppb.build_peptides(structure):
        seq_info = {}
        seq = pp.get_sequence()
        analyzed_seq = ProteinAnalysis(str(seq)) # needs to be a str

        seq_info['Sequence Number'] = counter # set sequence id
        seq_info['Sequence'] = seq # store Seq() object
        seq_info['Sequence Length'] = len(seq) # length of seq
        seq_info['Molecular Weight'] = round(analyzed_seq.molecular_weight(), 2) # mol weight
        seq_info['GRAVY'] = round(analyzed_seq.gravy(), 4) # average hydrophobicity
        seq_info['Amino Acid Count'] = analyzed_seq.count_amino_acids() # count residues
        seq_info['Amino Acid Percent'] = analyzed_seq.get_amino_acids_percent() # normalized count
        seq_info['Secondary Structure'] = analyzed_seq.secondary_structure_fraction() # helix, turn, sheet
        file.write(f"{counter}, {len(seq)}, {seq_info['Molecular Weight']}, {seq_info['GRAVY']}" + '\n')
        # Update all_seqs list and increase counter
        all_seqs.append(seq_info)
        counter += 1


# Now we have a list of dicts that can be indexed to select information easily. 

# In[22]:


all_seqs[0]['Molecular Weight']


# We can also perform protein analysis ad-hoc from stored sequences in the dict.

# In[23]:


seq1 = all_seqs[0]['Sequence']


# A note here though is that ProteinAnalysis() requires a string of the sequence, not a Seq() object. Biopython has an overloaded str() method that can retrieve the raw string from the Seq() object.  

# In[24]:


analysed_seq = ProteinAnalysis(str(seq1))


# **Molecular Weight**

# In[25]:


analysed_seq.molecular_weight()


# **Gravy**
# 
# > Protein GRAVY returns the GRAVY (grand average of hydropathy) value for the protein sequences you enter. The GRAVY value is calculated by adding the hydropathy value for each residue and dividing by the length of the sequence (Kyte and Doolittle; 1982).
# 
# A higher value is increased hydrophobicity.
# 
# [Source](https://pubmed.ncbi.nlm.nih.gov/7108955/):
# Kyte J, Doolittle RF (May 1983). "A simple method for displaying the hydropathic character of a protein". J. Mol. Biol. 157 (1): 105–32. PMID 7108955

# In[26]:


analysed_seq.gravy()


# **Amino Acid Count**

# In[27]:


analysed_seq.count_amino_acids()


# **Amino Acid Percentage**

# In[28]:


analysed_seq.get_amino_acids_percent()


# **Secondary Structure**
# 
# Returns a tuple of (helix, turn, sheet) percentage. Note that not all residues belong to a secondary structure, hence why the sum(fractions) != 1

# In[29]:


analysed_seq.secondary_structure_fraction() # helix, turn, sheet


# **Protein Scales**

# Scales are located [here](https://github.com/biopython/biopython/blob/master/Bio/SeqUtils/ProtParamData.py#L6).
# 
# - Kyte & Doolittle index of hydrophobicity --> kd
# - Normalized flexibility parameters (B-values), average --> Flex
# - Hydrophilicity --> hw
# - Surface accessibility --> em
# - Janin Interior to surface transfer energy scale --> ja

# In[30]:


analysed_seq.protein_scale(window=7, param_dict=ProtParamData.kd)


# In[31]:


ProtParamData.kd


# In[32]:


# Define parser and get structure from file
parser = MMCIFParser()
structure = parser.get_structure("PHA-L", "proteo/1fat.cif")

# Define polypeptide builder
ppb = CaPPBuilder()

# Create empty list for chains
all_seqs = []
counter = 1

# For each polypeptide in the structure, run protein analysis methods and store in dict
for pp in ppb.build_peptides(structure):
    seq_info = {}
    seq = pp.get_sequence()
    analyzed_seq = ProteinAnalysis(str(seq)) # needs to be a str

    seq_info['Sequence Number'] = counter # set sequence id
    seq_info['Sequence'] = seq # store Seq() object
    seq_info['Sequence Length'] = len(seq) # length of seq
    seq_info['Molecular Weight'] = round(analyzed_seq.molecular_weight(), 2) # mol weight
    seq_info['GRAVY'] = round(analyzed_seq.gravy(), 4) # average hydrophobicity
    seq_info['Amino Acid Count'] = analyzed_seq.count_amino_acids() # count residues
    seq_info['Amino Acid Percent'] = analyzed_seq.get_amino_acids_percent() # normalized count
    seq_info['Secondary Structure'] = analyzed_seq.secondary_structure_fraction() # helix, turn, sheet
    
    # Update all_seqs list and increase counter
    all_seqs.append(seq_info)
    counter += 1


# In[33]:


def analyze_protein(structure):
    all_seqs = []
    counter = 1
    
    # For each polypeptide in the structure, run protein analysis methods and store in dict
    for pp in ppb.build_peptides(structure):
        seq_info = {}
        seq = pp.get_sequence()
        analyzed_seq = ProteinAnalysis(str(seq)) # needs to be a str

        seq_info['Sequence Number'] = counter # set sequence id
        seq_info['Sequence'] = seq # store Seq() object
        seq_info['Sequence Length'] = len(seq) # length of seq
        seq_info['Molecular Weight'] = round(analyzed_seq.molecular_weight(), 2) # mol weight
        seq_info['GRAVY'] = round(analyzed_seq.gravy(), 4) # average hydrophobicity
        seq_info['Amino Acid Count'] = analyzed_seq.count_amino_acids() # count residues
        seq_info['Amino Acid Percent'] = analyzed_seq.get_amino_acids_percent() # normalized count
        seq_info['Secondary Structure'] = analyzed_seq.secondary_structure_fraction() # helix, turn, sheet

        # Update all_seqs list and increase counter
        all_seqs.append(seq_info)
        counter += 1

    return all_seqs


# In[34]:


analyze_protein(structure)


# In[35]:


all_seqs[0]



