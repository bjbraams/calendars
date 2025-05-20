---
layout: default
title: Calendars Home
---

{% assign baseurl = "https://bjbraams.github.io/calendars" %}

{% assign pagelist = "comp-el,comp-fd,comp-hp,comp-in,comp-ml,comp-na,comp-op,comp-qc,comp-uq,cs-al,cs-lo,cs-op,cs-oh,cs-qc,nuclear,plas-ph,plas-ig,plas-am,plas-pm,stat-th,stat-ml,stat-me,stat-ot,prob,stoch,qchem,qmat,qmol,light,ultrafast,spintronics,tbd" | split: "," %}

## Work in Progress

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({{baseurl}}/{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

## Related

[Relevant Organizations]({{baseurl}}/orgs).
