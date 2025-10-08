# Daily News Poster

每日资讯海报生成器 - 将JSON格式的资讯数据转换为精美的图片海报。

## 功能特性

- 支持从JSON文件读取资讯数据
- 自动将文字内容渲染到背景图片上
- **内置中文字体支持，跨平台兼容** - 使用文泉驿微米黑字体，确保所有平台都能正确显示中文
- 支持中文显示和自动换行
- 使用Fire框架提供友好的命令行接口
- 支持多种输出格式
- 智能半透明蒙版背景，提高文字可读性
- 海报风格设计，专业美观

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本用法

```bash
python -m daily_news_poster generate data.json output.png
```

### 参数说明

- `data.json`: 输入的JSON数据文件路径
- `output.png`: 输出海报文件路径
- `bg_image`: 背景图片路径 (可选，默认使用白色科技背景)

### 使用命名参数

```bash
python -m daily_news_poster generate --input_file data.json --output output.png
```

### 指定自定义背景

```bash
python -m daily_news_poster generate data.json output.png --bg_image daily_news_poster/background/black_tech.png
```

### 自定义颜色配置

```bash
python -m daily_news_poster generate data.json output.png \
  --title_color "#FF6B35" \
  --section_color "#00FF00" \
  --text_color "#FFFF00" \
  --section_bg_color "#1E3A8A" \
  --section_border_color "#3B82F6" \
  --shadow_color "#000000"
```

#### 颜色参数说明

- `--title_color`: 标题颜色 (默认: #000000 黑色加粗)
- `--section_color`: 章节标题颜色 (默认: #000000 黑色加粗)
- `--text_color`: 正文颜色 (默认: #000000 黑色加粗)
- `--section_bg_color`: 章节背景颜色 (默认: #F8F9FA 浅灰色)
- `--section_border_color`: 章节边框颜色 (默认: #000000 黑色)
- `--shadow_color`: 阴影颜色 (默认: #CCCCCC 浅灰色)

## 数据格式

JSON文件应包含以下结构：

```json
{
  "title": "每日AI资讯精华",
  "keys": {
    "最新论文": [
      "论文标题1",
      "论文标题2"
    ],
    "最新模型": [
      "模型名称1",
      "模型名称2"
    ],
    "最新资讯": [
      "资讯内容1",
      "资讯内容2"
    ]
  }
}
```

## 字体支持

本项目内置了**文泉驿微米黑**字体，这是一个优秀的开源中文字体，具有以下特点：

- **跨平台兼容**: 支持 Windows、macOS、Linux 等所有主流操作系统
- **完整中文支持**: 支持简体中文、繁体中文、日文、韩文等多种字符
- **开源免费**: 使用 SIL Open Font License 许可证，可自由使用和分发
- **自动回退**: 如果内置字体加载失败，会自动尝试使用系统字体

### 字体加载优先级

1. **内置字体** (优先): `daily_news_poster/fonts/wqy-microhei.ttc`
2. **系统字体** (回退): PingFang、Hiragino Sans GB、STHeiti 等

## 项目结构

```
daily-news-poster/
├── daily_news_poster/
│   ├── __init__.py
│   ├── __main__.py          # 命令行入口
│   ├── poster_generator.py  # 海报生成核心逻辑
│   ├── fonts/               # 内置字体目录
│   │   └── wqy-microhei.ttc # 文泉驿微米黑字体
│   └── background/
│       ├── white_tech.png   # 默认白色科技背景
│       ├── black_tech.png   # 黑色科技背景
│       └── template.png     # 模板背景
├── data.json                # 示例数据文件
├── requirements.txt         # 依赖包列表
└── README.md               # 项目说明
```

## 跨平台兼容性

本项目经过测试，支持以下操作系统：

- ✅ **macOS** - 完全支持，优先使用内置字体
- ✅ **Windows** - 完全支持，优先使用内置字体
- ✅ **Linux** - 完全支持，优先使用内置字体

### 字体兼容性说明

- **内置字体**: 文泉驿微米黑字体文件已包含在项目中，无需额外安装
- **自动回退**: 如果内置字体加载失败，会自动尝试使用系统字体
- **中文显示**: 确保在所有平台上都能正确显示中文字符

## 技术栈

- Python 3.7+
- Pillow (PIL) - 图像处理
- Fire - 命令行接口
- JSON - 数据格式
- 文泉驿微米黑字体 - 跨平台中文字体支持
