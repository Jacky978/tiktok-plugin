# TikTok 玩具达人榜 ChatGPT 插件

这是一个基于 FastAPI 的 ChatGPT 插件，用于抓取 TikTok 玩具达人排名数据，数据来源是 noxinfluencer.com。

## 使用方法

- 启动 FastAPI 服务（uvicorn main:app --host 0.0.0.0 --port 10000）
- 访问 API: `/tiktok-toy-influencers`
- 在 ChatGPT 插件商店开发者模式安装插件

## 依赖

- fastapi
- uvicorn
- requests
- beautifulsoup4

## 部署平台

推荐部署到 [Render](https://render.com)

## License

MIT License
