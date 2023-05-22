import glob
from utils import convert_to_spec
import pandas as pd
#df= pd.read_csv("music_data.csv")
#df = df.drop(['path', 'array'], axis=1)

from datasets import load_dataset
new_dict = {'ytid':[], 'file_name':[], 'text': []}

ds = load_dataset("google/MusicCaps")
ds = ds["train"]
for i in range(len(ds)):
    print(i)
    if i == 100:
        break
    ytid = str(ds[i]["ytid"])
    caption= str(ds[i]["caption"])
    filename = str("./music_new_data/"+ytid+".wav")
    image =convert_to_spec(filename)
    image_file = ytid+'.png'
    image.save("./musiccaps/train/"+image_file)
    new_dict['ytid'].append(ytid)
    new_dict['file_name'].append(image_file)
    new_dict['text'].append(caption)
    
new_df = pd.DataFrame(new_dict)
new_df.to_csv("musiccaps/metadata.csv", index=False)
