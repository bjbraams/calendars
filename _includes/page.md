<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="assets/style.css">
</head>

{% assign basename = {{page.name|remove:".md"}} %}

<!-- An html comment -->

{% comment %} A Liquid comment {% endcomment %}

# {{site.data.pages[basename].title}}

{{site.data.pages[basename].excerpt}}

## Contents

- [Highlights](#highlights)
- [Latest Additions to the Calendar](#latest-additions-to-the-calendar)
- [Future and Recent Past Meetings](#future-and-recent-past-meetings)
- [Other Meeting Lists and Calendars](#other-meeting-lists-and-calendars)
- [Archives and Histories of Selected Serial Meetings](#archives-and-histories-of-selected-serial-meetings)
- [Past Meetings by Date](#past-meetings-by-date)

## Highlights

{% include {{basename}}/highlights.md %}

## Latest Additions to the Calendar

Newly added information is shown here for about two months in reverse order of time of addition.

{% include {{basename}}/new.md %}

## Future and Recent Past Meetings

{% include {{basename}}/future.md %}

## Other Meeting Lists and Calendars

## Archives and Histories of Selected Serial Meetings

## Past Meetings by Date

{% include {{basename}}/past.md %}
