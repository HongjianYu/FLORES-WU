# %%
import opencc
import re
from tqdm.notebook import tqdm

# %%
lang = "wuu"

# %%
if lang == "mandarin":
  dataset = "zhwiki-20240801-pages-articles-multistream.txt"
  preprocessed = "cmn-wiki.txt"
elif lang == "wu":
  dataset = "wuuwiki-20240801-pages-articles-multistream.txt"
  preprocessed = "wuu-wiki.txt"
elif lang == "yue":
  dataset = "zh_yuewiki-20240801-pages-articles-multistream.txt"
  preprocessed = "yue-wiki.txt"
else:
  print("Options: mandarin, wu, yue")

# %%
ds = open(dataset, 'r')
processed = open(preprocessed, 'w')

l = 0; k = 0; total = 25000
length_threshold = 25
triviality_threshold = 0.25

remove_chars = '#*+=[]&|'
trans_table = str.maketrans('', '', remove_chars)
converter = opencc.OpenCC('t2s.json')

with tqdm(total=total) as pbar:
  while l < total:
    line = ds.readline(); k += 1
    if re.search(r"[a-zA-Z{}\/]", line) is None:
      trans_line = line.translate(trans_table)
      trans_line = re.sub(r'\s+', '', re.sub("'''", "", trans_line))
      if len(trans_line) > length_threshold and \
         len(re.findall(r'[\d%-]', trans_line)) < triviality_threshold * len(trans_line):
        trans_line = converter.convert(trans_line)
        processed.write(trans_line + "\n")
        l += 1; pbar.update(1)

print(f"Finish collation at line {k}")

ds.close()
processed.close()

# %%
