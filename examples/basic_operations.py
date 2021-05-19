from dmsales import DMSalesAPI

api = DMSalesAPI(api_key='your-generated-api-key') # you can generate a new key here https://app.dmsales.com/pl/panel/settings-account?settings=api-configuration

# download list of your projects
projects_list = api.project_list()
print('MY PROJECTS LIST:\n:', projects_list, '\n')

# download list of segments in your project
segments_list = api.segment_list(project_id='paste-here-project-id-from-projects-list')
print('MY SEGMENTS LIST:\n:', segments_list, '\n')

# download profiles and segments from project
search_list = api.search_list(project_id='paste-here-project-id-from-projects-list')
print('MY PROJECT PROFILES AND SEGMENTS:\n', search_list, '\n')

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

#add person
person_dict = {
    "tags": [
        "tag1",
        "tag2"
    ],
    "type": "b2b",
    "address": {
        "city": "Katowice",
        "county": "Katowice",
        "postal_code": "40-101",
        "street": "Al. Piastów",
        "street_number": "10",
        "local_number": "35",
        "voivodeship": "śląskie"
    },
    "personal_data": {
        "name": "Nowy",
        "surname": "Lead",
        "company_name": "My Very First Company",
        "position": "CEO"
    },
    "email": {
        "raw": "exae-email@test.test"
    },
    "phone": {
        "raw": "+48 123 456 678"
    },
    "sex": "kobieta"
}
response = api.add_person(id='test_id_1', project_id='paste-here-project-id-from-projects-list', person_dict=person_dict)
print(f'Person endpoint response: {response}')

#update person
response = api.update_person(id='test_id_1', project_id='paste-here-project-id-from-projects-list', person_dict=person_dict)
print(f'Person endpoint response: {response}')

#me
response = api.me()
print(f'My data: {response}')

#my points
response = api.my_points()
print(f'My points: {response}')