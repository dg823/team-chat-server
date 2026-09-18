# 프론트엔드/UI 개발자 담당 영역
import gradio as gr
import requests

def call_api(msg, hist):
    try:
        # 실제 운영 시 환경변수 등으로 URL 관리
        r = requests.post("http://127.0.0.1:8000/api/chat", json={"message": msg, "history": hist})
        return r.json()["res"]
    except:
        return "API 연결 실패"

def create_ui():
    with gr.Blocks(theme=gr.themes.Soft(), title="Team Project") as demo:
        gr.ChatInterface(
            fn=call_api,
            title="💬 Team Messenger",
            description="AI Project Template"
        )
    return demo
