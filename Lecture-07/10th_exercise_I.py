survey_results = [
    ["Python", "JavaScript", "C++"],
    ["Python", "JavaScript", "C#"],
    ["Python", "Java"],
    ["Python", "C++", "JavaScript"],
    ["Python", "JavaScript", "C++", "Java"]
]

see_once = set()
see_more = set()

attendance_sets = [set(participle) for participle in survey_results]

present_all_languages_chosen = set.intersection(*attendance_sets)
print(present_all_languages_chosen)

all_languages = set.union(*attendance_sets)

for participant in survey_results:
    for lang in set(participant):
        if lang in set(see_once):
            see_more.add(lang)
        else:
            see_once.add(lang)

only_chosen_one = see_once - see_more
print(list(only_chosen_one))

unique_languages = len(all_languages)
print("Number of unique languages: ", unique_languages)

