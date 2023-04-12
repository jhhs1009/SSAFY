# accounts/views.py

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)

        if person != request.user:
            if person.request.filter(pk=request.user.pk).exists():
                person.request.remove(request.user)
            else:
                person.request.add(request.user)
        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')