from sklearn.datasets import fetch_openml
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

database=fetch_openml(data_id= 43705)
df=pd.DataFrame(database.data,columns=database.feature_names)
encoder=LabelEncoder()
df["ocean_proximity_encod"]=encoder.fit_transform(df["ocean_proximity"])
df.drop(columns=["ocean_proximity"],inplace=True)
sns.pairplot(df,hue="ocean_proximity_encod")
plt.show()
