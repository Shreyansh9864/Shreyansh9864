import openai
import openai
apikey = "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"
openai_api_key = openai.OpenAI(api_key=apikey)
x=openai_api_key.images.generate(
    prompt="Exploring the transquity of Uttrakhand nature",
    n=1,
    quality="standard",
    model="dall-e-3",
    size="1024x1024",
)
z=image_url = x.data[0].url
from taipy import Gui
page =f"""
<img src="{z}"alt="uk"/>
<h1>Hi</h1>
"""
+++++++++