# imports
from instapy import InstaPy
from instapy import smart_run


# login credentials
insta_username = 'mundo_day_trade'
insta_password = 'insta25a9bs'

comments = ['boa! @{}',
            'perfil top! @{}',
            'Inspiraçao! :thumbsup:',
            'Incrivel! :open_mouth:',
            'Post muito top! @{}',
            'Parece incrivel! @{}']

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["daytrade","mercadofinanceiro","b3", "bolsadevalores", "ibovespa","mercadodeacoes"], amount=10)

    # Joining Engagement Pods
    session.set_do_comment(enabled=True, percentage=1)
    session.set_comments(comments)
    session.join_pods(topic='daytrade', engagement_mode='normal')