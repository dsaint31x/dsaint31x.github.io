---
layout: archive
title: "Patents"
permalink: /patents/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my patents on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.patents reversed %}
  {% include archive-single.html %}
{% endfor %}
