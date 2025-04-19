# Usage 

## `llm.py`

```python
from utils.llm import llm
import os

# create instance with gemini model : gemini-2.5-pro-exp
model = llm()

# optionally use any model from any provider using openai compatible url
model = llm(
    base_url="https://openrouter.ai/api/v1", # openrouter provider url for openai client
    api_key=os.getenv("OPENROUTER_API_KEY"), # openrouter api key
    model="google/gemma-2-9b-it:free", # model name from the provider
    req_per_day= 10000 # custom rate limit (default is 50/day as per gemini)
)

# get response directly 
response = model("What can you do?")

# rate limits are handled with a exponential backoff for 3 retry attempts after which it starts returning `None`
```


## `vis.py`

```python
from utils.vis import svg2pil
import matplotlib.pyplot as plt


svg_code = "<svg .... </svg>"

# convert svg code to PIL Image, returns default_svg if not convertable
img = svg2pil(svg_code)

plt.imshow(img)
```