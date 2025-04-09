<head>
  <link rel="stylesheet" href="assets/style.css">
  <meta name="google-site-verification" content="-TclahrTImXSL7tMHLFb3wUP8ne2e1MvaT5MyUA5msA" />
</head>

{% assign baseurl = https://bjbraams.github.io/calendars/ %}

{% assign pagelist = "plasma,iongas,atomic,pmi,nuclear,qsd,light,tcs,optim,stats,stoch,bioinsp,inprogress" | split: "," %}

## Planned Areas of Mathematical and Physical Science

{% for page in pagelist %}

### [{{site.data.pages[page].title}}]({baseurl}}{{page}})

{{site.data.pages[page].excerpt}}

{% endfor %}

### [Plasma Physics and Fusion Energy]({{baseurl}}plasma).

### [Ionized Gases and Plasma Chemistry]({{baseurl}}iongas).

### [Atomic Processes in Plasmas, Warm and Hot Dense Matter]({{baseurl}}atomic).

### [Plasma-Material Interactions and Related Materials Physics]({{baseurl}}pmi)

### [Nuclear Structure and Reactions]({{baseurl}}nuclear).

[Quantum Structure and Dynamics](https://bjbraams.github.io/calendars/qsd).

[Light Sources and Quantum Optics](https://bjbraams.github.io/calendars/light).

[Theoretical Computer Science, Algorithms, Complexity and Quantum Computing](https://bjbraams.github.io/calendars/tcs).

[Computational Science for Inverse Problems and Uncertainty Quantification]().

[Optimization Theory](optim).

[Statistics and Data Analysis](https://bjbraams.github.io/calendars/stats).

[Stochastics](https://bjbraams.github.io/calendars/stoch).

[Biologically-Inspired Computation](https://bjbraams.github.io/calendars/bioinsp).

[Not yet categorized](https://bjbraams.github.io/calendars/inprogress).

### Related

[Relevant Organizations](https://bjbraams.github.io/calendars/orgs).
