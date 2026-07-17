!pip -q install google-genai gradio

from google import genai
import gradio as gr

#gemini API key
client = genai.Client(api_key="")
def review_code(code):
  prompt=f"""
    Reiew this python code
    Provide
    1.Overview
    2.Bugs
    3.Performance Improvments
    4.Code style
    5.Security issues
    6.Improved Code
    7.Rating Issues
    8.Time complexity
    Code:
    {code}
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )

  return response.text

demo=gr.Interface(
    fn=review_code,
    inputs=gr.Textbox(label="Code"),
    outputs="markdown",
    title="AI Code Reviewer (Gemini)"
)
demo.launch()
