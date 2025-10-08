#!/usr/bin/env python3
"""
Daily News Poster - 每日资讯海报生成器
"""

import fire
from .poster_generator import PosterGenerator


def main():
    """主入口函数"""
    fire.Fire(PosterGenerator)


if __name__ == "__main__":
    main()
