import numpy as np
import pandas as pd 
from vggish_input import *
import matplotlib.pyplot as plt
import os


audio_data_dir = "/data1/mrahman/flusense_data/records"
audio_files = os.listdir(audio_data_dir)

x = wavfile_to_examples(os.path.join(audio_data_dir,audio_files[1]))
plt.imshow(x[0,:,:])