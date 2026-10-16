import os
import telebot

# Токенни сервердан олади
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Ассалому алайкум, устоз! Аттестация тест ботига хуш келибсиз.\n\nТест топширишни бошлаш учун /test буйруғини юборинг."
    )

@bot.message_handler(commands=['test'])
def send_test_poll(message):
    question = "[11/26] В стихотворении «Заблудившийся трамвай» в лирической форме изображены духовные искания русской интеллигенции после революции. Назовите этого поэта."
    
    options = [
        "А. Блок",
        "О. Мандельштам",
        "И. Бунин",
        "Н. Гумилёв"
    ]
    
    correct_index = 3  # Н. Гумилёв тўғри жавоб (0, 1, 2, 3)
    explanation = "💡 Изоҳ: Бу шеър Николай Гумилёв қаламига мансуб бўлиб, унда инқилобдан кейинги давр руҳияти акс этган."

    bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type='quiz',
        correct_option_id=correct_index,
        is_anonymous=False,
        explanation=explanation
    )

if __name__ == "__main__":
    print("Бот муваффақиятли ишга тушди...")
    bot.infinity_polling()
