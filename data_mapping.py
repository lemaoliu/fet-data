import json
from argparse import ArgumentParser
from tqdm import tqdm

arg_parser = ArgumentParser()
arg_parser.add_argument('--inp', type=str)
arg_parser.add_argument('--out', type=str)
arg_parser.add_argument('--mapping', type=str)
args = arg_parser.parse_args()

pseudo_data = args.inp
dev_fet_file = args.out
mapping_file = args.mapping

#pseudo_data = './figer_train.json'
#train_fet_file = './figer_ontoform_v2_train.json'
#dev_fet_file = './figer_ontoform_v2_dev.json'
#mapping_file = './mapping_fig2on.csv'

#total_lines = 5695853
#dev_lines = 0
mapping_dict = {}
with open(mapping_file, 'r', encoding='utf-8') as fr:
    for line in fr.readlines():
        target, source = line.strip().split('\t')
        if source not in mapping_dict:
            mapping_dict[source] = [target]
        else:
            if target not in mapping_dict[source]:
                mapping_dict[source].append(target)

pse_fr = open(pseudo_data, 'r', encoding='utf-8')
fet_fw = open(dev_fet_file, 'w', encoding='utf-8')

line = pse_fr.readline()
#tbar = tqdm(total=total_lines)
tbar = tqdm()
count = 0
while(line!=''):
    line = json.loads(line)
    tokens = line['tokens']
    mentions = line['mentions']
    final_mentions = []
    for m in mentions:
        start, end = m['start'], m['end']
        if(start>=len(tokens)):
            continue
        labels = m['labels']
        final_l = []
        for l in labels:
            if l in mapping_dict:
                for _l in mapping_dict[l]:
                    final_l.append(_l)
        if len(final_l)!=0:
            final_mentions.append({'start':start, 'end':end, 'labels':final_l})
    if len(final_mentions)!=0:
        final_line = {'tokens':tokens, 'mentions':final_mentions}
        final_line = json.dumps(final_line)+'\n'
        fet_fw.write(final_line)
    tbar.update()
    line = pse_fr.readline()
    count+=1
    if count%500==0:
        fet_fw.flush()
pse_fr.close()
fet_fw.close()
