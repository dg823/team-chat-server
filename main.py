# 메인 실행 파일 (모든 모듈 통합)
from fastapi import FastAPI
import gradio as gr
import sys
import os

# 상대 경로 임포트를 위한 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.routes import router
from ui.app import create_ui

app = FastAPI()

# 백엔드 라우터 등록
app.include_router(router, prefix="/api")

# UI 생성 및 마운트
demo = create_ui()
app = gr.mount_gradio_app(app, demo, path="/")

if __name__ == "__main__":
    import uvicorn
    # 실행 시 터미널에서: python server/12/team_project/main.py
    uvicorn.run(app, host="127.0.0.1", port=8000)
