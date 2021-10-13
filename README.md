# Fine-grained Entity Typing without Knowledge Base #

This section describes the data format of Pseudo Data and how to map it to the format in FIGER or OntoNotes.

## Pseudo Data ##

### Data Format ###
The data format is as follows. key-"tokens" represents the input tokens of the data, and the original sentence can be obtained by splicing with spaces; key-"mentions" stores each mention and its label in the sentence, and each record contains the start and end position of the mention, and the corresponding label.

```json
{
    "tokens":["Apple", "is", "company", "."],
    "mentions":[
        {"start":0, "end":1, "labels":["org.generic", "org.company"]},
        ...
    ],
    ... ...
}
```

### Typing Ontology ###
The type ontology in the pseudo data is from the TexSmart system and its definition can be found at 

## How to use ##
To use the pseudo data for a specific typing task such as FIGER or OntoNotes, one has to map the types in the pseudo data to the types from the specific ontology. 
This can be achieved by the command as follows:

`python data_mapping.py --inp file1 --out file2 --mapping file3`

- file1: the path of input file, i.e., the file of the pseudo data

- file2: the path of output file

- file3: mapping file. For the FIGER task, the mapping file is `mapping_figer.csv` and it is `mapping_onto.csv` for the OntoNotes task. For other tasks, one needs to manually define a similar csv file for ontology mapping. 




