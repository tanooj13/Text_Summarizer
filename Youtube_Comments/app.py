from googleapiclient.discovery import build




# Set your API key here
api_key = 'AIzaSyAPosTHM425kWVASQXOMVY9JtV60zW79h8'

# Build a YouTube service object
youtube = build('youtube', 'v3', developerKey=api_key)

def get_video_details(video_id):
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()

    if response['items']:
        stats = response['items'][0]['statistics']
        views = stats.get('viewCount', 'N/A')
        likes = stats.get('likeCount', 'N/A')
        comments = stats.get('commentCount', 'N/A')

        print(f"Views: {views}")
        print(f"Likes: {likes}")
        print(f"Comments: {comments}")
    else:
        print("Video not found")


video_id = link_id # Replace with your YouTube video ID
get_video_details(video_id)