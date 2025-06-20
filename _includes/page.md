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

{% include_relative _includes/highlights.md %}

## Latest Additions

Reserved space to show newly added information.

{% include_relative _includes/new.md %}

## Future Meetings

{% comment %} {% include_relative _includes/future.md %} {% endcomment %}

To follow.

## Other Meeting Lists

{% include_relative _includes/lists.md %}

## Selected Serial Meetings

{% include_relative _includes/series.md %}

## Past Meetings

{% comment %} {% include_relative _includes/past.md %} {% endcomment %}

To follow.
