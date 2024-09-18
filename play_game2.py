import random

# 単語リスト
words = ["red", "blue", "green", "yellow", "black", "white", "silver", "gold", "purple", "azure"]

def play_game():
    word = random.choice(words)
    word_result = "_" * len(word)
    guessed = False
    guessed_letters = []
    attempts_failed = 5

    print("単語当てゲームを始めます！")
    print(word_result)
    print(f"残り失敗可能回数: {attempts_failed}")

    while not guessed and attempts_failed > 0:
        guess = input("アルファベットを1文字入力してください: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("その文字は既に使用しています。別の文字を試してください。")
            elif guess not in word:
                print(f"{guess} は単語に含まれていません。")
                attempts_failed -= 1
                guessed_letters.append(guess)
            else:
                print(f"正解！ {guess} は単語に含まれています。")
                guessed_letters.append(guess)
                word_as_list = list(word_result)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_result = "".join(word_as_list)
                if "_" not in word_result:
                    guessed = True
        else:
            print("無効な入力です。アルファベットを1文字入力してください。")
        
        print(word_result)
        print(f"残り失敗可能回数: {attempts_failed}")
    
    if guessed:
        print("おめでとうございます！単語を当てました。")
    else:
        print(f"残念でした。正解は {word} でした。")

def main():
    while True:
        play_game()
        play_again = input("もう一度プレイしますか？ (はい: y, いいえ: n): ").lower()
        if play_again != 'y':
            print("ゲームを終了します。お疲れ様でした！")
            break

# ゲームを開始
if __name__ == "__main__":
    main()
