# Step 2 : Importing Data

import pandas as pd # excel for python
import numpy as np # Statistical analysis data
import matplotlib.pyplot as plt
import seaborn as sns # Statistical data visualization

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print(cancer.keys())
