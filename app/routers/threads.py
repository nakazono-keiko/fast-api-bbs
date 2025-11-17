from fastapi import APIRouter

router = APIRouter(
    prefix="/threads",
    tags=["Threads"]
)

# まだ何も書かない
# 今後ここに GET /threads, POST /threads 等を追加していく
