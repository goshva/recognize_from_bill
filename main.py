import easyocr
def text_recognize(file_path):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=0, allowlist='1,2,3,4,5,6,7,8,9,0,А,Б,В,Г,Е,З,И,К,Л,М,Н,О,П,С,Т,Х,Ч,Ь,Э,Я,а,б,в,г,е,з,и,к,л,м,н,о,п,с,т,х,ч,ь,э,я')

    # Проверяем, что есть как минимум два элемента в результате
    if len(result) >= 3:
        # Второй элемент (индекс 1) и третий элемент (индекс 2)
        print(result[2])  # Второй элемент
        print(result[3])  # Третий элемент
    # Проверяем равен ли вывод 2 номера и 3 если нето то это не купюра
    elif result[2] == result[3]:
        print("It's not a bill")
    else:
        print("Not enough text elements found in the image.")

    return result


def main():
    file_path = input("Enter a file path: ")
    print(text_recognize(file_path=file_path))


if __name__ == "__main__":
    main()
