---
layout: default
title: Horizon 每日速递
---

# Horizon 每日速递

{% assign posts = site.posts %}
{% assign latest = posts.first %}
{% if latest %}
{{ latest.content }}
{% else %}
*今日暂无内容*
{% endif %}

---

## 历史归档

{% assign archive = posts | offset: 1 | limit: 6 %}
{% if archive.size > 0 %}
<ul>
  {% for post in archive %}
    <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
  {% endfor %}
</ul>
{% else %}
*暂无历史记录*
{% endif %}
