{% assign basename = page.path | replace: '/index.md' | '' %}

<!-- An html comment -->

{% comment %} A Liquid comment {% endcomment %}

# {{site.data.pages[basename].title}}

{{site.data.pages[basename].excerpt}}

## Contents

- [Highlights](#highlights)
- [Latest Additions](#latest-additions)
- [Future Meetings](#future-meetings)
- [Other Meeting Lists](#other-meeting-lists)
- [Selected Serial Meetings](#selected-serial-meetings)
- [Past Meetings](#past-meetings)

## Highlights

{% include /{{basename}}/_includes/highlights.md %}

## Latest Additions

Reserved space to show newly added information.

{% include /{{basename}}/_includes/new.md %}

## Future Meetings

{% include /{{basename}}/_includes/future.md %}

## Other Meeting Lists

{% include /{{basename}}/_includes/lists.md %}

## Selected Serial Meetings

{% include /{{basename}}/_includes/series.md %}

## Past Meetings

{% include /{{basename}}/_includes/past.md %}
