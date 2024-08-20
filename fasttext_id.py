# %%
import fasttext

# %%
model = fasttext.train_supervised(input="all_out.valid-9", wordNgrams=1,
                                  lr=0.1, epoch=5)
model.save_model("lang.bin")

# %%
print(f"Mandarin accuracy: {model.test("all_out_cmn.valid-1")}")
print(f"Wu accuracy: {model.test("all_out_wuu.valid-1")}")
print(f"Yue accuracy: {model.test("all_out_yue.valid-1")}")
print(f"Overall accuracy: {model.test("all_out.valid-1")}")

# %%
