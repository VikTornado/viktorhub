from django.core.management.base import BaseCommand
from django.utils import timezone
from content.models import Tag, Project, BlogPost, Note
from datetime import timedelta


class Command(BaseCommand):
    help = 'Populate database with seed data for ViktorHub'

    def handle(self, *args, **options):
        self.stdout.write('Creating seed data...')

        # Create Tags
        tags_data = [
            'Python', 'Django', 'JavaScript', 'React', 'Next.js', 'TypeScript',
            'PostgreSQL', 'Docker', 'REST API', 'Full-Stack', 'DevOps',
            'Machine Learning', 'Data Science', 'Web Development', 'Tutorial'
        ]
        tags = {}
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags[tag_name] = tag
            if created:
                self.stdout.write(f'  ✓ Created tag: {tag_name}')

        # Create Projects
        projects_data = [
            {
                'title_en': 'ViktorHub - Personal Portfolio & Blog',
                'title_uk': 'ВікторХаб - Особисте Портфоліо та Блог',
                'excerpt_en': 'A full-stack web application built with Django and Next.js for managing projects, blog posts, and quick notes.',
                'excerpt_uk': 'Повнофункціональний веб-додаток, побудований на Django та Next.js для управління проектами, статтями блогу та швидкими нотатками.',
                'description_en': '<p>This project showcases modern web development practices with a Django REST Framework backend and Next.js frontend. Features include JWT authentication, multilingual content, responsive design, and Docker deployment.</p>',
                'description_uk': '<p>Цей проект демонструє сучасні практики веб-розробки з бекендом на Django REST Framework та фронтендом на Next.js. Функції включають JWT аутентифікацію, багатомовний контент, адаптивний дизайн та розгортання через Docker.</p>',
                'tech_stack': 'Django, Next.js, PostgreSQL, Docker, Tailwind CSS, REST API',
                'repo_url': 'https://github.com/VikTornado/viktorhub',
                'live_url': 'https://viktorhub.com',
                'tags': ['Django', 'Next.js', 'PostgreSQL', 'Docker', 'Full-Stack'],
                'is_featured': True
            },
            {
                'title_en': 'E-Commerce Platform',
                'title_uk': 'Платформа Електронної Комерції',
                'excerpt_en': 'Modern e-commerce solution with payment integration, inventory management, and real-time analytics.',
                'excerpt_uk': 'Сучасне рішення для електронної комерції з інтеграцією платежів, управлінням інвентарем та аналітикою в реальному часі.',
                'description_en': '<p>Built a scalable e-commerce platform handling thousands of daily transactions. Implemented Stripe payment processing, real-time inventory tracking, and comprehensive admin dashboard with sales analytics.</p>',
                'description_uk': '<p>Створено масштабовану платформу електронної комерції, яка обробляє тисячі щоденних транзакцій. Реалізовано обробку платежів через Stripe, відстеження інвентаря в реальному часі та повну адміністративну панель з аналітикою продажів.</p>',
                'tech_stack': 'React, Node.js, MongoDB, Stripe, Redis, AWS',
                'repo_url': 'https://github.com/VikTornado/ecommerce-platform',
                'live_url': 'https://demo-shop.example.com',
                'tags': ['React', 'JavaScript', 'Full-Stack', 'DevOps'],
                'is_featured': True
            },
            {
                'title_en': 'AI-Powered Content Analyzer',
                'title_uk': 'Аналізатор Контенту на Основі ШІ',
                'excerpt_en': 'Machine learning tool for content analysis, sentiment detection, and automated tagging.',
                'excerpt_uk': 'Інструмент машинного навчання для аналізу контенту, виявлення настрою та автоматичного тегування.',
                'description_en': '<p>Developed an AI-powered tool using natural language processing to analyze articles, detect sentiment, and automatically suggest relevant tags. Uses TensorFlow and scikit-learn for ML models.</p>',
                'description_uk': '<p>Розроблено інструмент на основі ШІ з використанням обробки природної мови для аналізу статей, виявлення настрою та автоматичної пропозиції відповідних тегів. Використовує TensorFlow та scikit-learn для моделей машинного навчання.</p>',
                'tech_stack': 'Python, TensorFlow, scikit-learn, Flask, Docker',
                'repo_url': 'https://github.com/VikTornado/ai-content-analyzer',
                'tags': ['Python', 'Machine Learning', 'Data Science'],
                'is_featured': True
            },
            {
                'title_en': 'Real-Time Chat Application',
                'title_uk': 'Додаток для Чату в Реальному Часі',
                'excerpt_en': 'WebSocket-based chat app with private messaging, group channels, and file sharing.',
                'excerpt_uk': 'Додаток для чату на основі WebSocket з приватними повідомленнями, груповими каналами та обміном файлами.',
                'description_en': '<p>Real-time messaging application built with Socket.io and React. Features include private/group chats, typing indicators, online status, message reactions, and secure file uploads.</p>',
                'description_uk': '<p>Додаток для обміну повідомленнями в реальному часі, побудований за допомогою Socket.io та React. Функції включають приватні/групові чати, індикатори набору тексту, статус онлайн, реакції на повідомлення та безпечне завантаження файлів.</p>',
                'tech_stack': 'React, Node.js, Socket.io, MongoDB, TypeScript',
                'repo_url': 'https://github.com/VikTornado/realtime-chat',
                'live_url': 'https://chat.example.com',
                'tags': ['React', 'TypeScript', 'JavaScript', 'Web Development'],
                'is_featured': False
            },
            {
                'title_en': 'Task Management Dashboard',
                'title_uk': 'Панель Управління Завданнями',
                'excerpt_en': 'Kanban-style project management tool with drag-and-drop, deadlines, and team collaboration.',
                'excerpt_uk': 'Інструмент управління проектами в стилі Kanban з перетягуванням, дедлайнами та командною співпрацею.',
                'description_en': '<p>Project management application inspired by Trello and Asana. Built with Next.js and features drag-and-drop task management, deadline tracking, team assignments, and real-time updates.</p>',
                'description_uk': '<p>Додаток для управління проектами, натхненний Trello та Asana. Побудований за допомогою Next.js і має функції управління завданнями з перетягуванням, відстеження термінів, призначення команди та оновлення в реальному часі.</p>',
                'tech_stack': 'Next.js, TypeScript, PostgreSQL, Prisma, Tailwind CSS',
                'repo_url': 'https://github.com/VikTornado/task-manager',
                'tags': ['Next.js', 'TypeScript', 'PostgreSQL', 'Full-Stack'],
                'is_featured': False
            },
            {
                'title_en': 'Weather Dashboard API',
                'title_uk': 'API Панелі Погоди',
                'excerpt_en': 'REST API for weather data aggregation from multiple sources with caching and analytics.',
                'excerpt_uk': 'REST API для агрегації даних про погоду з кількох джерел з кешуванням та аналітикою.',
                'description_en': '<p>Built a robust weather data API that aggregates information from multiple weather services, implements intelligent caching with Redis, and provides historical weather analytics. Includes rate limiting and API key management.</p>',
                'description_uk': '<p>Створено надійний API даних про погоду, який агрегує інформацію з кількох погодних сервісів, реалізує інтелектуальне кешування за допомогою Redis і надає аналітику історії погоди. Включає обмеження швидкості та управління ключами API.</p>',
                'tech_stack': 'Django, Django REST Framework, Redis, PostgreSQL, Celery',
                'repo_url': 'https://github.com/VikTornado/weather-api',
                'live_url': 'https://api.weather-dashboard.example.com',
                'tags': ['Django', 'REST API', 'Python', 'DevOps'],
                'is_featured': False
            },
        ]

        for proj_data in projects_data:
            tag_names = proj_data.pop('tags')
            project, created = Project.objects.get_or_create(
                slug=proj_data['title_en'].lower().replace(' ', '-').replace('--', '-'),
                defaults=proj_data
            )
            if created:
                project.tags.set([tags[name] for name in tag_names])
                self.stdout.write(f'  ✓ Created project: {proj_data["title_en"]}')

        # Create Blog Posts
        posts_data = [
            {
                'title_en': 'Building Modern Web Apps with Django and Next.js',
                'title_uk': 'Створення Сучасних Веб-Додатків з Django та Next.js',
                'excerpt_en': 'Learn how to build a production-ready full-stack application using Django REST Framework and Next.js with TypeScript.',
                'excerpt_uk': 'Дізнайтеся, як створити повнофункціональний додаток, готовий до виробництва, використовуючи Django REST Framework та Next.js з TypeScript.',
                'content_en': '<p>In this comprehensive guide, we\'ll explore how to build a modern full-stack web application combining the power of Django REST Framework on the backend with Next.js on the frontend.</p><h2>Why This Stack?</h2><p>Django provides a robust, batteries-included backend framework with excellent ORM, admin interface, and security features. Next.js offers server-side rendering, optimal performance, and a great developer experience.</p>',
                'content_uk': '<p>У цьому комплексному посібнику ми дослідимо, як створити сучасний повнофункціональний веб-додаток, поєднуючи потужність Django REST Framework на бекенді з Next.js на фронтенді.</p><h2>Чому Цей Стек?</h2><p>Django надає надійний фреймворк бекенду з відмінним ORM, адміністративним інтерфейсом та функціями безпеки. Next.js пропонує серверний рендеринг, оптимальну продуктивність та чудовий досвід розробника.</p>',
                'tags': ['Django', 'Next.js', 'Full-Stack', 'Web Development', 'Tutorial'],
                'status': 'published',
                'published_at': timezone.now() - timedelta(days=5)
            },
            {
                'title_en': 'Understanding JWT Authentication in Django',
                'title_uk': 'Розуміння JWT Аутентифікації в Django',
                'excerpt_en': 'A deep dive into implementing secure JWT authentication with Django REST Framework and SimpleJWT.',
                'excerpt_uk': 'Глибоке занурення в реалізацію безпечної JWT аутентифікації з Django REST Framework та SimpleJWT.',
                'content_en': '<p>JSON Web Tokens (JWT) have become the de facto standard for API authentication in modern web applications. Let\'s explore how to implement them securely in Django.</p><h2>What is JWT?</h2><p>JWT is a compact, URL-safe means of representing claims to be transferred between two parties. In the context of authentication, it allows stateless verification of user identity.</p>',
                'content_uk': '<p>JSON Web Tokens (JWT) стали фактичним стандартом для аутентифікації API в сучасних веб-додатках. Давайте дослідимо, як безпечно їх реалізувати в Django.</p><h2>Що таке JWT?</h2><p>JWT - це компактний, безпечний для URL спосіб представлення претензій для передачі між двома сторонами. У контексті аутентифікації він дозволяє перевірку особи користувача без стану.</p>',
                'tags': ['Django', 'REST API', 'Python', 'Tutorial'],
                'status': 'published',
                'published_at': timezone.now() - timedelta(days=12)
            },
            {
                'title_en': 'Optimizing React Performance with Memoization',
                'title_uk': 'Оптимізація Продуктивності React з Мемоізацією',
                'excerpt_en': 'Learn how to use React.memo, useMemo, and useCallback to prevent unnecessary re-renders and boost performance.',
                'excerpt_uk': 'Дізнайтеся, як використовувати React.memo, useMemo та useCallback для запобігання зайвим перемальовуванням і підвищення продуктивності.',
                'content_en': '<p>React is fast, but as your application grows, you might notice performance issues. Understanding memoization techniques is crucial for maintaining a snappy user experience.</p><h2>The Problem</h2><p>React components re-render when their props or state change. Sometimes this happens more often than necessary, leading to wasted computation.</p>',
                'content_uk': '<p>React швидкий, але в міру зростання вашого додатка ви можете помітити проблеми з продуктивністю. Розуміння технік мемоізації є критично важливим для підтримки швидкого користувацького досвіду.</p><h2>Проблема</h2><p>Компоненти React перемальовуються, коли змінюються їхні пропси або стан. Іноді це відбувається частіше, ніж необхідно, що призводить до марних обчислень.</p>',
                'tags': ['React', 'JavaScript', 'Web Development', 'Tutorial'],
                'status': 'published',
                'published_at': timezone.now() - timedelta(days=18)
            },
            {
                'title_en': 'Docker Best Practices for Python Applications',
                'title_uk': 'Найкращі Практики Docker для Додатків Python',
                'excerpt_en': 'Essential tips for creating efficient, secure, and production-ready Docker images for Python/Django projects.',
                'excerpt_uk': 'Основні поради для створення ефективних, безпечних та готових до виробництва Docker образів для проектів Python/Django.',
                'content_en': '<p>Docker has revolutionized how we deploy applications, but creating optimal Docker images requires understanding several best practices.</p><h2>Multi-Stage Builds</h2><p>Use multi-stage builds to keep your production images lean while having all the tools you need during development.</p>',
                'content_uk': '<p>Docker революціонізував спосіб розгортання додатків, але створення оптимальних Docker образів вимагає розуміння кількох найкращих практик.</p><h2>Багатоетапні Збірки</h2><p>Використовуйте багатоетапні збірки, щоб зберегти ваші виробничі образи компактними, маючи всі необхідні інструменти під час розробки.</p>',
                'tags': ['Docker', 'Python', 'Django', 'DevOps', 'Tutorial'],
                'status': 'published',
                'published_at': timezone.now() - timedelta(days=25)
            },
            {
                'title_en': 'Introduction to TypeScript for JavaScript Developers',
                'title_uk': 'Вступ до TypeScript для JavaScript Розробників',
                'excerpt_en': 'Making the transition from JavaScript to TypeScript: benefits, challenges, and practical examples.',
                'excerpt_uk': 'Перехід від JavaScript до TypeScript: переваги, виклики та практичні приклади.',
                'content_en': '<p>TypeScript has gained massive adoption in the JavaScript community. If you\'re wondering whether to make the switch, this guide will help you understand what TypeScript offers.</p><h2>What is TypeScript?</h2><p>TypeScript is a superset of JavaScript that adds static typing, making your code more predictable and easier to debug.</p>',
                'content_uk': '<p>TypeScript отримав масове визнання в спільноті JavaScript. Якщо ви вагаєтеся зробити перехід, цей посібник допоможе вам зрозуміти, що пропонує TypeScript.</p><h2>Що таке TypeScript?</h2><p>TypeScript - це надмножина JavaScript, яка додає статичну типізацію, роблячи ваш код більш передбачуваним і легшим для налагодження.</p>',
                'tags': ['TypeScript', 'JavaScript', 'Web Development', 'Tutorial'],
                'status': 'published',
                'published_at': timezone.now() - timedelta(days=30)
            },
        ]

        for post_data in posts_data:
            tag_names = post_data.pop('tags')
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['title_en'].lower().replace(' ', '-'),
                defaults=post_data
            )
            if created:
                post.tags.set([tags[name] for name in tag_names])
                self.stdout.write(f'  ✓ Created blog post: {post_data["title_en"]}')

        # Create Notes
        notes_data = [
            {
                'title_en': 'Python List Comprehension Trick',
                'title_uk': 'Трюк з List Comprehension в Python',
                'content_en': 'Quick tip: Use conditional list comprehension to filter and transform in one line:\n\nsquares = [x**2 for x in range(10) if x % 2 == 0]\n\nThis creates a list of squares of even numbers from 0 to 9.',
                'content_uk': 'Швидка порада: Використовуйте умовне list comprehension для фільтрації та трансформації в один рядок:\n\nsquares = [x**2 for x in range(10) if x % 2 == 0]\n\nЦе створює список квадратів парних чисел від 0 до 9.',
                'tags': ['Python']
            },
            {
                'title_en': 'CSS Flexbox Centering',
                'title_uk': 'Центрування за допомогою CSS Flexbox',
                'content_en': 'Perfect centering with Flexbox:\n\n.container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n\nWorks for both horizontal and vertical centering!',
                'content_uk': 'Ідеальне центрування за допомогою Flexbox:\n\n.container {\n  display: flex;\n  justify-content: center;\n  align-items: center;\n}\n\nПрацює як для горизонтального, так і для вертикального центрування!',
                'tags': ['Web Development']
            },
            {
                'title_en': 'Git Amend Last Commit',
                'title_uk': 'Git Зміна Останнього Коміту',
                'content_en': 'Forgot to add a file to your last commit?\n\ngit add forgotten_file.py\ngit commit --amend --no-edit\n\nThis adds the file to the previous commit without changing the message.',
                'content_uk': 'Забули додати файл до останнього коміту?\n\ngit add forgotten_file.py\ngit commit --amend --no-edit\n\nЦе додає файл до попереднього коміту без зміни повідомлення.',
                'tags': ['DevOps']
            },
            {
                'title_en': 'React useState Array Update',
                'title_uk': 'Оновлення Масиву в React useState',
                'content_en': 'To add an item to a state array:\n\nsetItems([...items, newItem]);\n\nTo remove an item:\n\nsetItems(items.filter(item => item.id !== idToRemove));',
                'content_uk': 'Щоб додати елемент до масиву стану:\n\nsetItems([...items, newItem]);\n\nЩоб видалити елемент:\n\nsetItems(items.filter(item => item.id !== idToRemove));',
                'tags': ['React', 'JavaScript']
            },
            {
                'title_en': 'Django Query Optimization',
                'title_uk': 'Оптимізація Запитів Django',
                'content_en': 'Avoid N+1 queries with select_related and prefetch_related:\n\n# For foreign keys\nProject.objects.select_related(\'author\')\n\n# For many-to-many\nProject.objects.prefetch_related(\'tags\')',
                'content_uk': 'Уникайте N+1 запитів з select_related та prefetch_related:\n\n# Для зовнішніх ключів\nProject.objects.select_related(\'author\')\n\n# Для багато-до-багатьох\nProject.objects.prefetch_related(\'tags\')',
                'tags': ['Django', 'Python']
            },
            {
                'title_en': 'Docker Cleanup Commands',
                'title_uk': 'Команди Очищення Docker',
                'content_en': 'Free up disk space:\n\ndocker system prune -a\n\nRemove all stopped containers:\n\ndocker container prune\n\nRemove unused images:\n\ndocker image prune -a',
                'content_uk': 'Звільнити місце на диску:\n\ndocker system prune -a\n\nВидалити всі зупинені контейнери:\n\ndocker container prune\n\nВидалити невикористовувані образи:\n\ndocker image prune -a',
                'tags': ['Docker', 'DevOps']
            },
            {
                'title_en': 'JavaScript Array Methods Cheatsheet',
                'title_uk': 'Шпаргалка з Методів Масивів JavaScript',
                'content_en': 'Essential array methods:\n\nmap() - transform each element\nfilter() - select elements\nreduce() - accumulate to single value\nfind() - get first matching element\nevery() - test if all match\nsome() - test if any match',
                'content_uk': 'Основні методи масивів:\n\nmap() - трансформувати кожен елемент\nfilter() - вибрати елементи\nreduce() - накопичити до одного значення\nfind() - отримати перший збіг\nevery() - перевірити, чи всі відповідають\nsome() - перевірити, чи хоч один відповідає',
                'tags': ['JavaScript', 'Web Development']
            },
            {
                'title_en': 'PostgreSQL JSON Query',
                'title_uk': 'JSON Запити в PostgreSQL',
                'content_en': 'Query JSON fields in PostgreSQL:\n\nSELECT * FROM projects \nWHERE data->>\'status\' = \'active\';\n\nFor nested data:\n\nWHERE data->\'config\'->>\'enabled\' = \'true\';',
                'content_uk': 'Запити до JSON полів в PostgreSQL:\n\nSELECT * FROM projects \nWHERE data->>\'status\' = \'active\';\n\nДля вкладених даних:\n\nWHERE data->\'config\'->>\'enabled\' = \'true\';',
                'tags': ['PostgreSQL']
            },
        ]

        for note_data in notes_data:
            tag_names = note_data.pop('tags')
            note, created = Note.objects.get_or_create(
                content_en=note_data['content_en'],
                defaults=note_data
            )
            if created:
                note.tags.set([tags[name] for name in tag_names])
                self.stdout.write(f'  ✓ Created note: {note_data.get("title_en", "Untitled")}')

        self.stdout.write(self.style.SUCCESS('\n✅ Seed data created successfully!'))
        self.stdout.write(f'Total: {Project.objects.count()} projects, {BlogPost.objects.count()} posts, {Note.objects.count()} notes, {Tag.objects.count()} tags')
