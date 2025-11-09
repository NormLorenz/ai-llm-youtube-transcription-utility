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

Yes, you can display a **toaster-style notification** in Gradio using the `gr.Notification()` component introduced in Gradio 4.x. It’s perfect for showing brief messages like success alerts, errors, or status updates—similar to toast popups in web apps.

### 🔔 Example: Toaster notification in Gradio

```python
import gradio as gr

def greet(name):
    gr.Notification(f"Hello, {name}!", type="success").show()
    return f"Welcome, {name}!"

with gr.Blocks() as demo:
    name_input = gr.Textbox(label="Enter your name")
    output = gr.Textbox(label="Greeting")
    greet_btn = gr.Button("Greet Me")

    greet_btn.click(fn=greet, inputs=name_input, outputs=output)

demo.launch()
```

### 🛠️ Notification types
You can customize the `type` of notification:
- `"success"` (green)
- `"error"` (red)
- `"warning"` (yellow)
- `"info"` (blue)

### 💡 Notes
- Notifications are ephemeral and appear briefly in the corner.
- You can trigger them inside any function tied to a Gradio event.

Would you like help integrating this into a larger app or customizing the style or behavior?
