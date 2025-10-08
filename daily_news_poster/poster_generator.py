#!/usr/bin/env python3
"""
海报生成器 - 将JSON数据转换为图片海报
"""

import json
import os
from typing import Dict, List, Any
from PIL import Image, ImageDraw, ImageFont
import textwrap


class PosterGenerator:
    """海报生成器类"""
    
    def __init__(self):
        self.default_font_size = 42
        self.title_font_size = 72
        self.section_font_size = 52
        self.line_spacing = 12
        self.margin = 80
        
        # 默认颜色配置 - 黑色加粗海报风格
        self.title_color = '#000000'
        self.section_color = '#000000'
        self.text_color = '#000000'
        self.section_bg_color = '#F8F9FA'
        self.section_border_color = '#000000'
        self.shadow_color = '#CCCCCC'
        
    def generate(self, input_file: str, output: str, bg_image: str = None,
                 title_color: str = None, section_color: str = None, 
                 text_color: str = None, section_bg_color: str = None,
                 section_border_color: str = None, shadow_color: str = None):
        """
        生成海报
        
        Args:
            input_file: 输入的JSON数据文件路径
            output: 输出文件路径
            bg_image: 背景图片路径 (默认: daily_news_poster/background/white_tech.png)
            title_color: 标题颜色 (默认: #000000)
            section_color: 章节标题颜色 (默认: #000000)
            text_color: 正文颜色 (默认: #000000)
            section_bg_color: 章节背景颜色 (默认: #F8F9FA)
            section_border_color: 章节边框颜色 (默认: #000000)
            shadow_color: 阴影颜色 (默认: #CCCCCC)
        """
        # 设置默认背景图片
        if bg_image is None:
            bg_image = "daily_news_poster/background/template.png"
        
        # 更新颜色配置
        if title_color:
            self.title_color = title_color
        if section_color:
            self.section_color = section_color
        if text_color:
            self.text_color = text_color
        if section_bg_color:
            self.section_bg_color = section_bg_color
        if section_border_color:
            self.section_border_color = section_border_color
        if shadow_color:
            self.shadow_color = shadow_color
        # 读取JSON数据
        data = self._load_json_data(input_file)
        
        # 加载背景图片
        background = self._load_background_image(bg_image)
        
        # 生成海报
        poster = self._create_poster(background, data)
        
        # 保存海报
        self._save_poster(poster, output)
        
        print(f"海报已生成: {output}")
    
    def _load_json_data(self, file_path: str) -> Dict[str, Any]:
        """加载JSON数据"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"找不到文件: {file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON格式错误: {e}")
    
    def _load_background_image(self, image_path: str) -> Image.Image:
        """加载背景图片"""
        try:
            return Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"找不到背景图片: {image_path}")
        except Exception as e:
            raise ValueError(f"无法加载背景图片: {e}")
    
    def _create_poster(self, background: Image.Image, data: Dict[str, Any]) -> Image.Image:
        """创建海报"""
        # 创建画布
        poster = background.copy()
        draw = ImageDraw.Draw(poster)
        
        # 尝试加载中文字体，优先使用内置字体
        try:
            # 优先使用内置的文泉驿微米黑字体（跨平台支持中文）
            font_path = os.path.join(os.path.dirname(__file__), 'fonts', 'wqy-microhei.ttc')
            title_font = ImageFont.truetype(font_path, self.title_font_size)
            section_font = ImageFont.truetype(font_path, self.section_font_size)
            text_font = ImageFont.truetype(font_path, self.default_font_size)
            print("使用内置字体: 文泉驿微米黑")

        except:
            try:
                # 尝试PingFang字体（macOS，支持中文）
                title_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", self.title_font_size)
                section_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", self.section_font_size)
                text_font = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", self.default_font_size)
                print("使用系统字体: PingFang")

            except:
                try:
                    # 尝试Hiragino Sans GB（macOS，支持中文）
                    title_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", self.title_font_size)
                    section_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", self.section_font_size)
                    text_font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", self.default_font_size)
                    print("使用系统字体: Hiragino Sans GB")

                except:
                    try:
                        # 尝试STHeiti Light（华文黑体，支持中文）
                        title_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc", self.title_font_size)
                        section_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc", self.section_font_size)
                        text_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc", self.default_font_size)
                        print("使用系统字体: STHeiti Light")

                    except:
                        try:
                            # 尝试STHeiti Medium（华文黑体，支持中文）
                            title_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", self.title_font_size)
                            section_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", self.section_font_size)
                            text_font = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", self.default_font_size)
                            print("使用系统字体: STHeiti Medium")

                        except:
                            try:
                                # 尝试Arial Unicode MS（支持中文）
                                title_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", self.title_font_size)
                                section_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", self.section_font_size)
                                text_font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", self.default_font_size)
                                print("使用系统字体: Arial Unicode MS")

                            except:
                                # 如果所有字体都加载失败，使用默认字体
                                print("警告: 无法加载中文字体，使用默认字体，可能显示乱码")
                                title_font = ImageFont.load_default()
                                section_font = ImageFont.load_default()
                                text_font = ImageFont.load_default()
        
        # 获取图片尺寸
        width, height = poster.size
        
        # 当前绘制位置
        current_y = self.margin
        
        # 绘制标题 - 海报风格设计
        title = data.get('title', '每日资讯')
        title_bbox = draw.textbbox((0, 0), title, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_height = title_bbox[3] - title_bbox[1]
        title_x = (width - title_width) // 2
        
        # 绘制标题半透明蒙版背景
        bg_padding = 30
        bg_x1 = title_x - bg_padding
        bg_y1 = current_y - bg_padding
        bg_x2 = title_x + title_width + bg_padding
        bg_y2 = current_y + title_height + bg_padding
        
        # 创建半透明蒙版
        mask = Image.new('RGBA', (bg_x2 - bg_x1, bg_y2 - bg_y1), (255, 255, 255, 180))  # 白色半透明
        poster.paste(mask, (bg_x1, bg_y1), mask)
        
        # 绘制标题边框
        draw.rectangle([bg_x1, bg_y1, bg_x2, bg_y2], outline=self.section_border_color, width=4)
        
        # 绘制标题阴影
        draw.text((title_x + 2, current_y + 2), title, fill=self.shadow_color, font=title_font)
        # 绘制主标题
        draw.text((title_x, current_y), title, fill=self.title_color, font=title_font)
        current_y += self.title_font_size + 80
        
        # 绘制各个部分
        keys = data.get('keys', {})
        for section_name, items in keys.items():
            if not items:
                continue
                
            # 绘制章节标题 - 海报风格设计
            section_bbox = draw.textbbox((0, 0), section_name, font=section_font)
            section_width = section_bbox[2] - section_bbox[0]
            section_height = section_bbox[3] - section_bbox[1]
            section_x = (width - section_width) // 2
            
            # 绘制章节标题半透明蒙版背景
            padding = 25
            bg_x1 = section_x - padding
            bg_y1 = current_y - padding
            bg_x2 = section_x + section_width + padding
            bg_y2 = current_y + section_height + padding
            
            # 创建半透明蒙版
            mask = Image.new('RGBA', (bg_x2 - bg_x1, bg_y2 - bg_y1), (255, 255, 255, 160))  # 白色半透明
            poster.paste(mask, (bg_x1, bg_y1), mask)
            
            # 绘制章节标题边框
            draw.rectangle([bg_x1, bg_y1, bg_x2, bg_y2], outline=self.section_border_color, width=3)
            
            # 绘制装饰性线条
            line_y = current_y + section_height + 15
            line_x1 = section_x - padding
            line_x2 = section_x + section_width + padding
            draw.line([(line_x1, line_y), (line_x2, line_y)], fill=self.section_border_color, width=2)
            
            # 绘制章节标题阴影
            draw.text((section_x + 2, current_y + 2), section_name, fill=self.shadow_color, font=section_font)
            # 绘制主章节标题
            draw.text((section_x, current_y), section_name, fill=self.section_color, font=section_font)
            current_y += self.section_font_size + 50
            
            # 绘制章节内容 - 海报风格排版
            for i, item in enumerate(items):
                # 文本换行处理
                max_width = width - 2 * self.margin - 40  # 为项目符号留空间
                wrapped_lines = self._wrap_text(item, text_font, max_width)
                
                # 计算文本区域大小
                text_height = len(wrapped_lines) * (self.default_font_size + self.line_spacing) - self.line_spacing
                text_width = max_width
                
                # 绘制文本半透明蒙版背景
                text_bg_x1 = self.margin + 20
                text_bg_y1 = current_y - 8
                text_bg_x2 = self.margin + 20 + text_width
                text_bg_y2 = current_y + text_height + 8
                
                # 创建半透明蒙版
                mask = Image.new('RGBA', (text_bg_x2 - text_bg_x1, text_bg_y2 - text_bg_y1), (255, 255, 255, 140))  # 白色半透明
                poster.paste(mask, (text_bg_x1, text_bg_y1), mask)
                
                # 绘制项目符号
                bullet_x = self.margin + 20
                bullet_y = current_y + self.default_font_size // 2
                draw.ellipse([bullet_x - 4, bullet_y - 4, bullet_x + 4, bullet_y + 4], fill=self.text_color)
                
                for j, line in enumerate(wrapped_lines):
                    if current_y > height - self.margin - self.default_font_size:
                        break
                    
                    line_bbox = draw.textbbox((0, 0), line, font=text_font)
                    line_width = line_bbox[2] - line_bbox[0]
                    line_x = self.margin + 40  # 左对齐，为项目符号留空间
                    
                    # 绘制文字阴影
                    draw.text((line_x + 1, current_y + 1), line, fill=self.shadow_color, font=text_font)
                    # 绘制主文字
                    draw.text((line_x, current_y), line, fill=self.text_color, font=text_font)
                    current_y += self.default_font_size + self.line_spacing
                
                current_y += 25  # 项目间距
                
                if current_y > height - self.margin:
                    break
            
            current_y += 40  # 章节间距
            
            if current_y > height - self.margin:
                break
        
        return poster
    
    def _wrap_text(self, text: str, font: ImageFont.ImageFont, max_width: int) -> List[str]:
        """文本换行处理"""
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            bbox = font.getbbox(test_line)
            text_width = bbox[2] - bbox[0]
            
            if text_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # 单个词太长，强制换行
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _save_poster(self, poster: Image.Image, output_path: str):
        """保存海报"""
        # 确保输出目录存在
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 保存图片
        poster.save(output_path, 'PNG', quality=95)
