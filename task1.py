import requests


URL = "https://jsonplaceholder.typicode.com"

def get_first_five_posts():
    try:
        # Отправляем GET-запрос к /posts
        response = requests.get(f"{URL}/posts")
        
        # Проверяем успешность запроса
        response.raise_for_status()  
        
        # Получаем данные в формате JSON
        posts = response.json()
        
        print("Первые 5 постов:\n" + "="*50)
        
        # Выводим только первые 5 постов
        for post in posts[:5]:
            print(f"ID: {post['id']}")
            print(f"Заголовок: {post['title']}")
            print(f"Текст:\n{post['body']}")
            print("-" * 70)
            
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    get_first_five_posts()