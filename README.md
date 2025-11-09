# ai-llm-youtube-transcription-utility

Gradio itself doesn’t directly generate HTML tables as part of its core UI components, but you can absolutely **display HTML tables** within a Gradio interface using the `gr.HTML()` component. This allows you to embed any custom HTML—including tables—into your app.

### ✅ How to show an HTML table in Gradio

Here’s a simple example:

```python
import gradio as gr

html_table = """
<table border="1">
  <tr><th>Name</th><th>Age</th></tr>
  <tr><td>Alice</td><td>30</td></tr>
  <tr><td>Bob</td><td>25</td></tr>
</table>
"""

with gr.Blocks() as demo:
    gr.HTML(html_table)

demo.launch()
```

### 🧠 Bonus: Dynamic HTML table generation

If you want to generate the table dynamically from Python data (like a list of dictionaries or a pandas DataFrame), you can convert it using `.to_html()` or custom string formatting, then pass it to `gr.HTML()`.

Would you like help building a dynamic table from data, or integrating it into a larger Gradio app?
