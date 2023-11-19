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
