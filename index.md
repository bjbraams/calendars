---
layout: default
title: Calendars Home
---

{% assign baseurl = "https://bjbraams.github.io/calendars" %}

{% assign pagelist = "astro-ph,astro-ph.CO,astro-ph.EP,astro-ph.GA,astro-ph.HE,astro-ph.IM,astro-ph.SR,cond-mat.dis-nn,cond-mat.mes-hall,cond-mat.ml-ml,cond-mat.mtrl-sci,cond-mat.quant-gas,cond-mat.soft,cond-mat.stat-mech,cond-mat.str-el,cond-mat.supr-con,cs.AI,cs.ALA,cs.CC,cs.CE,cs.CG,cs.CL,cs.CR,cs.CS,cs.CV,cs.CY,cs.DB,cs.DC,cs.DM,cs.DS,cs.ET,cs.FL,cs.GR,cs.GT,cs.HC,cs.IR,cs.IT,cs.LG,cs.LO,cs.MA,cs.MS,cs.NA,cs.NE,cs.NI,cs.PF,cs.PL,cs.RO,cs.SC,cs.SE,cs.SI,cs.SY,econ.EM,eess.IV,eess.SP,eng-geo,hep-ex,hep-ph,hep-th,math.AC,math.AG,math.AP,math.AT,math.CA,math.CO,math.DG,math.DS,math.FA,math.GM,math.GR,math.LO,math.MG,math.NA,math.NT,math.OA,math.OC,math-ph,math.PR,math.RT,math.SP,math.ST,nlin.CD,nucl-ex,nucl-th,physics.acc-ph,physics.ao-ph,physics.app-ph,physics.atm-clus,physics.atom-ph,physics.bio-ph,physics.chem-ph,physics.class-ph,physics.comp-ph,physics.data-an,physics.flu-dyn,physics.geo-ph,physics.hist-ph,physics.ins-det,physics.med-ph,physics.optics,physics.plasm-ph,physics.soc-ph,q-bio.BM,q-bio.GN,q-bio.PE,q-bio.QM,q-fin.CP,q-fin.MF,quant-ph,stat.AP,stat.CO,stat.ME,stat.ML,stat.TH" | split: "," %}

{% comment %} Previously, using the bjb-kw: comp-el,comp-fd,comp-hp,comp-in,comp-ml,comp-na,comp-op,comp-ot,comp-qc,comp-uq,cs-al,cs-lo,cs-op,cs-oh,cs-qc,nuclear,plas-ph,plas-ig,plas-am,plas-pm,plas-ft,stat-th,stat-ml,stat-me,stat-ot,prob,stoch,qchem,qmat,qmol,light,ultrafast,spintronics,tbd {% endcomment %}

## Work in Progress

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({{baseurl}}/{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

## Related

[Relevant Organizations]({{baseurl}}/orgs).
