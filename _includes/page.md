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

{% include {{basename}}/highlights.md %}

## Latest Additions

Newly added information is shown here for about two months in reverse order of time of addition.

{% include {{basename}}/new.md %}

## Future Meetings

{% include {{basename}}/future.md %}

## Other Meeting Lists

{% include {{basename}}/lists.md %}

## Selected Serial Meetings

{% include {{basename}}/series.md %}

## Past Meetings

{% include {{basename}}/past.md %}
