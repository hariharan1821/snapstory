import streamlit as st
import Video_summarizer


input_video = st.container()
input_subtitle = st.container()
display_summarized_video = st.container()

with input_video:
    st.title('VIDEO SUMMARIZER')
    video_file = st.file_uploader("Choose a video file", type=["mp4", "webm", "avi", "mov"], key="v1")
    st.video(video_file)

with input_subtitle:
    st.text('Enter the subtitle: ')
    subtitle_file = st.file_uploader("Upload subtitle file", type=["srt"], key="s1")
    

with display_summarized_video:
    if st.button('Summarize video'):
        st.title('SUMMARIZED VIDEO')
        video = Video_summarizer.get_summary(video_file.name, subtitle_file.name)
        st.video("video_file_1.mp4")