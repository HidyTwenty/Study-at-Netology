def count_words_percentage(queries):
    user1_ids = queries['user1']
    user2_ids = queries['user2']
    user3_ids = queries['user3']

    all_user_ids = user1_ids + user2_ids + user3_ids
    result = []

    for user_ids in all_user_ids:
        if user_ids not in result:
            result.append(user_ids)

    return result
