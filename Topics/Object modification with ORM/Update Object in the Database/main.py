call_mom = Task.objects.filter(description="call mom")[0]
call_mom.priority = 100500
call_mom.save()
