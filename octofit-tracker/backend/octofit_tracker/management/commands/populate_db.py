from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        thor = User.objects.create(name='Thor', email='thor@marvel.com', team=marvel)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        wonderwoman = User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300, date='2023-01-01')
        Activity.objects.create(user=captain, type='Cycling', duration=45, calories=400, date='2023-01-02')
        Activity.objects.create(user=thor, type='Swimming', duration=60, calories=500, date='2023-01-03')
        Activity.objects.create(user=superman, type='Flying', duration=120, calories=1000, date='2023-01-04')
        Activity.objects.create(user=batman, type='Martial Arts', duration=40, calories=350, date='2023-01-05')
        Activity.objects.create(user=wonderwoman, type='Running', duration=35, calories=320, date='2023-01-06')

        # Create workouts
        cardio = Workout.objects.create(name='Cardio', description='Cardio workout')
        strength = Workout.objects.create(name='Strength', description='Strength workout')
        flexibility = Workout.objects.create(name='Flexibility', description='Flexibility workout')
        cardio.suggested_for.set([ironman, captain, superman])
        strength.suggested_for.set([thor, batman])
        flexibility.suggested_for.set([wonderwoman])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, total_points=1200)
        Leaderboard.objects.create(team=dc, total_points=1670)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
