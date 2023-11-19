import streamlit as st
from utils import blog_post_format
import pyperclip  # For copying to clipboard

# Title and Description
st.title("BlogWiz: Your AI-Powered Blog Generator")
st.subheader("Your Ideas, Our Words, Endless Stories.")
# # Sidebar - User Input
with st.sidebar:
    st.header("Blog Post Info")
    blog_topic = st.text_input(
        "Enter Blog Topic", placeholder='Enter your topic you need')
    blog_field = st.multiselect(
        label='Blog Topic Field', placeholder='Enter the field of blog sperated by comma', options=['Computer Science', 'Artificial Intelligence', 'Mathematics', 'Physics', 'Travel', 'Shopping', 'Electronics'])
    gen_btn = st.button('Generate')
if blog_topic and blog_field and gen_btn:
    try:
        with st.spinner('Generating...'):
            if 'blog_post' not in st.session_state:
                st.session_state.blog_post = blog_post_format(
                    blog_topic, blog_field)
            # Display Generated Blog Post
            print(st.session_state.blog_post)
            st.subheader("Generated Blog Post:")
            st.markdown(st.session_state.blog_post)

            if st.button('Copy'):
                pyperclip.copy(st.session_state.blog_post)
                st.success('Text copied successfully!')
            if st.button('Edit', key='eit_btn'):
                st.text_area(label='Generated Blog Post',
                             value=st.session_state.blog_post)

            st.download_button(
                label="Download Blog Post",
                data=st.session_state.blog_post,
                file_name="generated_blog_post.md",
                key="download_btn"
            )

    except:
        st.warning('There is an error')
if 'blog_post' in st.session_state:
    # Display Generated Blog Post
    print(st.session_state.blog_post)
    st.subheader("Generated Blog Post:")
    st.markdown(st.session_state.blog_post)

    if st.button('Copy'):
        pyperclip.copy(st.session_state.blog_post)
        st.success('Text copied successfully!')
    if st.button('Edit', key='eit_btn'):
        st.text_area(label='Generated Blog Post',
                     value=st.session_state.blog_post)

    st.download_button(
        label="Download Blog Post",
        data=st.session_state.blog_post,
        file_name="generated_blog_post.md",blog_post
        key="download_btn"
    )


# Add a footer
st.text("© 2023 BlogWiz. Your Ideas, Our Words, Endless Stories. All Rights Reserved.")
