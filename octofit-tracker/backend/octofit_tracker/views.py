from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

def api_root(request, format=None):
    # Use codespace URL for endpoints to avoid HTTPS certificate issues
    codespace_url = 'https://humble-space-invention-vpgrv4px593xq6-8000.app.github.dev/'
    localhost_url = 'http://localhost:8000/'
    return Response({
        'users': codespace_url + 'api/users/?format=api',
        'teams': codespace_url + 'api/teams/?format=api',
        'activity': codespace_url + 'api/activity/?format=api',
        'leaderboard': codespace_url + 'api/leaderboard/?format=api',
        'workouts': codespace_url + 'api/workouts/?format=api',
        'users_local': localhost_url + 'api/users/?format=api',
        'teams_local': localhost_url + 'api/teams/?format=api',
        'activity_local': localhost_url + 'api/activity/?format=api',
        'leaderboard_local': localhost_url + 'api/leaderboard/?format=api',
        'workouts_local': localhost_url + 'api/workouts/?format=api',
    })
