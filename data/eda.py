import pandas as pd
import numpy as np

# --------------------------------------------
# ********** READ DATA INTO PANDAS **********
# --------------------------------------------

train = pd.read_csv('west_nile/input/train.csv')
spray = pd.read_csv('west_nile/input/spray.csv')
weather = pd.read_csv('west_nile/input/weather.csv')

# ----------------------------------
# ******** HELPER FUNCTIONS ********
# ----------------------------------

