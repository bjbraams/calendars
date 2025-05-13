<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/style.css">
</head>

# Societies' Event Lists

{%for soc in site.data.socs%}
{%if soc.link%}[{{soc.name}}]({{soc.link}}){%else%}{{soc.name}}{%endif%}.
{%if soc.more%} {{soc.more}}.{%endif%}{%if soc.kw%} kw: {{soc.kw}}.{%endif%}
{%endfor%}
