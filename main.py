import streamlit as st
from streamlit import session_state as ss
from driver import read_query
import pandas as pd
from rules import rule_1_check

st.set_page_config(page_title="DENT",
                    page_icon=":tooth:",
                    layout='wide')

# st.title("DENTUXO")
def add_item():
    selected_item = ss.selected_item_code
    if "selected_items" not in ss:
        ss["selected_items"] = []
    if selected_item not in ss.selected_items:
        ss.selected_items.append(selected_item)

def remove_item(item):
    ss.selected_items.remove(item)



def check_items():
    
    ss.rule_1_bool, ss.rule_1_text = rule_1_check(codes_list=ss.selected_items)

   




q_df = read_query('MATCH (tt:Treatment) RETURN tt.code as code , tt.name as tt',params={})

# # records = result.records()
# keys = result.keys()
# data = [dict(zip(keys, record)) for record in result]

parsed_dic = q_df.set_index('code').to_dict(orient='dict')

# Sample list of items to select from
codes_dic = parsed_dic['tt']
names_dic = {v: k for k, v in codes_dic.items()}




# Callback function to update code when name changes
def update_code():
    if ss.selected_name != None:
        ss.selected_code = names_dic[ss.selected_name]
        ss.selected_item_code = ss.selected_code


# Callback function to update name when code changes
def update_name():
    if ss.selected_code != None:
        ss.selected_name = codes_dic[ss.selected_code]
        ss.selected_item_code = ss.selected_code



def app():
    st.markdown("<h1 style='text-align: center; color: pink;'>DENTUXO</h1>", unsafe_allow_html=True)

    # col1, col2, col3 = st.columns([1,2,2])
    col1, col2 = st.columns([3,7])

    with col1:
        with st.container():
            
           

            # Selectbox for selecting items
            st.selectbox("Select by name",
                          names_dic.keys(),
                            key='selected_name',
                            index=None,
                            placeholder="Choose an option",
                            on_change=update_code)
            # Selectbox for selecting items
            st.selectbox("Select by code",
                          codes_dic.keys(),
                            key='selected_code',
                            index=None,
                            placeholder="Choose an option",
                            on_change=update_name)

            cols = st.columns([1,1,1])
            with cols[0]:
                # Button to add the selected item
                st.button("Add Item", on_click=add_item)
            with cols[-1]:
                if 'selected_items' in ss:
                    st.button("Submit",
                           on_click=check_items,
                        #    args=ss.selected_items,
                           )
                    

            # Display the selected items in a container with remove buttons
           
            if "selected_items" in ss:
                with st.container(border=True):
                    st.write("##### Selected Items")
                    for item in ss.selected_items:
                        ct_col1,ct_col2= st.columns([10,1])
                        with ct_col1:
                            with st.container(border=True):
                                st.write(item, codes_dic[item])
                        with ct_col2:
                            st.button(f"❌", 
                                  key=f"{item}_remove",
                                    on_click=remove_item,
                                      args=(item,),
                                      use_container_width=True)
            
                        



            



    with col2:
        with st.container(border=True):
            if "analysis_results" in ss:
                if ss.rule_1_bool == False:
                    st.warning("PROBLEMS")
                    st.dataframe(ss.rule_1_text)
    # with col3:
    #     with st.container(border=True):
    #         st.write(ss)


if __name__ == "__main__":
    app()
