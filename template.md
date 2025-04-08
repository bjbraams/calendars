---
title: Template
name: template
---

<head>
  <link rel="stylesheet" href="assets/style.css">
</head>

# {{ page.title }}

Brief description

## Contents

- [Highlights](#highlights)
- [Latest Additions to the Calendar](#latest-additions-to-the-calendar)
- [Future and Recent Past Meetings](#future-and-recent-past-meetings)
- [Other Meeting Lists and Calendars](#other-meeting-lists-and-calendars)
- [Archives and Histories of Selected Serial Meetings](#archives-and-histories-of-selected-serial-meetings)
- [Past Meetings by Date](#past-meetings-by-date)

## Highlights

Meetings listed in bold in the main section.

## Latest Additions to the Calendar

Newly added information is shown here for about two months in reverse order of time of addition.

## Future and Recent Past Meetings

### {{ site.year0 }}

### {{ site.year0 | plus: 1 }}

{% include {{ page.name }}{{ site:year0 | plus: 1}}.md %}

### {{ site.year0 | plus: 2 }}+

## Other Meeting Lists and Calendars

## Archives and Histories of Selected Serial Meetings

## Past Meetings by Date

### {{ site.year0 | minus: 1 }}-

### {{ site.year0 }}
