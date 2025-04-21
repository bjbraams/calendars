{% for event in site.data.latest %}
- dates: {{ event.dates }}, name: {{ event.name }}
{% endfor %}
