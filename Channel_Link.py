import streamlit as st

st.title("YouTube Channel Uploads Playlist Generator")

channel_id = st.text_input("Please Paste Channel ID (Start with UC):")

if channel_id:
    if channel_id.startswith("UC") and len(channel_id) == 24:
        playlist_id = "UU" + channel_id[2:]
        playlist_url = f"https://www.youtube.com/playlist?app=desktop&list={playlist_id}"
        st.success("✅ Link playlist uploads:")
        st.code(playlist_url)
        st.markdown(f"[Open in new tab]({playlist_url})")
    else:
        st.error("❌ Invalid Channel ID.")
