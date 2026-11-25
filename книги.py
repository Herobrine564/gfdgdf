while True:
  book = 0
  print("Книг")
  print(book)
  menu = int(input("Перейдите в меню (напишите 1)"))
  if menu == 1:
    print("Меню")
    break
  else:
    print("Ошибка = напишите 1")
while True:  
  action = int(input("Выберите действие: 1 - выдача книги, 2 - показ выданных книг, 3 - сбрасывание счетчика, 0 - завершение работы"))
  if action == 1:
    add = int(input("Добавьте книгу(напишите 1 или для отмены напишите 0)"))
    if add == 0:
      print("Возвращение обратно")
    elif add == 1:
        book += 1
    else:
        print("Ошибка = напишите 1")
  elif action == 2:
    print("Выданных книг")
    print(book)
  elif action == 3:
    book = 0
    print("Счетчик книг успешно сброшен")
  elif action == 0:
    break
  else:
    print("Ошибка = это не действие")