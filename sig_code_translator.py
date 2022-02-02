from .sig_codes import translation_dict


def convert_to_sig_from_english(input_string: str) -> str:
    output_string = input_string.lower().strip()
    # sort dict by value length, descending
    for key in sorted(
        translation_dict, key=lambda k: len(translation_dict[k]), reverse=True
    ):
        value = translation_dict[key]
        if value in output_string:
            output_string = output_string.replace(value, key)
    return output_string


def convert_to_english_from_sig(input_string: str) -> str:
    input_list = input_string.lower().strip().split(" ")
    output_list = []
    for word in input_list:
        if word in translation_dict:
            output_list.append(translation_dict[word])
        else:
            output_list.append(word)
    output_string = " ".join(output_list)
    return output_string
