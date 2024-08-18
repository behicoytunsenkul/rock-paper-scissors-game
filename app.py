from tkinter import *
import tkinter.font as font
import random
import pygame
from tkinter import messagebox

# Oyun içi ses dosyaları
pygame.mixer.init()
click_sound = pygame.mixer.Sound("./sounds/click-47609.mp3")
win_sound = pygame.mixer.Sound("./sounds/goodresult-82807.mp3")
lose_sound = pygame.mixer.Sound("./sounds/kids-laugh-45357.mp3")
brbr_sound = pygame.mixer.Sound("./sounds/back-tick-107822.mp3")

# Default değerler
player_score = 0
computer_score = 0
game_count = 0
player_wins = 0
computer_wins = 0
options = [('Taş', 0), ('Kağıt', 1), ('Makas', 2)]
difficulty = 'Kolay'

def play_sound(effect):
    effect.play()

def reset_game():
    global player_score, computer_score, game_count
    player_score = 0
    computer_score = 0
    game_count += 1
    winner_label.config(text="Oynamak için bir seçim yapın...", fg='black')

# Oyunu sıfırlar
def reset_all():
    global player_score, computer_score, game_count, player_wins, computer_wins
    player_score = 0
    computer_score = 0
    game_count = 0
    player_wins = 0
    computer_wins = 0
    winner_label.config(text="Oynamak için bir seçim yapın...", fg='black')
    player_score_label.config(text='Skorunuz: -')
    computer_score_label.config(text='Bilgisayarın Skoru: -')
    player_choice_label.config(text='Seçiminiz: ---')
    computer_choice_label.config(text='Bilgisayarın Seçimi: ---')
    difficulty_label.config(text="Zorluk Seviyesi: X")
    play_sound(click_sound)

def player_choice(player_input):
    global player_score, computer_score, player_wins, computer_wins

    # Butona bastıkça ses çıkar
    play_sound(click_sound)

    computer_input = get_computer_choice()

    player_choice_label.config(text='Seçiminiz: ' + player_input[0])
    computer_choice_label.config(text='Bilgisayarın Seçimi: ' + computer_input[0])

    if player_input == computer_input:
        winner_label.config(text="Berabere!", fg="orange", font=('Times New Roman', 26, 'bold'))
        play_sound(brbr_sound)
    elif (player_input[1] - computer_input[1]) % 3 == 1:
        player_score += 1
        winner_label.config(text="Kazandınız!", fg="green", font=('Times New Roman', 26, 'bold'))
        player_score_label.config(text='Skorunuz: ' + str(player_score))
        play_sound(win_sound)
    else:
        computer_score += 1
        winner_label.config(text="Bilgisayar Kazandı!", fg="red", font=('Times New Roman', 26, 'bold'))
        computer_score_label.config(text='Bilgisayarın Skoru: ' + str(computer_score))
        play_sound(lose_sound)

    if player_score == 3:
        player_wins += 1
        messagebox.showinfo("Oyun Bitti", "Tebrikler, oyunu kazandınız!")
        reset_game()
        reset_all()
    elif computer_score == 3:
        computer_wins += 1
        messagebox.showinfo("Oyun Bitti", "Maalesef, bilgisayar oyunu kazandı!")
        reset_game()
        reset_all()

#bilgisayarın secim stratejileri
def get_computer_choice():
    #olasılık oranı azaldıkca zorluk artar
    if difficulty == 'Kolay': #secimleri tamamen rasgele yapar
        return random.choice(options)

    elif difficulty == 'Orta':
        if random.random() > 0.5: #%5
            if player_choice_label['text'] == 'Seçiminiz: Taş':
                return options[1]  # Kağıt
            elif player_choice_label['text'] == 'Seçiminiz: Kağıt':
                return options[2]  # Makas
            elif player_choice_label['text'] == 'Seçiminiz: Makas':
                return options[0]  # Taş
        else:
            return random.choice(options)

    elif difficulty == 'Zor':
        if random.random() > 0.3: #%3
            if player_choice_label['text'] == 'Seçiminiz: Taş':
                return options[1]  # Kağıt
            elif player_choice_label['text'] == 'Seçiminiz: Kağıt':
                return options[2]  # Makas
            elif player_choice_label['text'] == 'Seçiminiz: Makas':
                return options[0]  # Taş
        else:
            return random.choice(options)

    elif difficulty == 'İmkansız':
            if player_choice_label['text'] == 'Seçiminiz: Taş':
                return options[1]  # Kağıt
            elif player_choice_label['text'] == 'Seçiminiz: Kağıt':
                return options[2]  # Makas
            elif player_choice_label['text'] == 'Seçiminiz: Makas':
                return options[0]  # Taş


