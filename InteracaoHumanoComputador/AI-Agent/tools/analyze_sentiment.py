from smolagents.tools import Tool
from transformers import pipeline

# Initialize the sentiment analyzer
sentiment_analyzer = pipeline("sentiment-analysis")

class AnalyzeSentimentTool(Tool):
    name = "analyze_sentiment_of_comments"
    description = "Analyzes the sentiment of YouTube comments to determine the overall reception."
    
    inputs = {
        'comments': {
            'type': 'string',
            'description': 'A string containing the YouTube comments'
        }
    }
    
    output_type = "string"

    def forward(self, comments: str) -> str:
        """
        Analyzes the sentiment of YouTube comments to determine the overall reception.
        """
        try:
            comment_list = comments.split("\n")
            sentiments = [sentiment_analyzer(comment)[0] for comment in comment_list if len(comment.strip()) > 0]
            positive_count = sum(1 for sentiment in sentiments if sentiment['label'] == 'POSITIVE')
            negative_count = sum(1 for sentiment in sentiments if sentiment['label'] == 'NEGATIVE')
            if positive_count > negative_count:
                return f"The overall reception is positive. Positive comments: {positive_count}, Negative comments: {negative_count}."
            elif negative_count > positive_count:
                return f"The overall reception is negative. Positive comments: {positive_count}, Negative comments: {negative_count}."
            else:
                return f"The overall reception is neutral. Positive comments: {positive_count}, Negative comments: {negative_count}."
        except Exception as e:
            return f"Error during sentiment analysis: {str(e)}"
