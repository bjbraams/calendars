<head>
  <link rel="stylesheet" href="assets/style.css">
  <meta name="google-site-verification" content="-TclahrTImXSL7tMHLFb3wUP8ne2e1MvaT5MyUA5msA" />
</head>

{% assign urlhead = "https://bjbraams.github.io/calendars" %}

{{urlhead}}

{% assign pagelist = "plasma,iongas,atomic,pmi,nuclear,qsd,light,tcs,optim,stats,stoch,bioinsp" | split: "," %}

## Work in Progress

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({{urlhead}}/{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

## Preliminary

[Computational Science for Inverse Problems and Uncertainty Quantification]().

[Not yet categorized]({{urlhead}}/inprogress).

## Related

[Relevant Organizations]({{urlhead}}/orgs).
