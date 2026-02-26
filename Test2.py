def manage_tags(existing_tags: dict, *simple_tags, **key_value_tags) -> dict:
    """
    Applies simple and key-value tags to an existing dictionary of tags.

    Args:
        existing_tags: The initial dictionary of tags.
        *simple_tags: Positional string arguments to be added as tags with a
                      value of 'true'. Duplicates should be ignored.
        **key_value_tags: Keyword arguments to be added or used to overwrite
                          existing tags.

    Returns:
        A new dictionary with all tags merged.
    """

    new_tags = existing_tags.copy()
    for item in simple_tags:
        new_tags.update({item:True})
    for k, v in key_value_tags.items():
        if k in new_tags:
            new_tags.update({k:v})
        else:
            new_tags.setdefault(k, v)  
    return new_tags

initial = {'owner': 'dev-team', 'env': 'dev'}
final_tags = manage_tags(
    initial,
    'billable',              # A simple tag
    'critical',              # Another simple tag
    env='staging',           # A key-value tag that overwrites an existing key
    cost_center='xyz-123'    # A new key-value tag
)
print(final_tags)

    