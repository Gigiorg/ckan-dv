import ckan.plugins.toolkit as tk
import ckanext.test.logic.schema as schema


@tk.side_effect_free
def test_get_sum(context, data_dict):
    tk.check_access(
        "test_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.test_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'test_get_sum': test_get_sum,
    }
