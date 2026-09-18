# Team Project — FastAPI + Gradio Chat Server

FastAPI 백엔드와 Gradio UI를 한 프로세스에 마운트한 간단한 AI 챗봇 서버 팀 프로젝트입니다. Groq의 LLM(`openai/gpt-oss-20b`)으로 대화 응답을 생성합니다.

역할을 나눠 작업했습니다.

- `core/llm.py` — AI 엔지니어 담당: Groq LLM 연동, 대화 히스토리 처리
- `api/routes.py` — 백엔드 개발자 담당: `/api/chat` FastAPI 라우터
- `ui/app.py` — 프론트엔드/UI 개발자 담당: Gradio ChatInterface
- `main.py` — FastAPI 앱에 Gradio UI 마운트, 전체 통합
- `tests/test_api.py` — API 유닛 테스트

## 실행

```bash
pip install -r requirements.txt
```

`.env.example`을 참고해 `.env` 파일에 Groq API 키를 설정합니다.

```
GROQ_API_KEY=gsk_...
```

```bash
python main.py
```

`http://127.0.0.1:8000` 에서 채팅 UI를, `http://127.0.0.1:8000/api/chat` 에서 API를 확인할 수 있습니다.

## 테스트

```bash
pytest tests/test_api.py
```
