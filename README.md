# TODO
*  For clearity, rename the models to what they really are called instead of GPT, Claude, Gemini
*  Hook in the toaster
*  Remove unused files in the project (config.py, main.html, main.py, pyproject.toml, requirments.txt un.lock
  
# How do you display an HTML table in Gardio?

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


# Can you display a toaster in Gradio?

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

# How would you prompt a LLM model with a list of Python dictionaries?

### 🧠 General Prompting Strategy

Assume you have an array like this:

```python
data = [
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]
```

### ✍️ Prompting for Different Tasks

#### 1. **Summarization**
```text
Here is a list of people represented as Python dictionaries:
[
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]
Summarize the roles and age ranges of these individuals.
```

#### 2. **Transformation**
```text
Convert the following array of Python dictionaries into a CSV format:
[
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]
```

#### 3. **Filtering or Querying**
```text
From the following list of dictionaries, return only those where age is greater than 30:
[
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]
```

#### 4. **Natural Language Interpretation**
```text
Given this data:
[
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]
Who is the oldest person and what is their role?

```

### ✅ Best Practices

- **Use triple backticks** or brackets to clearly delimit the data.
- **Be explicit** about what you want the model to do with the data.
- **Avoid ambiguity**—LLMs don’t infer intent well from vague prompts.
- **Keep it readable**—formatting matters for comprehension.


# In Python, how do you reference a file called utilities.py which contains several functions in the main.py. Should utilities.py be a class?

Great question, Norm! Here's how to reference `utilities.py` in `main.py`, and whether it should be a class depends on how you're organizing your code.


### 🧩 Referencing `utilities.py` in `main.py`

Assuming both files are in the same directory:

```python
# main.py
import utilities

# Call a function from utilities.py
utilities.some_function()
```

Or, if you want to import specific functions:

```python
from utilities import some_function, another_function

some_function()
```

If `utilities.py` is in a subfolder (e.g., `helpers/utilities.py`), you’ll need an `__init__.py` file in that folder to treat it as a package:

```python
from helpers.utilities import some_function
```

### 🧱 Should `utilities.py` Be a Class?

Not necessarily. Here's a quick guide:

| Use Case | Should You Use a Class? |
|----------|-------------------------|
| Grouping stateless helper functions | ❌ No — use plain functions |
| Managing state or configuration | ✅ Yes — use a class |
| Creating reusable components with methods | ✅ Yes — use a class |
| Just organizing utility logic | ❌ No — modules are fine |

So if `utilities.py` just contains things like `def clean_text()`, `def format_date()`, etc., a module with plain functions is perfect.

# How do I apply css to a Gradio object?

You can apply CSS to a Gradio interface using the `css` parameter in the `gr.Interface()` or `gr.Blocks()` constructor. This allows you to customize the appearance of components like buttons, textboxes, and containers.

### 🎨 Example: Applying CSS in Gradio

```python
import gradio as gr

custom_css = """
#my-button {
  background-color: #4CAF50;
  color: white;
  font-size: 18px;
  padding: 10px 20px;
  border-radius: 8px;
}
"""

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks(css=custom_css) as demo:
    name_input = gr.Textbox(label="Your Name")
    greet_button = gr.Button("Greet", elem_id="my-button")
    output = gr.Textbox(label="Greeting")

    greet_button.click(fn=greet, inputs=name_input, outputs=output)

demo.launch()
```

### 🧩 Key Concepts

- **`elem_id`**: Assigns a unique ID to a component so you can target it with CSS.
- **`css` parameter**: Accepts a string of CSS rules.
- **Scoped styling**: Gradio uses Shadow DOM for some components, so not all global CSS will apply—use `elem_id` or `elem_classes` for precision.

# How do I import a file called utilities.py that exists in the content folder of my Colab project and reference a function called fetch_transcript in main.ipynb

To import a Python file like `utilities.py` from the `content` folder in your Colab project and use its `fetch_transcript` function in `main.ipynb`, follow these steps:

### ✅ Step-by-step setup in `main.ipynb`

1. **Mount your Google Drive (if needed):**
   If your `content` folder is inside Google Drive:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. **Ensure the file is in the correct location:**
   If `utilities.py` is directly in `/content`, you’re good. If it’s in a subfolder like `/content/my_folder`, adjust the path accordingly.

3. **Add the folder to Python’s path (if needed):**
   ```python
   import sys
   sys.path.append('/content')  # or '/content/my_folder' if it's nested
   ```

4. **Import the function:**
   You can now import the function like this:
   ```python
   from utilities import fetch_transcript
   ```

5. **Use the function:**
   ```python
   transcript = fetch_transcript("video_id_or_url")
   print(transcript)
   ```

---

### 🛠️ Troubleshooting tips

- If you get a `ModuleNotFoundError`, double-check the path and filename.
- If the file is in a subfolder, use:
  ```python
  from my_folder.utilities import fetch_transcript
  ```
  and make sure to add `/content/my_folder` to `sys.path`.

# How do I copy HTML in Gradio and put it in the clipboard?

To copy HTML content to the clipboard in a Gradio app, you can use a combination of Gradio's `HTML` component and a bit of JavaScript embedded in the HTML. Here's a simple example:

### ✅ Example: Copy HTML to Clipboard in Gradio

```python
import gradio as gr

html_content = """
<div id="copyTarget">Hello, <strong>Gradio!</strong></div>
<button onclick="copyToClipboard()">Copy HTML</button>
<script>
function copyToClipboard() {
  const target = document.getElementById("copyTarget");
  const html = target.outerHTML;
  navigator.clipboard.writeText(html).then(() => {
    alert("HTML copied to clipboard!");
  });
}
</script>
"""

with gr.Blocks() as demo:
    gr.HTML(html_content)

demo.launch()
```

### 🔍 How It Works
- `#copyTarget` is the HTML element you want to copy.
- `outerHTML` grabs the full HTML string of that element.
- `navigator.clipboard.writeText()` copies it to the clipboard.
- A button triggers the copy action via `onclick`.

### 🛠 Notes
- Clipboard access requires HTTPS or localhost.
- This works in most modern browsers.
- You can customize the copied content (e.g., innerHTML, plain text, etc.).

Would you like help adapting this for a specific use case—like copying Markdown, styled HTML, or user-generated content?


Would you like help verifying the folder structure or testing the import interactively?



