# TODO  Напишите функцию count_letters
def count_letters(text):
    text = text.lower()
    letter_dict = {}
    for i in text:
        if i.isalpha():
            if i in letter_dict.keys():
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1
    return letter_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letter_dict):
    new_dict = {}
    letters = letter_dict.keys()
    total_letters = sum(letter_dict.values())
    for i in letters:
        new_dict[i] = letter_dict[i]/total_letters
    return new_dict


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary = calculate_frequency(count_letters(main_str))
for i, j in dictionary.items():
    print(f'{i}: {round(j, 2):.2f}')