def set_difficulty(level):
    global difficulty
    difficulty = level
    difficulty_label.config(text="Zorluk Seviyesi: " + difficulty)
    play_sound(click_sound)

game_window = Tk()
game_window.title("Taş-Kağıt-Makas")
game_window.configure(bg='lavender')
app_font = font.Font(size=22, weight='bold')
game_title = Label(game_window, text='Taş Kağıt Makas', font=font.Font(size=40), fg='red', bg='lavender')
game_title.pack()

# Zorluk seviyesi seçimi
difficulty_frame = Frame(game_window, bg='lavender')
difficulty_frame.pack(pady=10)
difficulty_label = Label(difficulty_frame, text="Zorluk Seviyesi: SEÇİM YOK", font=app_font, fg='blue', bg='lavender')
difficulty_label.grid(row=0, column=0, pady=8)
kolay_btn = Button(difficulty_frame, text='KOLAY', width=10, command=lambda: set_difficulty('Kolay'),
                   font=app_font, fg='green')
kolay_btn.grid(row=0, column=1, padx=8)
orta_btn = Button(difficulty_frame, text='ORTA', width=10, command=lambda: set_difficulty('Orta'),
                  font=app_font, fg='orange')
orta_btn.grid(row=0, column=2, padx=8)
zor_btn = Button(difficulty_frame, text='ZOR', width=10, command=lambda: set_difficulty('Zor'),
                 font=app_font, fg='red')
zor_btn.grid(row=0, column=3, padx=8)
imkansiz_btn = Button(difficulty_frame, text='İMKANSIZ', width=10, command=lambda: set_difficulty('İmkansız'),
                      font=app_font, fg='purple')
imkansiz_btn.grid(row=0, column=4, padx=8)
winner_label = Label(game_window, text="Oynamak için bir seçim yapın...", fg='black', font=('Helvetica', 26, 'bold'),
                     pady=8, bg='lavender')
winner_label.pack()

input_frame = Frame(game_window, bg='lavender')
input_frame.pack()

#Secenekler
player_options = Label(input_frame, text="Seçenekleriniz: ", font=app_font, fg='purple', bg='lavender')
player_options.grid(row=0, column=0, pady=8)

rock_btn = Button(input_frame, text='🪨 Taş 🪨', width=15, bd=0, bg='pink', pady=5,
                  command=lambda: player_choice(options[0]),
                  font=app_font)
rock_btn.grid(row=1, column=1, padx=8, pady=5)

paper_btn = Button(input_frame, text='📄 Kağıt 📄', width=15, bd=0, bg='silver', pady=5,
                   command=lambda: player_choice(options[1]),
                   font=app_font)
paper_btn.grid(row=1, column=2, padx=8, pady=5)

scissors_btn = Button(input_frame, text='✂️ Makas ✂️', width=15, bd=0, bg='light blue', pady=5,
                      command=lambda: player_choice(options[2]),
                      font=app_font)
scissors_btn.grid(row=1, column=3, padx=8, pady=5)

# Raporların görüntülenmesi
score_label = Label(input_frame, text='Skor:', font=app_font, fg='black', bg='lavender')
score_label.grid(row=2, column=0)

player_choice_label = Label(input_frame, text='Seçiminiz: ---', font=app_font, fg='navy', bg='lavender')
player_choice_label.grid(row=3, column=1, pady=5)

player_score_label = Label(input_frame, text='Skorunuz: -', font=app_font, fg='navy', bg='lavender')
player_score_label.grid(row=3, column=2, pady=5)

computer_choice_label = Label(input_frame, text='Bilgisayarın Seçimi: ---', font=app_font, fg='black', bg='lavender')
computer_choice_label.grid(row=4, column=1, pady=5)

computer_score_label = Label(input_frame, text='Bilgisayarın Skoru: -', font=app_font, fg='black', bg='lavender')
computer_score_label.grid(row=4, column=2, padx=(10, 0), pady=5)

# Sıfırla butonu
reset_btn = Button(game_window, text="Sıfırla", command=reset_all, font=app_font, fg='black', bg='lightgrey')
reset_btn.pack(pady=20)

game_window.geometry('1200x500')  # Oyun ekran boyutu
game_window.mainloop()
