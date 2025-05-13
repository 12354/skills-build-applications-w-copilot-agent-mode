from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Add test data for users
        User.objects.create(email="john.doe@example.com", name="John Doe")
        User.objects.create(email="jane.smith@example.com", name="Jane Smith")

        # Add test data for teams
        Team.objects.create(name="Team Alpha")
        Team.objects.create(name="Team Beta")

        # Add test data for activities
        Activity.objects.create(description="Running 5km")
        Activity.objects.create(description="Swimming 1km")

        # Add test data for leaderboard
        Leaderboard.objects.create(rank=1)
        Leaderboard.objects.create(rank=2)

        # Add test data for workouts
        Workout.objects.create(title="Morning Yoga")
        Workout.objects.create(title="Evening Cardio")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
