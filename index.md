---
layout: default
title: CloudZun 每日速递
---

# CloudZun 每日速递

{% assign posts = site.posts %}
{% assign latest = posts.first %}
{% if latest %}
{{ latest.content }}
{% else %}
*今日暂无内容*
{% endif %}

---

## 历史归档

<ul>
  {% for post in posts offset: 1 limit: 3 %}
    <li><a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a></li>
  {% endfor %}
</ul>
