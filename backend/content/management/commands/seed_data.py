import os
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.utils import timezone
from content.models import Tag, Project, BlogPost, Note

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        # Create Tags
        tags_data = ['React', 'Next.js', 'Django', 'Python', 'Tailwind', 'PostgreSQL', 'Docker', 'AWS']
        tags = {}
        for name in tags_data:
            tag, created = Tag.objects.get_or_create(name=name)
            tags[name] = tag

        # Create Projects
        projects = [
            {
                'title_en': 'E-commerce Platform',
                'title_uk': 'Платформа електронної комерції',
                'excerpt_en': 'A full-featured online store built with Next.js and Django.',
                'excerpt_uk': 'Повнофункціональний інтернет-магазин на Next.js та Django.',
                'tech_stack': 'Next.js, Django, Postgres, Redis',
                'is_featured': True,
                'tag_names': ['Next.js', 'Django', 'PostgreSQL']
            },
            {
                'title_en': 'Weather Dashboard',
                'title_uk': 'Панель погоди',
                'excerpt_en': 'Real-time weather data visualization using OpenWeatherMap API.',
                'excerpt_uk': 'Візуалізація даних про погоду в реальному часі за допомогою API OpenWeatherMap.',
                'tech_stack': 'React, Tailwind, API',
                'is_featured': False,
                'tag_names': ['React', 'Tailwind']
            },
            {
                'title_en': 'Task Management App',
                'title_uk': 'Додаток для управління завданнями',
                'excerpt_en': 'Collaborative task tracking with real-time updates.',
                'excerpt_uk': 'Спільне відстеження завдань з оновленнями в реальному часі.',
                'tech_stack': 'Next.js, Supabase, Tailwind',
                'is_featured': True,
                'tag_names': ['Next.js', 'Tailwind']
            },
            {
                'title_en': 'Personal Portfolio',
                'title_uk': 'Особисте портфоліо',
                'excerpt_en': 'The very site you are looking at!',
                'excerpt_uk': 'Саме цей сайт, який ви зараз переглядаєте!',
                'tech_stack': 'Next.js, Django, Framer Motion',
                'is_featured': False,
                'tag_names': ['Next.js', 'Django', 'Tailwind']
            },
            {
                'title_en': 'Crypto Explorer',
                'title_uk': 'Крипто Провідник',
                'excerpt_en': 'Track cryptocurrency prices and market trends.',
                'excerpt_uk': 'Відстежуйте ціни на криптовалюту та ринкові тренди.',
                'tech_stack': 'React, Web3.js, Chart.js',
                'is_featured': False,
                'tag_names': ['React']
            },
            {
                'title_en': 'Smart Home Controller',
                'title_uk': 'Контролер розумного будинку',
                'excerpt_en': 'IoT dashboard for controlling home devices.',
                'excerpt_uk': 'Панель керування IoT для домашніх пристроїв.',
                'tech_stack': 'Python, Raspberry Pi, MQTT',
                'is_featured': True,
                'tag_names': ['Python', 'Docker']
            }
        ]

        for p in projects:
            project, created = Project.objects.get_or_create(
                slug=slugify(p['title_en']),
                defaults={
                    'title_en': p['title_en'],
                    'title_uk': p['title_uk'],
                    'excerpt_en': p['excerpt_en'],
                    'excerpt_uk': p['excerpt_uk'],
                    'description_en': f"<p>{p['excerpt_en']} Full description coming soon.</p>",
                    'description_uk': f"<p>{p['excerpt_uk']} Повний опис з'явиться незабаром.</p>",
                    'tech_stack': p['tech_stack'],
                    'is_featured': p['is_featured']
                }
            )
            for tag_name in p['tag_names']:
                project.tags.add(tags[tag_name])

        # Create Posts
        posts = [
            {
                'title_en': 'Mastering Next.js 14',
                'title_uk': 'Опанування Next.js 14',
                'excerpt_en': 'Learn the latest features of Next.js App Router.',
                'excerpt_uk': 'Дізнайтеся про останні можливості Next.js App Router.',
                'tag_names': ['Next.js']
            },
            {
                'title_en': 'Django for Beginners',
                'title_uk': 'Django для початківців',
                'excerpt_en': 'A comprehensive guide to building your first API.',
                'excerpt_uk': 'Вичерпний посібник зі створення вашого першого API.',
                'tag_names': ['Django', 'Python']
            },
            {
                'title_en': 'Dockerizing Full-Stack Apps',
                'title_uk': 'Докеризація Full-Stack додатків',
                'excerpt_en': 'How to setup Docker Compose for development.',
                'excerpt_uk': 'Як налаштувати Docker Compose для розробки.',
                'tag_names': ['Docker', 'PostgreSQL']
            },
            {
                'title_en': 'Tailwind Best Practices',
                'title_uk': 'Найкращі практики Tailwind',
                'excerpt_en': 'How to keep your CSS clean and maintainable.',
                'excerpt_uk': 'Як підтримувати ваш CSS чистим та зручним у супроводі.',
                'tag_names': ['Tailwind']
            },
            {
                'title_en': 'The Future of AI in Coding',
                'title_uk': 'Майбутнє ШІ в програмуванні',
                'excerpt_en': 'Exploring how AI assistants are changing work.',
                'excerpt_uk': 'Дослідження того, як ШІ-помічники змінюють роботу.',
                'tag_names': ['Python']
            }
        ]

        for p in posts:
            post, created = BlogPost.objects.get_or_create(
                slug=slugify(p['title_en']),
                defaults={
                    'title_en': p['title_en'],
                    'title_uk': p['title_uk'],
                    'excerpt_en': p['excerpt_en'],
                    'excerpt_uk': p['excerpt_uk'],
                    'content_en': f"<p>{p['excerpt_en']} Post content.</p>",
                    'content_uk': f"<p>{p['excerpt_uk']} Зміст статті.</p>",
                    'status': 'published',
                    'published_at': timezone.now()
                }
            )
            for tag_name in p['tag_names']:
                post.tags.add(tags[tag_name])

        # Create Notes
        notes = [
            "Quick tip: use React.memo for heavy components.",
            "Remember to check for memory leaks in useEffect.",
            "Django QuerySets are lazy, use select_related for performance.",
            "PostgreSQL indexing can speed up complex queries significantly.",
            "Always use environment variables for sensitive data.",
            "Next.js Image component handles optimization automatically.",
            "Tailwind config is where you define your brand colors.",
            "Keep your Git commits small and meaningful."
        ]

        for i, content in enumerate(notes):
            Note.objects.get_or_create(
                slug=f"note-{i}",
                defaults={
                    'title_en': f"Coding Tip #{i+1}",
                    'title_uk': f"Порада #{i+1}",
                    'content_en': content,
                    'content_uk': f"Українська версія: {content}",
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded database'))
