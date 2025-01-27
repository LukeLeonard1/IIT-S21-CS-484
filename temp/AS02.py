# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 17:48:44 2021

@author: pc
"""

import pandas

ToyAssoc = pandas.read_csv('q2data.csv', delimiter=',')

# Convert the Sale Receipt data to the Item List format
ListItem = ToyAssoc.groupby(['Friend'])['Item'].apply(list).values.tolist()

# Convert the Item List format to the Item Indicator format
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(ListItem).transform(ListItem)
ItemIndicator = pandas.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Find the frequent itemsets
frequent_itemsets = apriori(ItemIndicator, min_support = 0.3, max_len = 2, use_colnames = True)

# Discover the association rules
assoc_rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold = 0.5)