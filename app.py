# 安装依赖包：pip install fastapi==0.115.12 uvicorn==0.34.2 fastapi[standard]
# 开发模式启动：fastapi dev app.py
# 生产模式启动：uvicorn app:app --reload
# 接口访问地址：http://127.0.0.1:8000/docs

# 导入 FastAPI 框架
from fastapi import FastAPI,Query
from typing import Union, Optional, List
# 导入用户模块（注意：当前目录下需要有 user.py 文件）
import user
# 导入 uvicorn ASGI 服务器
import uvicorn

# 创建 FastAPI 应用实例
app = FastAPI(name="FastAPI Demo", 
description="FastAPI 示例项目", 
version="0.0.1", 
title="FastAPI Demo")

# 根路径接口 - 返回欢迎消息
@app.get("/")
async def root():
    return {"message": "Hello World"}

# 主页接口 - 返回欢迎消息
@app.get("/items")
async def items():
    return {"message": "Hello World"}

# 路径参数接口 - 获取指定商品信息
# item_id: 路径参数，表示商品ID
# q: 查询参数，可选，用于搜索过滤
@app.get("/items/{item_id}")
async def path_params(item_id:int, q: Union[str,None] = None):
    return {"item_id": item_id, "q": q}

# 查询参数接口 - 分页查询商品列表
# page_id: 页面大小，默认10条
# page_num: 页码，默认第0页
@app.get("/items")
async def qurey_params(page_id: int=Query(0), page_num: Optional[int] = 0):
    return {"page_id": page_id, "page_num": page_num}

# 请求体接口
# 信息提交接口 - 接收并处理用户提交的信息数据
# POST /info - 接收JSON格式的请求体数据
# info: 请求体参数，字典类型，包含用户提交的信息
@app.post("/info")
async def request_body(info: dict):
    return {"item": info}

# 主程序入口
if __name__ == "__main__":
    # 直接运行方式
    # uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    
    # 推荐的运行方式 - 使用字符串形式指定应用
    # host: 监听地址，127.0.0.1 表示只允许本地访问
    # port: 监听端口，8000
    # reload: 开启热重载，代码修改后自动重启服务
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)