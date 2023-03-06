from .models import Schedule


def get_month_salary(teacher, mount):
    schedules = Schedule.objects.filter(status='completed',
                                        teacher=teacher)
    salary = sum([schedule.webinar.rate * schedule.duration for schedule in schedules if
                  schedule.start_time.strftime('%Y-%m') == mount.strftime(
                      '%Y-%m')])
    return salary
