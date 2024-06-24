import streamlit as st
import neo4j
import pandas as pd
import re

from driver import read_query








def rule_1_check(codes_list):
    """
    Single act vs Procedure
    """
    rule_1 = """Il peut d'agir d'un Acte ISOLE ou d'une PROCEDURE, c'est-a-dire un ensemble d'actes isoles, realises ensembe. Le practicien doir coder en choisissant 
    la modalite la plus ssimples, la plus complete et la ples synthetique de decription de l'acte realise.
    """
    
    # Define a function to check patterns using regex
    def check_numbers(text):
        if pd.isna(text):
            return None
        elif 'd\'1 dent' in text:
            return 1
        else:
            match = re.search(r' (\d+) dents', text)
            if match:
                # return int(match.group(1))
                return 1 
            else:
                return None

    q = """Match (tt) 
where tt.code IN $codes

with tt
match (tt:Treatment)-[:INSTANCE_OF]->(cat:Treatment_Category)
return tt.code as tt_code, tt.name as tt_name, cat.name as cat_name
"""
    res = read_query(q, params={'codes':codes_list})
    print(res)
    
    #  group by category and leave only the ones with same category
    
    # categories where value_counts is bigger than 1
    # cats = res[res.value_counts>1]
    counts = res.cat_name.value_counts()
    cats = counts[counts>1].index.tolist()

    if len(cats) > 0:

        cats_df = res[res.cat_name.isin(cats)]
        # do new col with boolean if there is mention of number of teeth
        cats_df['numbers'] = cats_df['tt_name'].apply(check_numbers)
        final_cats = cats_df.groupby('cat_name')['cat_name'].count().index.tolist()

        final_df = res[res.cat_name.isin(final_cats)]
        
        # result_dict = {}
        # for cat, group in final_df.groupby('cat'):
        #     result_dict[cat] = group.to_dict(orient='records')

        return False,final_df,rule_1
        
        
    else:

        return True,"No probs", "rule 1 ok"


