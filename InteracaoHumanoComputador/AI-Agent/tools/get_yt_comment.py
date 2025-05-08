from smolagents.tools import Tool
from youtube_comment_downloader import *

class GetYTCommentTool(Tool):
    name = "get_yt_comment"
    description = "Fetches comments from a YouTube video and returns them as a single string."

    inputs = {
        'link': {
            'type': 'string',
            'description': 'The YouTube video URL'
        },
        'max_comments': {
            'type': 'integer',
            'description': 'The maximum number of comments to retrieve',
            'nullable': True
        }
    }

    output_type = "string"

    def forward(self, link: str, max_comments: int = 50) -> str:
        try:
            downloader = YoutubeCommentDownloader()  # type: ignore
            comments = []
            for comment in downloader.get_comments_from_url(link, sort_by=SORT_BY_POPULAR):  # type: ignore
                comments.append(comment['text'])
                if len(comments) >= max_comments:
                    break
            
            comment_string = "\n".join(comments)
            return f"These are the top {len(comments)} comments from the video:\n{comment_string}"
        except Exception as e:
            return f"Error fetching comments: {str(e)}"
