import random
import os

class MillionaireGame:
    def __init__(self):
        self.score = 0
        self.current_question = 0
        self.total_questions = 15
        self.correct_answers = 0
        self.questions = self.load_questions()
        
        self.answer_history = []
        self.correct_history = []
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def load_questions(self):
        questions_data = [
            ["Какая планета самая большая в Солнечной системе?", ["Земля", "Марс", "Юпитер", "4546B"], 2],
            ["Какой химический элемент обозначается символом 'O'?", ["Золото", "Кислород", "Серебро", "Олег"], 1],
            ["Кто написал роман 'Мастер и Маргарита'?", ["Лев Толстой", "Федор Достоевский", "Михаил Булгаков", "Александр Пушкин"], 2],
            ["В каком году человек впервые полетел в космос?", ["1957", "1961", "1969", "1997"], 1],
            ["Как называется самая длинная река в мире?", ["Амазонка", "Нил", "Янцзы", "Миссисипи"], 1],
            ["Какой газ преобладает в атмосфере Земли?", ["Кислород", "Углекислый газ", "Азот", "Водород"], 2],
            ["Кто изобрел телефон?", ["Томас Эдисон", "Никола Тесла", "Александр Белл", "Гульельмо Маркони"], 2],
            ["Какой океан самый большой по площади?", ["Атлантический", "Индийский", "Северный Ледовитый", "Тихий"], 3],
            ["Сколько континентов на Земле?", ["5", "6", "7", "8"], 2],
            ["Кто написал картину 'Мона Лиза'?", ["Рафаэль", "Микеланджело", "Леонардо да Винчи", "Винсент Ван Гог"], 2],
            ["Какой элемент имеет атомный номер 1?", ["Гелий", "Водород", "Литий", "Кислород"], 1],
            ["Столица Австралии?", ["Сидней", "Мельбурн", "Канберра", "Брисбен"], 2],
            ["Какой из этих языков не является славянским?", ["Польский", "Чешский", "Венгерский", "Украинский"], 2],
            ["Кто открыл закон всемирного тяготения?", ["Альберт Эйнштейн", "Исаак Ньютон", "Галилео Галилей", "Никола Коперник"], 1],
            ["Какой год считается годом основания Рима?", ["476 г. до н.э.", "753 г. до н.э.", "44 г. до н.э.", "27 г. до н.э."], 1],
            ["Какой из этих металлов является самым легким?", ["Золото", "Алюминий", "Литий", "Ртуть"], 2],
            ["Сколько цветов у радуги?", ["5", "6", "7", "8"], 2],
            ["Кто написал 'Евгения Онегина'?", ["Лермонтов", "Пушкин", "Гоголь", "Тургенев"], 1],
            ["Какой орган человека самый большой?", ["Мозг", "Печень", "Кожа", "Сердце"], 2],
            ["Сколько сторон у восьмиугольника?", ["6", "7", "8", "9"], 2],
            ["Какая самая высокая гора в мире?", ["К2", "Эверест", "Макалу", "Канченджанга"], 1],
            ["Кто был первым президентом России?", ["Ельцин", "Горбачев", "Путин", "Медведев"], 0],
            ["Какой прибор измеряет атмосферное давление?", ["Термометр", "Барометр", "Гигрометр", "Анемометр"], 1],
            ["Сколько часов в сутках?", ["12", "24", "36", "48"], 1],
            ["Кто написал 'Войну и мир'?", ["Достоевский", "Толстой", "Чехов", "Тургенев"], 1],
            ["Сколько дней в високосном году?", ["365", "366", "364", "367"], 1],
            ["Какая самая маленькая страна в мире?", ["Монако", "Ватикан", "Сан-Марино", "Лихтенштейн"], 1],
            ["Как называется наука о растениях?", ["Зоология", "Ботаника", "Биология", "Экология"], 1],
            ["Сколько игроков в футбольной команде?", ["9", "10", "11", "12"], 2],
            ["Какой газ нужен растениям для фотосинтеза?", ["Кислород", "Азот", "Углекислый газ", "Водород"], 2],
            ["Сколько зубов у взрослого человека?", ["28", "30", "32", "34"], 2],
            ["Какой город является столицей Франции?", ["Лондон", "Берлин", "Париж", "Рим"], 2],
            ["Кто написал 'Гамлета'?", ["Чарльз Диккенс", "Уильям Шекспир", "Марк Твен", "Джейн Остин"], 1],
            ["Как называется самая большая пустыня в мире?", ["Сахара", "Гоби", "Аравийская", "Калахари"], 0],
            ["Сколько планет в Солнечной системе?", ["7", "8", "9", "Недостаточно"], 1],
            ["Какой язык программирования назван в честь комедийного шоу?", ["Python", "Java", "C++", "ComedyClub"], 0]
        ]
        
        return random.sample(questions_data, self.total_questions)
    
    def shuffle_answers(self, question_data):
        answers, correct_idx = question_data[1][:], question_data[2]
        correct_answer = answers[correct_idx]
        
        indexed_answers = list(enumerate(answers))
        random.shuffle(indexed_answers)
        
        shuffled_answers = [ans for _, ans in indexed_answers]
        new_correct_idx = shuffled_answers.index(correct_answer)
        
        return shuffled_answers, new_correct_idx
    
    def get_game_stats(self):
        stats = [
            f"Вопрос: {self.current_question + 1}/{self.total_questions}",
            f"Счет: {self.score} очков",
            f"Правильных: {self.correct_answers}/{self.current_question}" if self.current_question > 0 else "Правильных: 0/0"
        ]
        return stats
    
    def display_header(self):
        header_lines = [
            "╔══════════════════════════════════════════════════════════╗",
            "║            КТО ХОЧЕТ СТАТЬ МИЛЛИОНЕРОМ?                  ║",
            "╚══════════════════════════════════════════════════════════╝"
        ]
        return "\n".join(header_lines)
    
    def display_question(self, question_data, shuffled_answers):
        lines = [
            f"\n{'═' * 60}",
            f"❓ ВОПРОС {self.current_question + 1}:",
            f"{'─' * 60}",
            f"{question_data[0]}",
            f"{'─' * 60}"
        ]
        
        for i, answer in enumerate(shuffled_answers, 1):
            lines.append(f"{i}. {answer}")
        
        lines.append(f"{'─' * 60}")
        return "\n".join(lines)
    
    def get_valid_choice(self):
        valid_choices = ['0', '1', '2', '3', '4']
        
        while True:
            choice = input("\nВаш выбор (1-4) или '0' для выхода: ").strip()
            
            if choice in valid_choices:
                return int(choice)
            print("⚠️  Пожалуйста, введите число от 0 до 4")
    
    def process_answer(self, user_choice, is_correct, shuffled_answers, correct_idx):
        self.answer_history.append(user_choice)
        self.correct_history.append(is_correct)
        
        if is_correct:
            self.score += 100
            self.correct_answers += 1
            result_lines = [
                f"\n{'✅' * 30}",
                f"✅ ПРАВИЛЬНЫЙ ОТВЕТ!",
                f"✅ +100 очков",
                f"{'✅' * 30}"
            ]
        else:
            self.score = max(0, self.score - 100) 
            correct_answer = shuffled_answers[correct_idx]
            result_lines = [
                f"\n{'❌' * 30}",
                f"❌ НЕПРАВИЛЬНЫЙ ОТВЕТ!",
                f"❌ -100 очков",
                f"📖 Правильный ответ: {correct_answer} (№{correct_idx + 1})",
                f"{'❌' * 30}"
            ]
        
        self.current_question += 1
        return "\n".join(result_lines)
    
    def get_final_stats(self):
        total_answered = self.current_question
        percentage = (self.correct_answers / total_answered * 100) if total_answered > 0 else 0
        
        stats = [
            f"\n{'🎉' * 30}",
            f"🎉 ИГРА ЗАВЕРШЕНА!",
            f"{'🎉' * 30}",
            f"\n{'📊' * 20}",
            f"📊 ФИНАЛЬНАЯ СТАТИСТИКА:",
            f"{'📊' * 20}",
            f"• Всего вопросов: {self.total_questions}",
            f"• Отвечено: {total_answered}",
            f"• Правильных ответов: {self.correct_answers}",
            f"• Процент правильных: {percentage:.1f}%",
            f"• Финальный счет: {self.score} очков"
        ]
        
        # Определяем оценку
        if percentage >= 90:
            grade = "🥇 ЗОЛОТО! Вы настоящий гений!"
        elif percentage >= 70:
            grade = "🥈 СЕРЕБРО! Отличный результат!"
        elif percentage >= 50:
            grade = "🥉 БРОНЗА! Хорошие знания!"
        else:
            grade = "📚 ЕСТЬ КУДА СТРЕМИТЬСЯ! Продолжайте учиться!"
        
        stats.extend([
            f"\n{'🏆' * 20}",
            f"🏆 ВАША ОЦЕНКА:",
            f"{'🏆' * 20}",
            grade
        ])
        
        return "\n".join(stats)
    
    def get_answer_history_table(self):
        if not self.answer_history:
            return ""
        
        table_lines = [
            f"\n{'📝' * 20}",
            f"📝 ИСТОРИЯ ОТВЕТОВ:",
            f"{'📝' * 20}"
        ]
        
        for i in range(len(self.answer_history)):
            status = "✅" if self.correct_history[i] else "❌"
            answer_num = self.answer_history[i]
            table_lines.append(f"Вопрос {i+1}: {status} (выбрано: {answer_num})")
        
        return "\n".join(table_lines)
    
    def play_round(self):
        if self.current_question >= len(self.questions):
            return False
        
        question_data = self.questions[self.current_question]
        shuffled_answers, correct_idx = self.shuffle_answers(question_data)
        
        self.clear_screen()
        print(self.display_header())
        print("\n".join(self.get_game_stats()))
        print(self.display_question(question_data, shuffled_answers))
        
        user_choice = self.get_valid_choice()
        
        if user_choice == 0:
            return 'exit'
        
        is_correct = (user_choice - 1) == correct_idx
        
        self.clear_screen()
        print(self.display_header())
        print("\n".join(self.get_game_stats()))
        print(self.process_answer(user_choice, is_correct, shuffled_answers, correct_idx))
        
        if self.current_question < self.total_questions:
            input(f"\n{'⏭️ ' * 20}\nНажмите Enter для следующего вопроса...")
        
        return 'continue'
    
    def play(self):
        self.clear_screen()
        print(self.display_header())
        
        rules = [
            "\n" + "="*60,
            "📋 ПРАВИЛА ИГРЫ:",
            "="*60,
            "• Вам будет задано 15 случайных вопросов",
            "• Отвечайте, вводя номер ответа (1, 2, 3 или 4)",
            "• За правильный ответ: +100 очков",
            "• За неправильный ответ: -100 очков",
            "• Минимальный счет: 0 очков",
            "• Для выхода введите 0",
            "="*60
        ]
        
        print("\n".join(rules))
        input("\n🎮 Нажмите Enter, чтобы начать игру...")
        
        # Игровой цикл
        while self.current_question < self.total_questions:
            result = self.play_round()
            if result == 'exit':
                print(f"\n🎯 Игра завершена досрочно!")
                break
        
        self.clear_screen()
        print(self.display_header())
        print(self.get_final_stats())
        print(self.get_answer_history_table())
        print(f"\n🎮 Спасибо за игру! До встречи!")

def main():
    while True:
        game = MillionaireGame()
        game.play()
        
        options = [
            f"\n{'🔄' * 20}",
            "Хотите сыграть еще раз?",
            "1 - Да, сыграть еще раз",
            "0 - Нет, выйти из игры"
        ]
        
        print("\n".join(options))
        choice = input("\nВаш выбор: ").strip()
        
        if choice != '1':
            farewell = [
                "\n" + "="*60,
                "👋 До свидания! Спасибо за игру!",
                "="*60
            ]
            print("\n".join(farewell))
            break

if __name__ == "__main__":
    main()