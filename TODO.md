- timezone bug expires current listing a few hours too early

    (gmt v local???)

    [eric has worked on this](https://github.com/cohpy/cohpy.org/pull/40)

- lunch/monthly bug

    "lunch" events never appear

- DRY for entering event info on cohpy.org and meetup.org

    single source will be cohpy.org

    enter events once on cohpy.org,
    which would be posted to both cohpy.org and meetup.com
    with no ugliness
    (instead of scraping meetup.org to copy to cohpy.org)

- pagination of past events

    n events per page,
    instead of all on one monster page

- add a todo list

