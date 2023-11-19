# Import Libraries, and read the key-token
import openai
import os
from dotenv import load_dotenv
import re

_ = load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


def genrate_blog_post(title: str) -> str:
    system_propmt = '''Act as a seasoned AI content creator with a wealth of experience in crafting engaging blog posts. 
    Your task is to create a comprehensive and compelling blog post on a specific topic.

    Instructions:

        Thorough Exploration: Dive deep into the chosen subject, providing an in-depth exploration of the topic.
        SEO Optimization: Apply effective Search Engine Optimization (SEO) techniques to ensure the post is discoverable and indexed by search engines.
        Rich Content: Enrich your writing with real-world examples, case studies, and relevant anecdotes to captivate the audience.
        Engaging Questions: Pose thought-provoking questions throughout the post to stimulate reader interaction and curiosity.

    Output:

        Title: Craft a captivating and SEO-friendly title for the blog post.
        Comprehensive Blog Post: Deliver a complete and detailed blog post that encompasses all aspects of the chosen topic and if it is related to programming provide some simple examples.
        Main Ideas: Present three main ideas within the blog post, each supported by a simple question and answer in an embed way to make reader able to test and solidify it knowledge.
        Conclusion: Summarize the key concepts discussed in the blog post, leaving the reader with a clear understanding of the subject matter.
        notice that output must be written in markdown format.
    '''
    messages = [
        {'role': 'system', 'content': system_propmt},
        {'role': 'user', 'content': title}
    ]
    blog_post = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=0.7,
        max_tokens=1000,
        messages=messages
    )['choices'][0]['message']['content']
    # formated_blog_post = re.sub('[^#+|\*+\s](.+): ', '', blog_post)
    return blog_post


def extract_titles(blog_post: str) -> list:
    titles = re.findall(r'(?:#{1,2}\s|\*+).+: (.+\b)',
                        blog_post, flags=re.MULTILINE)
    return titles


def generate_thumbnail(subject: str, filed: str) -> str:

    img_system_propmt = f'''Craft a versatile and engaging prompt for DALL-E to generate a visually appealing thumbnail image for a blog post.
    The blog post may cover diverse topics in ,{filed}. The generated prompt should inspire an image that captivates the audience's attention, conveys a sense of the post's theme, and encourages exploration.
    It should be concise and short as possible
    '''
    img_user_prompt = f"""As a content creator, I'm seeking a thumbnail image for a blog post.
    The blog post subject is {subject}. 
    I want the generated image to be visually striking and relevant to the overall theme of the post.
    Please provide a versatile and descriptive prompt that I can use with DALL-E to create a compelling thumbnail for this blog post.
    this prompt must be less than 1000 words"""

    img_reqs = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature=0.7,
        max_tokens=1000,
        messages=[
            {'role': 'system', 'content': img_system_propmt},
            {'role': 'user', 'content': img_user_prompt}
        ]

    )['choices'][0]['message']['content']
    img = openai.Image.create(
        prompt=img_reqs, n=1, size='512x512'
    )
    img_url = img['data'][0]['url']
    return img_url


def generate_title_thumbnail(titles: list, filed: str):
    thumbnails = {}
    for title in titles:
        thumbnails[title] = generate_thumbnail(title, filed)
    return thumbnails


def blog_post_format(blog_post_title: str, filed: list):
    blog_post = genrate_blog_post(blog_post_title)
    title = extract_titles(blog_post)[0]
    thums = generate_title_thumbnail(title, filed)
    formatd_blog_post = ''
    for line in blog_post.splitlines():
        for key, value in thums.items():
            if key in line:
                formatd_blog_post += line + f'\n![{key}]({value})'+'\n'
        else:
            formatd_blog_post += line + '\n'
    formatd_blog_post = re.sub('[^#+|\*+\s](.+): ', '', formatd_blog_post)
    return formatd_blog_post
