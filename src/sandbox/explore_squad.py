import sys
from time import time
sys.path.insert(0, "/Users/tom/Dropbox/msc-ml/project/src/")


from helpers import loader, preprocessing

import string

squad =  loader.load_squad_triples('./data/',False,v2=False)

start = time()
max_context_len=0
max_pos = None
debugstr = ""
for i,triple in enumerate(squad):
    filtered,new_pos = preprocessing.filter_context(triple[0], triple[3], 1)

    c_toks=  preprocessing.tokenise(filtered, asbytes=False)
    # context_set = sorted(set(c_toks))
    context_set = c_toks
    if len(context_set) > max_context_len:
        max_context_len = len(context_set)
        max_pos = new_pos
        debugstr = filtered
end = time()
print(end-start)
print(max_context_len," @ ",i)
print(debugstr)
print(len(preprocessing.tokenise(debugstr, asbytes=False)))


# min_pos = 99999999
# num_out=0
# for i,triple in enumerate(squad):
#     if "African blacks and white" in triple[0]:
#         # tokens = preprocessing.tokenise(triple[0], asbytes=False)
#         # tok_pos = preprocessing.char_pos_to_word(triple[0].encode(), tokens, triple[3])
#         # print(tokens[tok_pos])
#         # print(tok_pos)
#         # print(tokens)
#         # print(i,">>>"+triple[0][triple[3]:])
#         print(triple[2])
#         filt, filt_pos = preprocessing.filter_context(triple[0], triple[3], 1)
#         print(filt[filt_pos:filt_pos+10])
#         num_out +=1
#         if num_out >5:
#             exit()
