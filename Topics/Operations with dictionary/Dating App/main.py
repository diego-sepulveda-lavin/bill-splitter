def select_dates(potential_dates):
    matches = []
    min_age = 30
    for candidate in potential_dates:
        expected_age = candidate['age'] > min_age
        expected_city = candidate['city'] == 'Berlin'
        expected_hobbies = 'art' in candidate['hobbies']

        if expected_age and expected_city and expected_hobbies:
            matches.append(candidate['name'])

    return ", ".join(matches)
