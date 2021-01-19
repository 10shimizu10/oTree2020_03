from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=0.01, participation_fee=0.5, mturk_hit_settings=dict(title='Simple Ethical Questions (- 8 minutes)', description='It takes about 8 minute.', keywords='bonus, study', frame_height=500, minutes_allotted_per_assignment=60, expiration_hours=168, grant_qualification_id='', qualification_requirements=[{'QualificationTypeId': '00000000000000000071', 'Comparator': 'EqualTo', 'LocaleValues': [{'Country': 'US'}]}, {'QualificationTypeId': '3HK1NS1RTOBWUTRVNOG4T9V4TV5WYU', 'Comparator': 'DoesNotExist'}], template='global/mturk_template.html'))
SESSION_CONFIGS = [dict(name='my_session', num_demo_participants=2, app_sequence=['priming', 'dictator', 'punishing_loving', 'GOD', 'demographic', 'manipulation_check', 'last_page'], my_key=0)]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True
DEMO_PAGE_INTRO_HTML = ''
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']


