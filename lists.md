<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/style.css">
</head>

# Group or Personal Event Lists

{%for list in site.data.lists%}
{%if list.link%}[{{list.name}}]({{list.link}}){%else%}{{list.name}}{%endif%}.
{%if list.more%} {{list.more}}.{%endif%}{%if list.kw%} kw: {{list.kw}}.{%endif%}
{%endfor%}
