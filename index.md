---
layout: default
title: Calendars Home
---

{% assign baseurl = "https://bjbraams.github.io/calendars" %}

{% assign pagelist = "astro-ph,astro-ph.CO,astro-ph.EP,astro-ph.GA,astro-ph.HE,astro-ph.IM,astro-ph.SR,chem-ph,comp-ph,cond-mat.dis-nn,cond-mat.mes-hall,cond-mat.ml-ml,cond-mat.mtrl-sci,cond-mat.quant-gas,cond-mat.soft,cond-mat.stat-mech,cond-mat.str-el,cond-mat.supr-con,cs.AI,cs.ALA,cs.CC,cs.CE,cs.CG,cs.CL,cs.CR,cs.CS,cs.CV,cs.CY,cs.DB,cs.DC,cs.DM,cs.DS,cs.ET,cs.FL,cs.GR,cs.GT,cs.HC,cs.IR,cs.IT,cs.LG,cs.LO,cs.MA,cs.MS,cs.NA,cs.NE,cs.NI,cs.PF,cs.PL,cs.RO" | split: "," %}

{% comment %} Previously, using the bjb-kw: comp-el,comp-fd,comp-hp,comp-in,comp-ml,comp-na,comp-op,comp-ot,comp-qc,comp-uq,cs-al,cs-lo,cs-op,cs-oh,cs-qc,nuclear,plas-ph,plas-ig,plas-am,plas-pm,plas-ft,stat-th,stat-ml,stat-me,stat-ot,prob,stoch,qchem,qmat,qmol,light,ultrafast,spintronics,tbd {% endcomment %}

## Work in Progress

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({{baseurl}}/{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

## Related

[Relevant Organizations]({{baseurl}}/orgs).
