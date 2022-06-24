""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных """

encode_in_file = 'rle_encode_in.txt'
encode_out_file = 'rle_encode_out.txt'
decode_in_file = 'rle_decode_in.txt'
decode_out_file = 'rle_decode_out.txt'


def encode_file(in_file=encode_in_file, out_file=encode_out_file):
    print('Кодирование файла', in_file)
    with open(in_file, 'r') as file:
        txt = file.read().strip()
    print('Входящие данные:')
    print(txt)
    index, index2 = 0, 0
    encoded_txt = ''
    while index < len(txt):
        encoded_txt += txt[index]
        count = 0
        while index2 < len(txt) and txt[index2] == txt[index]:
            index2 += 1
            count += 1
        index = index2
        encoded_txt += str(count)
    if out_file:
        with open(out_file, 'w') as file:
            print(encoded_txt, file=file)
    print('Исходящие данные:')
    print(encoded_txt)


def decode_file(in_file=decode_in_file, out_file=decode_out_file):
    print('Декодирование файла', in_file)
    with open(in_file, 'r') as file:
        txt = file.readline().strip()
    print('Входящие данные:')
    print(txt)
    decoded_txt = ''
    index = 0
    while index < len(txt):
        index2 = index + 1
        while index2 < len(txt) and txt[index2].isdigit():
            index2 += 1
        decoded_txt += txt[index] * int(txt[index + 1:index2])
        index = index2
    if out_file:
        with open(out_file, 'w') as file:
            print(decoded_txt, file=file)
    print('Исходящие данные:')
    print(decoded_txt)


if __name__ == '__main__':
    encode_file()
    print('-' * 50)
    decode_file()
