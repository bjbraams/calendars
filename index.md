<head>
  <link rel="stylesheet" href="assets/style.css">
  <meta name="google-site-verification" content="-TclahrTImXSL7tMHLFb3wUP8ne2e1MvaT5MyUA5msA" />
</head>

{% assign baseurl = "https://bjbraams.github.io/calendars" %}

{% assign pagelist = "comp-in,comp-ml,comp-na,comp-op,comp-qc,comp-uq,cs-al,nuclear,plas-ph,plas-ig,plas-am,plas-pm,stat-th,stat-ml,stat-me,stoch,qchem,qmat,qmol,light,ultrafast,spintronics" | split: "," %}

## Work in Progress

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({{baseurl}}/{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

## Preliminary

[Not yet categorized]({{baseurl}}/inprogress).

## Related

[Relevant Organizations]({{baseurl}}/orgs).
