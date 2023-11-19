# BlogWiz: Your AI-Powered Blog Generator

*Your Ideas, Our Words, Endless Stories.*

## Overview

`BlogWiz` is an AI-powered blog generator that leverages the capabilities of OpenAI's GPT-3.5 Turbo and DALL-E models to craft comprehensive and engaging blog posts. Whether you're looking to explore new topics, enhance your SEO strategy, or captivate your audience with visually appealing thumbnails, BlogWiz is here to assist.

## Modules

### `utils.py`

#### `genrate_blog_post(title: str) -> str`

This function generates a comprehensive blog post based on the provided title. It utilizes OpenAI's GPT-3.5 Turbo model to create content that is well-researched, SEO-friendly, and enriched with real-world examples.

#### `extract_titles(blog_post: str) -> list`

Extracts titles from a given blog post. The titles are identified based on Markdown headings (e.g., `#` and `##`).

#### `generate_thumbnail(subject: str, filed: str) -> str`

Generates a visually striking thumbnail image for a blog post using OpenAI's DALL-E model. The prompt for DALL-E is crafted based on the subject and field of the blog post.

#### `generate_title_thumbnail(titles: list, filed: str) -> dict`

Generates thumbnails for a list of blog post titles. The thumbnails are associated with their respective titles.

#### `blog_post_format(blog_post_title: str, filed: list) -> str`

Formats a blog post by incorporating generated thumbnails into the content. The function combines the blog post content, titles, and thumbnails.

### `api.py`

#### `generate(blog_post_title: str, fields: list) -> str`

FastAPI endpoint that receives a blog post title and a list of fields. It then generates and returns the formatted blog post using the `blog_post_format` function from the `utils` module.

## Usage

1. Ensure that you have the necessary environment variables set, including the OpenAI API key.

2. Run the FastAPI server using the provided `api.py` script.

3. Make a POST request to the `/generate` endpoint with the desired blog post title and fields.

Example:
```python
import requests

url = "http://localhost:8000/generate"
data = {
    "blog_post_title": "Artificial Intelligence Advancements",
    "fields": ["AI", "Technology", "Innovation"]
}

response = requests.post(url, json=data)
print(response.text)
```

4. Receive the formatted blog post generated by BlogWiz.
