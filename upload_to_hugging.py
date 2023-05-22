from datasets import load_dataset

dataset = load_dataset("musiccaps", data_dir="train")
dataset.push_to_hub("pranked03/musiccaps_spectrogram")
