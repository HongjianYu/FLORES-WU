# %%
import fasttext

# %%
model = fasttext.train_supervised(input="all_out.train", wordNgrams=2,
                                  lr=1.0, epoch=25)
model.save_model("lang.bin")

# %%
print(f"Mandarin accuracy: {model.test("cmn.valid")[1]}")
print(f"Wu accuracy: {model.test("wuu.valid")[1]}")
print(f"Yue accuracy: {model.test("yue.valid")[1]}")
print(f"Overall accuracy: {model.test("all_out.valid")[1]}")

# %%
