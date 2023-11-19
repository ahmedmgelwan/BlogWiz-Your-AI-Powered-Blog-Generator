

# BlogWiz: Your AI-Powered Blog Generator

*Your Ideas, Our Words, Endless Stories.*

## Project Overview

**BlogWiz** is an AI-powered blog post generator that empowers users to effortlessly create captivating and comprehensive blog posts on various topics. The system utilizes OpenAI's GPT-3.5 Turbo for natural language generation and DALL-E for thumbnail image creation.

## Usage Instructions

### `utils.py`

#### `genrate_blog_post(title: str) -> str`

Generates a comprehensive blog post based on the provided title using OpenAI's GPT-3.5 Turbo.

#### `extract_titles(blog_post: str) -> list`

Extracts titles from the generated blog post.

#### `generate_thumbnail(subject: str, filed: str) -> str`

Generates a visually appealing thumbnail image for a blog post using DALL-E.

#### `generate_title_thumbnail(titles: list, filed: str) -> dict`

Generates thumbnails for a list of titles and returns a dictionary mapping titles to image URLs.

#### `blog_post_format(blog_post_title: str, filed: list) -> str`

Formats the generated blog post by embedding thumbnails based on titles.

### `api.py`

FastAPI implementation to expose an endpoint for generating formatted blog posts.

```python
from typing import Annotated, Union
from fastapi import FastAPI, Query
from utils import blog_post_format

app = FastAPI(debug=True)

@app.post('/generate')
async def generate(
    blog_post_title: str,
    fields: Annotated[Union[list[str], None], Query()] = None
) -> str:
    blog_post = blog_post_format(blog_post_title, fields)
    return blog_post
```

### `app.py`

Streamlit application for user interaction. Allows users to input blog topic and field, generates, and displays the formatted blog post.

## Getting Started

1. Install the required dependencies: `pip install openai streamlit pyperclip fastapi`.

2. Set up your OpenAI API key and provide it in the `.env` file.

3. Run the Streamlit app: `streamlit run app.py`.

4. Enter the blog topic and field, click "Generate," and explore the generated blog post.

5. Copy, edit, and download the blog post as needed.