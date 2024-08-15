# %%
import jieba
import opencc
from tqdm.notebook import tqdm

# %%
split = "train"

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
all_out = open("all_out." + split, 'w')

texts = [f.readlines() for f in files]

for line in texts[0]:
  seg_list = jieba.cut(line, cut_all=False)
  segmented = "__label__mandarin " + " ".join(seg_list)
  out[0].write(segmented)
  all_out.write(segmented)

if split == "valid":
  for line in texts[1]:
    seg_list = jieba.cut(converter.convert(line), cut_all=False)
    segmented = "__label__mandarin " + " ".join(seg_list)
    out[0].write(segmented)
    all_out.write(segmented)

for line in texts[-2]:
  seg_list = jieba.cut(line, cut_all=False)
  segmented = "__label__wu " + " ".join(seg_list)
  out[1].write(segmented)
  all_out.write(segmented)

for line in texts[-1]:
  seg_list = jieba.cut(converter.convert(line), cut_all=False)
  segmented = "__label__yue " + " ".join(seg_list)
  out[2].write(segmented)
  all_out.write(segmented)

for f in files:
  f.close()
for f in out:
  f.close()
all_out.close()

# %%
