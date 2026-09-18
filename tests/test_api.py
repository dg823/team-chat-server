# FastAPI 단위 테스트 코드
# 실행 방법: conda activate sv 후 pytest server/12/team_project/tests/test_api.py

import pytest
from fastapi.testclient import TestClient
import sys
import os

# 프로젝트 루트 경로 추가 (main.py가 있는 위치)
# server/12/team_project/tests/test_api.py 기준 두 단계 위
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from main import app
except ImportError:
    # 절대 경로로 시도
    import sys
    sys.path.append("C:/U/server/12/team_project")
    from main import app

client = TestClient(app)

def test_chat_endpoint_success():
    """정상적인 질문에 대한 API 응답 테스트"""
    payload = {
        "message": "안녕, 반가워!",
        "history": []
    }
    # 엔드포인트는 routes.py에서 /chat으로 정의되었고 main.py에서 /api 프리픽스가 붙음
    response = client.post("/api/chat", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "res" in data
    assert isinstance(data["res"], str)

def test_chat_endpoint_invalid_payload():
    """잘못된 형식의 데이터 전송 시 에러 처리 테스트 (Pydantic 검증)"""
    payload = {
        "wrong_field": "test"
    }
    response = client.post("/api/chat", json=payload)
    
    # 필수 필드인 'message'가 없으므로 422 에러 발생 기대
    assert response.status_code == 422

if __name__ == "__main__":
    pytest.main([__file__])
