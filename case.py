# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("persona.csv")


df.shape   #(5000, 5)

df.info()


df.head()

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE":"sum"}).sort_values("PRICE",ascending=False)
agg_df

agg_df = agg_df.reset_index()
agg_df

agg_df["AGE_CUT"] = pd.cut(agg_df.AGE,bins = [0,18,23,30,40,agg_df.AGE.max()],labels=["0_18","19_23","24_30","31_40","41_"+str(agg_df.AGE.max())])


agg_df.head()

agg_df["customers_level_based"] = [col[0].upper() + "_" + col[1].upper() + "_" + col[2].upper() + "_" + col[5].upper() for col in agg_df.values]

agg_df.head()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4 , labels = ["D","C","B","A"])


agg_df = agg_df.reset_index()

# Which segment does a 42 year old Turkish woman using IOS belong to? 

user = "TUR_IOS_FEMALE_41_66"
agg_df[agg_df["customers_level_based"] ==  user ]  #136.0 D


