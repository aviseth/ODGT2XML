import json
import numpy as np

with open('annotation_train.odgt', 'r+') as f: #input filename
    datalist = f.readlines()

inputfile = []
inner = {}
for i in np.arange(len(datalist)):
    adata = json.loads(datalist[i])
    gtboxes = adata['gtboxes']
    for gtbox in gtboxes: #Change lines 13 to 27 based on the number of classes you have and their names
        if gtbox['tag']=='person': # here, person = the class name
            inner = {
                    'filename': adata['ID'],
                    'name': 'person',
                    'bndbox': gtbox['vbox']
                }
            inputfile.append(inner)

        if gtbox['tag']=='mask':
            inner = {
                    'filename': adata['ID'],
                    'name': 'mask',
                    'bndbox': gtbox['vbox']
                }
            inputfile.append(inner)

inputfile = json.dumps(inputfile)

with open('COCO_train.json', 'a+') as f: #output file name
    f.write(str(inputfile))
