import gradio as gr
from .agent import chat

def start_ui():
    interface = gr.ChatInterface(
        fn = lambda message, history:chat(message, history),
        title = "AI Resume Agent"
    )
    interface.launch()