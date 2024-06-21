import streamlit as st
from driver import read_query


st.set_page_config(page_title="DENT",
                    page_icon=":tooth:",
                    layout='wide')

# st.title("DENTUXO")


# st.write(read_query('MATCH (cat:Treatment {code: $code}) RETURN cat',params={'code':'HBGD475'}))

# st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")


# Sample list of items to select from
treat_codes = {"apple": '1', "banana":'2', "grape":'3'}
codes_treat = {v: k for k, v in treat_codes.items()}


def app():
    st.markdown("<h1 style='text-align: center; color: pink;'>DENTUXO</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,2])

    with col1:
        with st.container():
            
            # selected_tt = st.multiselect("Select one or more treatments:", treat)
            # selected_code = st.multiselect("Select one or more codes:", codes)

            selected_tt = st.selectbox("Select one or more treatments:", 
                                       treat_codes.keys(),
                                       index=None,
                                       placeholder="GGGG",
                                       )
            selected_code = st.selectbox("Select one or more codes:", 
                                         codes_treat.keys(),
                                         index=None,
                                         placeholder="GGGG",)
            
            if selected_tt:
                selected_item = selected_tt
            elif selected_code:
                selected_item = treat_codes[selected_code]
            else:
                selected_item = "No item selected"
            
            st.write(selected_item)

            def add_item():
                selected_item = st.session_state.selected_item
                if "selected_items" not in st.session_state:
                    st.session_state["selected_items"] = []
                if selected_item not in st.session_state.selected_items:
                    st.session_state.selected_items.append(selected_item)

            def remove_item(item):
                st.session_state.selected_items.remove(item)

            # Selectbox for selecting items
            st.selectbox("Select an item", treat_codes.keys(), key='selected_item')

            # Button to add the selected item
            st.button("Add Item", on_click=add_item)

            # Display the selected items in a container with remove buttons
            st.write("### Selected Items")
            if "selected_items" in st.session_state:
                for item in st.session_state.selected_items:
                    # st.write(f"{item} ", key=f"{item}_box")
                    st.button(f"Remove {item}", key=f"{item}_remove", on_click=remove_item, args=(item,))


            



    with col2:
        with st.container(border=True):
            st.title("LLL")
    with col3:
        with st.container(border=True):
            st.write('BB')


if __name__ == "__main__":
    app()
