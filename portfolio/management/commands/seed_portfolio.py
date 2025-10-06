from django.core.management.base import BaseCommand
from django.utils.text import slugify
from portfolio.models import Project, Profile, Skill, Experience
from datetime import date


class Command(BaseCommand):
    help = "Seed the database with sample portfolio data"

    def handle(self, *args, **options):
        profile, _ = Profile.objects.get_or_create(
            name="Your Name",
            defaults={
                "tagline": "Full‑stack Developer",
                "bio": "I build clean, user‑centric web apps.",
                "location": "Your City",
            },
        )

        skills = [
            ("Python", 5, "🐍"),
            ("Django", 5, "🌿"),
            ("JavaScript", 4, "🟨"),
            ("React", 4, "⚛️"),
        ]
        for name, level, icon in skills:
            Skill.objects.get_or_create(name=name, defaults={"level": level, "icon": icon})

        Experience.objects.get_or_create(
            role="Software Engineer",
            company="Acme Inc.",
            start_date=date(2023, 1, 1),
            defaults={"description": "Worked on scalable features across the stack."},
        )

        projects = [
            {
                "title": "Sample Project",
                "description": "A demo project entry for the portfolio.",
                "github_url": "https://github.com/your/repo",
                "live_url": "https://example.com",
            }
        ]
        for p in projects:
            Project.objects.get_or_create(
                slug=slugify(p["title"]),
                defaults=p,
            )

        self.stdout.write(self.style.SUCCESS("Portfolio data seeded."))

