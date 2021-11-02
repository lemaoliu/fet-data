# Fine-grained Entity Typing without Knowledge Base #

This project releases a pseudo dataset for fine-grained entity typing, which is obtained from unstructured data without any knowledge bases.
For more details about this project, please see our paper [EMNLP 2021](https://2021.aclweb.org/).  



## Data Description ##

### Format ###
The data format is as follows. 

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
key-"tokens" represents the input tokens of the data, and the original sentence can be obtained by splicing with spaces; key-"mentions" stores each mention and its label in the sentence, and each record contains the start and end position of the mention, and the corresponding label.

### Ontology ###
The type ontology in the pseudo data is from the [TexSmart](https://texsmart.qq.com) system and its definition can be found at [ontology](https://ai.tencent.com/ailab/nlp/texsmart/download/texsmart-ont-0.3.0.tar.gz).

## Usage ##
To use the pseudo data for a specific typing task such as FIGER or OntoNotes, one has to map the types in the pseudo data to the types from the specific ontology. 
This can be achieved by the command as follows:

`python data_mapping.py --inp file1 --out file2 --mapping file3`

- file1: the path of input file, i.e., the file of the pseudo data

- file2: the path of output file

- file3: mapping file. For the FIGER task, the mapping file is `mapping_figer.csv` and it is `mapping_onto.csv` for the OntoNotes task. For other tasks, one needs to manually define a similar csv file for ontology mapping. 

### About Test Sets ###
The test datasets (for FIGER and OntoNotes) are not provided in this repo but available at [data](https://github.com/INK-USC/AFET/tree/master/Data).

## Citation ##
If you use the data for research, please cite the following paper:
```
@article{jing2021fine,
  title={Fine-grained Entity Typing without Knowledge Base},
  author={Qian, Jing and Liu, Yibin and Liu, Lemao and Li, Yangming and Jiang, Haiyun and Zhang, Haisong and Shi, Shuming},
  journal={Proceedings of EMNLP},
  year={2021}
}
```

## Contact ##
If you have any questions, please contact ``lemaoliu@GMAIL DOT COM``
