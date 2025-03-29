import streamlit as st
import requests
import time
from camera_input_live import camera_input_live


st.title("Chat with Cashew!")
image = camera_input_live()

if image:
  st.image(image)
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov"])

if uploaded_file is not None:
    # To read file as bytes:
    video_bytes = uploaded_file.getvalue()
    
    # Show the uploaded video file size (for feedback to user)
    st.write(f"Video file size: {len(video_bytes)} bytes")
    
    # Optionally, you can display the video directly within Streamlit
    st.video(video_bytes)
    
    # If you need to save this video into a variable to use later:
    video_data = video_bytes  # This variable holds the video in byte format
    
    # Additional processing can be done on video_data as needed.
    # For example, saving it to a file on the server:
    with open("uploaded_video.mp4", "wb") as f:
        f.write(video_data)
    st.write("Video submited successfully.")

st.divider()
st.title('Next Step: Wait for the Magic 🪄')

#CHAT##
API_KEY = "02AXxwWKxNdxfkbFKXlUvjW3a6RSiPZWehoVyUS2VosdvAmH20Shbb3qytl88yKY4PyIteFiYyA_warznwwtnBUN5WkV4"
audio_file_path = "./uploaded_video.mp4"

st.subheader("Upload an audio file and get its transcription.")
st.caption('Audio Transcription with Rev.ai')
 
# File uploader widget
audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "mp4"])
 
if audio_file is not None:
    # Show progress bar
    with st.spinner("Uploading and processing the audio..."):
        # Step 1: Upload the audio file to Rev.ai
        files = {'file': audio_file.getvalue()}
        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post("https://api.rev.ai/revvoice/v1beta/jobs", headers=headers, files=files)
 
if audio_file is not None:
    # Show progress bar
    with st.spinner("Uploading and processing the audio..."):
        # Step 1: Upload the audio file to Rev.ai
        try:
            files = {'file': audio_file.getvalue()}  # Convert file to bytes
            headers = {"Authorization": f"Bearer {API_KEY}"}
            response = requests.post("https://api.rev.ai/revvoice/v1beta/jobs", headers=headers, files=files)
            
            if response.status_code == 200:
                job_id = response.json()['id']
                st.success("Audio file uploaded successfully! Processing...")
                
                # Step 2: Poll the status of the transcription job
                status_url = f"https://api.rev.ai/revvoice/v1beta/jobs/{job_id}"
                while True:
                    status_response = requests.get(status_url, headers=headers)
                    status = status_response.json().get('status')
                    
                    if status == 'completed':
                        # Step 3: Fetch the transcription result
                        transcript_url = f"https://api.rev.ai/revvoice/v1beta/jobs/{job_id}/transcript"
                        transcript_response = requests.get(transcript_url, headers=headers)
                        
                        if transcript_response.status_code == 200:
                            transcript = transcript_response.json()['monologues'][0]['elements']
                            transcription_text = ' '.join([element['value'] for element in transcript])
                            st.write("### Transcription:")
                            st.write(transcription_text)
                        else:
                            st.error("Failed to fetch the transcription result.")
                        break
                    
                    elif status == 'failed':
                        st.error("Transcription failed. Please try again.")
                        break
                    else:
                        # Check every 10 seconds for completion
                        time.sleep(10)
                        st.write("Still processing...")

            else:
                st.error(f"Failed to upload the file. Status code: {response.status_code}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")