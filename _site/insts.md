<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/style.css">
</head>

# Institute Event Lists

{%for inst in site.data.insts%}
{%if inst.link%}[{{inst.name}}]({{inst.link}}){%else%}{{inst.name}}{%endif%}.
{%if inst.more%} {{inst.more}}.{%endif%}{%if inst.kw%} kw: {{inst.kw}}.{%endif%}
{%endfor%}
