---
layout: default
title: Horizon 每日速递
---

# Horizon 每日速递

AI 驱动的科技新闻聚合

## 历史归档

<ul>
  {% for post in site.posts limit:30 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a>
    </li>
  {% else %}
    <li><em>暂无内容</em></li>
  {% endfor %}
</ul>
