<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/style.css">
</head>

# Latest Finds

These events are scheduled to appear on the topical pages soon.

{%for event in site.data.latest%}
{{event.dd}}:
{%if event.link%}[{{event.name}}]({{event.link}}){%else%}{{event.name}}{%endif%},
{{event.loc}}.{%if event.more%} {{event.more}}.{%endif%}{%if event.kw%} kw: {{event.kw}}.{%endif%}

{%endfor%}
