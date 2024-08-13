# %%
import jieba
import opencc
from tqdm.notebook import tqdm

# %%
split = "valid"

# %%
if split == "train":
  datasets = ["cmn-wiki.txt", "wuu-wiki.txt", "yue-wiki.txt"]
elif split == "valid":
  datasets = ["dev.cmn_Hans", "dev.cmn_Hant", "dev.wuu_Hans", "dev.yue_Hant"]
else:
  print("Options: train, valid")

# %%
converter = opencc.OpenCC('t2s.json')

files = [open(ds, 'r') for ds in datasets]
out = [open(lang + '.' + split, 'w') for lang in ["cmn", "wuu", "yue"]]

texts = [f.readlines() for f in files]

for line in texts[0]:
  seg_list = jieba.cut(line, cut_all=False)
  out[0].write("__label__mandarin " + " ".join(seg_list))

if split == "valid":
  for line in texts[1]:
    seg_list = jieba.cut(converter.convert(line), cut_all=False)
    out[0].write("__label__mandarin " + " ".join(seg_list))

for line in texts[-2]:
  seg_list = jieba.cut(line, cut_all=False)
  out[1].write("__label__wu " + " ".join(seg_list))

for line in texts[-1]:
  seg_list = jieba.cut(converter.convert(line), cut_all=False)
  out[2].write("__label__yue " + " ".join(seg_list))

for f in files:
  f.close()
for f in out:
  f.close()

# %%
