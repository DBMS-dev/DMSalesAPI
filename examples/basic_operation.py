from dmsales import DMSalesAPI

api = DMSalesAPI(api_key='your-generated-api-key') # you can generate a new key here https://app.dmsales.com/pl/panel/settings-account?settings=api-configuration

# download list of your projects
projects_list = api.project_list()
print('MY PROJECTS LIST:\n:', projects_list, '\n')

# download list of segments in your project
segments_list = api.segment_list(project_id='paste-here-project-id-from-projects-list')
print('MY SEGMENTS LIST:\n:', segments_list, '\n')

# download list of your contacts in project
contacts = api.persons_list(
    page=1,
    limit=10,
    project_id='paste-here-project-id-from-projects-list'
)
print('MY CONTACTS:\n', contacts, '\n')

# add custom event
response = api.add_custom_event(
    project_id='paste-here-project-id-from-projects-list',
    type='test-event',
    email='paste-here-person-email-from-your-project',
    custom={"test-field": "test-value"}
)
print(f'Custom event response: {response}')

# start validation data
task_id = api.validation_start(
    name='paste-here-name-to-validate',
    phone='paste-here-phone-to-validate',
    postal_code='paste-here-postal-code-to-validate',
    email='paste-here-email-to-validate'
)
print(f'TASK ID:\n', task_id, '\n')

# return validaion report
report = api.validation_report(
    task_id='paste-here-generated-task-id'
)
print(f'VALIDATION REPORT:\n', report, '\n')

# return details for given project_id and base_key
response = api.get_contact_card(
    project_id='1506ff30-69ec-4c31-9b09-21eb4a6460ad',
    base_key='bazaMR_5272644702'
)
print(f'DETAILS FOR GIVEN BASE_KEY:\n', response, '\n')
